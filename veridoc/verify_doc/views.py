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
                
        return render(request,"apikey/credentials.html")
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
             #VDG_M_documentDetails.Created_by = User.username



                    #serializer = VDG_M_documentDetailsSerializer(response_data, many=True)
                    #return Response({"response_data": serializer.data})
                    #return render(request,json.dumps(response_data))
                    #return HttpResponse(response_data)
                   
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            #if key1 is None:
             #   response_data = {}
              #  response_data['result'] = '1'
               # response_data['message'] = 'Apikey not found!!'
                #return render(request,json.dumps(response_data))     
          #  else:
           #     if payload is None:
            #        response_data['result'] = '1'
             #       response_data['message'] = 'payload not found!!'
              #      return render(request,json.dumps(response_data)) 
               # else:
                    #return_code = 0
                #    que = ApiKeyToken.objects.filter(key = key1).values_list('secret_key', flat=True)
                 #   sec_key = que[0]
                  #  print(sec_key)
                    #secret = key1+sec_key
                    #m = hashlib.sha256()
                    #m.update(key1 + sec_key)
                    #payload = m.digest()
                    #serializer = VDG_M_documentDetailsSerializer(payload, many=True)
                   # response_data = {'sec_key':sec_key}
                    #response_data['result'] = ''
                    #response_data['message'] = ''
                    #return Response({"payload": serializer.data})
                    #return Response(request,json.dumps(response_data),{'sec_key':sec_key})
        #else:
         #   return HttpResponse(request,"You are not authenticated to use this !!!!")               






                #data = ApiKeyToken.objects.find('secret_key',flat=True).filter(key=key)
                #print(que.get(secret_key))
#                sec_key = que.get('secret_key')
 ##                   sec_key.encode('utf-8'),
   #                 digestmod=sha256
    #                ).digest()
     #           signature = b64encode(computed_sig).decode()
                #sec_key = que.getattr('secret_key')
                #serializer = VDG_M_documentDetailsSerializer(que, many=True)
                #return Response({"queryset": serializer.data})
                #return Response({"quer": que})


          #return HttpResponse(secret_key,'Not found')
                #sec_key = queryset.filter(key = key).only('secret_key')
               # print(getattr(sec_key,secret_key))
                #qur = queryset.filter(Q(key = key) & Q(secret_key = secretkey))
                #print(queryset.get('user'))
              
        #ap_key = request.GET['apikey']
        #apikey = ApiKeyToken.objects.all(key = kwargs['ap_key'])
        #serializer = VDG_M_documentDetailsSerializer(apikey, many=True)
        #return Response({"apikey": serializer.data})
      
       # print(apikey)
       
       # if request.META.get(apikey=kwargs[key]):
        #    return HttpResponse(request,"api keyyyyy found") 
        #else:
         #   return HttpResponse(request,"Not found")
        #else:  
         #   docs = VDG_M_documentDetails.objects.all()
            # the many param informs the serializer that it will be serializing more than a single article.
          #  serializer = VDG_M_documentDetailsSerializer(docs, many=True)
           # return Response({"docs": serializer.data})

            #user1 = ApiKeyToken.objects.filter(key = key).values("user")
            #id = user1.get('user_id')
            #user2 = User.objects.get(id = user1.get('user_id',None)).values("username")
            #print(user1)
