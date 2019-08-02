from django.shortcuts import render
from django.shortcuts import render,HttpResponse
from rest_framework.response import Response
from rest_framework.views import APIView
from django.utils import six
from apikey.models import ApiKeyToken
from django.contrib.auth.models import User
from verify_doc.models import VDG_M_documentDetails
from .serializers import VDG_M_readFileSerializer
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
import urllib
import urllib.request as urllib2

class VDG_M_readFileView(LoggingMixin,APIView):
    def post(self, request,*argv, **kwargs):
        if request.method == 'POST':
            key1 = self.request.META.get('HTTP_APIKEY',None)
            payload1 = self.request.META.get('HTTP_PAYLOAD',None)
            uniqueId = self.request.data['uniqueId']
            fileurl = self.request.data['fileurl']
            metadata =  self.request.data['metadata']
            delimeter = self.request.data['delimeter']
            if not uniqueId:
                response_data  = {}
                response_data['returncode'] = '2'
                response_data['message'] = 'UniqueId not found'
                return HttpResponse(json.dumps(response_data), content_type="application/json")
            if not key1:
                response_data  = {}
                response_data['returncode'] = '2'
                response_data['message'] = 'Apikey not found'
                return HttpResponse(json.dumps(response_data), content_type="application/json")
            if not payload1:
                response_data  = {}
                response_data['returncode'] = '2'
                response_data['message'] = 'Payload not found'
                return HttpResponse(json.dumps(response_data), content_type="application/json")
            payload1 = payload1.lower()                      
            #que = ApiKeyToken.objects.filter(key = key1).values_list('secret_key', flat=True)            
            que = ApiKeyToken.objects.filter(key = key1).first()
            if not que:
                response_data  = {}
                response_data['returncode'] = '2'
                response_data['message'] = 'Sorry you are not authorized user!!'
                context = {'response_data':response_data}
                return HttpResponse(json.dumps(response_data), content_type="application/json")  
            sec_key = que.secret_key
            secret = key1+uniqueId+fileurl+metadata+delimeter+sec_key            
            hash_object = hashlib.sha256(str(secret).encode('utf-8'))
            payload = hash_object.hexdigest()
            if payload != payload1:
                response_data  = {}
                response_data['returncode'] = '2'
                response_data['message'] = 'Sorry you are not authorized user...!!'
                context = {'response_data':response_data}
                return HttpResponse(json.dumps(response_data), content_type="application/json")

            id_get = VDG_M_documentDetails.objects.filter(VGuid = uniqueId).first() 
            if not id_get:
                response_data  = {}
                response_data['returncode'] = '2'
                response_data['message'] = 'UniqueId not found'
                context = {'response_data':response_data}
                return HttpResponse(json.dumps(response_data), content_type="application/json")  

            if id_get.CustomeID !=que.user.id :
                response_data  = {}
                response_data['returncode'] = '2'
                response_data['message'] = 'Sorry you are not authorized user...!!'
                context = {'response_data':response_data}
                return HttpResponse(json.dumps(response_data), content_type="application/json") 

            try:
                sha256 = hashlib.sha256()
                txt = urllib2.urlopen(fileurl).read()
                sha256.update(txt) 
                h2 = sha256.hexdigest()
            except urllib.error.URLError as e:
                response_data  = {}
                response_data['returncode'] = '2'
                response_data['message'] = 'No such file Found.'
                return HttpResponse(json.dumps(response_data), content_type="application/json")            
            
            id_get.Fileurl = fileurl
            id_get.Metadata = metadata
            id_get.Hash = h2
            id_get.delimeter = delimeter
            id_get.Modified_on = datetime.datetime.now()
            id_get.Modified_by = que.user.id                 
            id_get.save()

            response_data  = {}
            response_data['returncode'] = '1'
            response_data['message'] = 'Value updated successfully.'
            response_data['uniqueId'] = uniqueId
            response_data['FileHash'] = h2
            return HttpResponse(json.dumps(response_data), content_type="application/json")
