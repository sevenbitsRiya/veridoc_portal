from django.shortcuts import render
from django.shortcuts import render,HttpResponse
from rest_framework.response import Response
from rest_framework.views import APIView
from django.utils import six
from apikey.models import ApiKeyToken
from django.contrib.auth.models import User
from .models import VDG_M_readFile
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
            fileurl = self.request.META.get('HTTP_FILEURL',None)
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
            if not fileurl:
                response_data  = {}
                response_data['returncode'] = '2'
                response_data['message'] = 'Fileurl not found'
                return HttpResponse(json.dumps(response_data), content_type="application/json")
            

            # with open(fileurl, 'r') as myfile:
            #   data = myfile.read()
            txt = urllib.urlopen(fileurl).read()

            #data = urllib2.urlopen(fileurl).read() # read only 20 000 chars
            #data = data.split("\n") # then split it into lines
            #for line in data:
            #    print(line)

            response_data  = {}
            response_data['result'] = '1'
            response_data['message'] = ''
            response_data['uniqueId'] = '1'
            response_data['qr'] = 'http://127.0.0.1:8000/verify/'
            response_data['file'] = 'file:'+txt
 
            
            return HttpResponse(json.dumps(response_data), content_type="application/json")
              

            # payload1 = payload1.lower()                      
            # que = ApiKeyToken.objects.filter(key = key1).values_list('secret_key', flat=True)            
            # if not que:
            #     response_data  = {}
            #     response_data['result'] = '2'
            #     response_data['message'] = 'Sorry you are not authorized user!!'
            #     context = {'response_data':response_data}
            #     return HttpResponse(json.dumps(response_data), content_type="application/json")    
            # sec_key = que[0]
            # secret = key1+sec_key
            # hash_object = hashlib.sha256(str(secret).encode('utf-8'))
            # payload = hash_object.hexdigest()
            # file_name = 'client_secret_driv.json'
            # file_id = service.files().list(q="name='" + file_name + "' and trashed=false", fields="files(id)").execute()
            # permissions = service.permissions().list(fileId=file_id["files"][0]["id"]).execute()
            # result = permissions.get('permissions', [])
        
            # if payload != payload1:
            #     response_data  = {}
            #     response_data['result'] = '2'
            #     response_data['message'] = 'Sorry you are not authorized user...!!'
            #     context = {'response_data':response_data}
            #     return HttpResponse(json.dumps(response_data), content_type="application/json")
            # response_data  = {}
            # response_data['result'] = '1'
            # response_data['message'] = ''
            # response_data['uniqueId'] = '1'
            # response_data['qr'] = 'http://127.0.0.1:8000/verify/'
            # context = {'response_data':response_data}                    
            # return HttpResponse(json.dumps(response_data), content_type="application/json")
              
            