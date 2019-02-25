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
from base64 import b64encode
from hashlib import sha256
import json

class VDG_M_documentDetailsView(LoggingMixin,APIView):
    def get(self, request, **kwargs):
        if self.request.method == 'GET':
            queryset = ApiKeyToken.objects.all()
            key = self.request.GET.get('apikey',None)
            payload = self.request.GET.get('payload',None)            
            if key is None:
                response_data = {}
                response_data['result'] = 'error'
                response_data['message'] = 'Some error message'
                return render(request,json.dumps(response_data)) 
            else:
                return_code = 0
                que = ApiKeyToken.objects.filter(key = key).values_list('secret_key', flat=True).order_by('user_id')
                sec_key = que[0]
                response_data = {'sec_key':sec_key}
                response_data['result'] = 'error'
                response_data['message'] = 'Some error message'
                return render(request,json.dumps(response_data),{'sec_key':sec_key})
        else:
            return HttpResponse(request,"You are not authenticated to use this !!!!")               






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
