from django.shortcuts import render,HttpResponse
from .forms import VDG_M_excelDetailsForm
from rest_framework.response import Response
from rest_framework.views import APIView
from django.utils import six
from .models import VDG_M_ExcelDetails
from django.contrib.auth.models import User
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
from apikey.models import ApiKeyToken

# Create your views here.
class VDG_M_ExcelDetailsView(LoggingMixin,APIView):
    def post(self, request,*argv, **kwargs):
        if request.method == 'POST':
            status = 0
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

            #user request body check
            if not self.request.data:
                response_data  = {}
                response_data['result'] = '2'
                response_data['message'] = 'You didnot passed anything in body!!'
                context = {'response_data':response_data}
                return HttpResponse(json.dumps(response_data), content_type="application/json")    
            
            if not self.request.data['uniqueId']:
                response_data  = {}
                response_data['result'] = '2'
                response_data['message'] = 'You didnot passed uniqueId in body!!'
                context = {'response_data':response_data}
                return HttpResponse(json.dumps(response_data), content_type="application/json")    
            
            if not self.request.data['Fileurl']:
                response_data  = {}
                response_data['result'] = '2'
                response_data['message'] = 'You didnot passed Fileurl in body!!'
                context = {'response_data':response_data}
                return HttpResponse(json.dumps(response_data), content_type="application/json")    
            
            if not self.request.data['Metadata']:
                response_data  = {}
                response_data['result'] = '2'
                response_data['message'] = 'You didnot passed Metadata in body!!'
                context = {'response_data':response_data}
                return HttpResponse(json.dumps(response_data), content_type="application/json")    
            
            if not self.request.data['Delimieter']:
                response_data  = {}
                response_data['result'] = '2'
                response_data['message'] = 'You didnot passed Delimieter in body!!'
                context = {'response_data':response_data}
                return HttpResponse(json.dumps(response_data), content_type="application/json")    
            #generate payload for verification
            secret = key1+self.request.data['uniqueId']+self.request.data['Fileurl']+self.request.data['Metadata']+self.request.data['Delimieter']+sec_key
            hash_object = hashlib.sha256(str(secret).encode('utf-8'))
            payload = hash_object.hexdigest()
            if payload != payload1:
                response_data  = {}
                response_data['result'] = '2'
                response_data['message'] = 'Sorry you are not authorized user...!!'
                return HttpResponse(json.dumps(response_data), content_type="application/json")

            #guid=str(uuid.uuid4())

            que = ApiKeyToken.objects.filter(key = key1).values_list('user', flat=True)            
            customerId=que[0] 
            status = 1
            doc = VDG_M_ExcelDetails(
                Filename = "https://google.com/",
                extention = ".html",
                publicGuid = self.request.data['uniqueId'],
                Customer_ID = customerId,
                Filepath = self.request.data['Fileurl'],
                progressStatus = status,
                
            )
            doc.save()
            response_data  = {}
            response_data['result'] = '1'
            response_data['message'] = 'You are authorized user!!'
            response_data['CustometId'] = customerId
            response_data['progress status'] = status
            return HttpResponse(json.dumps(response_data), content_type="application/json")
                