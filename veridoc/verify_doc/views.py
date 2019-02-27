from django.shortcuts import render,HttpResponse
from .forms import VDG_M_documentDetailsForm
from rest_framework.response import Response
from rest_framework.views import APIView
from django.utils import six
from .models import VDG_M_documentDetails
from apikey.models import ApiKeyToken
from django.contrib.auth.models import User

from .serializers import VDG_M_documentDetailsSerializer
from rest_framework import generics
from rest_framework.response import Response
from rest_framework_tracking.mixins import LoggingMixin
from django.db.models import Q
import hmac
import base64
from base64 import b64encode
from hashlib import sha256
import hashlib
from django.http import JsonResponse
from django.http import Http404
import uuid
import json
import datetime
from django.views.decorators.csrf import csrf_exempt


class VDG_M_documentDetailsView(LoggingMixin,APIView):
    def post(self, request,*argv, **kwargs):
        if request.method == 'POST':
            key1 = self.request.META.get('HTTP_APIKEY',None)
            payload1 = self.request.META.get('HTTP_PAYLOAD',None)
            if not key1:
                response_data  = {}
                response_data['returncode'] = '2'
                response_data['message'] = 'Apikey not found'
                context = {'response_data':response_data}
                return HttpResponse(json.dumps(response_data), content_type="application/json")
            if not payload1:
                response_data  = {}
                response_data['returncode'] = '2'
                response_data['message'] = 'Payload not found'
                context = {'response_data':response_data}
                return HttpResponse(json.dumps(response_data), content_type="application/json")

            payload1 = payload1.lower()                      
            que = ApiKeyToken.objects.filter(key = key1).values_list('secret_key', flat=True)            
            if not que:
                response_data  = {}
                response_data['result'] = '2'
                response_data['message'] = 'Sorry you are not authorized user!!'
                context = {'response_data':response_data}
                return HttpResponse(json.dumps(response_data), content_type="application/json")    
            
            sec_key = que[0]
            secret = key1+sec_key
            hash_object = hashlib.sha256(str(secret).encode('utf-8'))
            payload = hash_object.hexdigest()
            if payload != payload1:
                response_data  = {}
                response_data['result'] = '2'
                response_data['message'] = 'Sorry you are not authorized user...!!'
                context = {'response_data':response_data}
                return HttpResponse(json.dumps(response_data), content_type="application/json")

            guid=str(uuid.uuid4())

            que = ApiKeyToken.objects.filter(key = key1).values_list('user', flat=True)            
            customerId=que[0]                           
            doc = VDG_M_documentDetails(
                VGuid= guid,
                VPage=1,
                CustomeID=customerId,
                Status=1,
                Created_on=datetime.datetime.now(),
                Modified_on=datetime.datetime.now(),
                Created_by=customerId,
                Modified_by=customerId
            )
            #serializer = VDG_M_documentDetailsSerializer(doc, many=True)
            
            doc.save()

            response_data  = {}
            response_data['result'] = '1'
            response_data['message'] = ''
            response_data['uniqueId'] = doc.VGuid
            response_data['qr'] = 'http://127.0.0.1:8000/verify/'+doc.VGuid
            context = {'response_data':response_data}                    
            return HttpResponse(json.dumps(response_data), content_type="application/json")
                
