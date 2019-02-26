from django.shortcuts import render
from apikey.models import ApiKeyToken
from django.http import HttpResponse
from django.http import HttpResponseRedirect

# Create your views here.
'''def get_api_key(self,request):
    if request.user.is_authenticated:
        username = request.user.username
        apikeys = ApiKeyToken.objects.all()
        output =  ".".join([str (apikey)for apikey in apikeys])
        #if apikey.user == username:
        #    return apikey.Key
        args = {'apikeys': apikeys,'output': output}
    else:
        return HttpResponseRedirect('/accounts/user_login/')
    return render(request,args)

def apikey(request):
    a = ApiKeyToken.objects.all()
    output = ",".join([str (apikey)for apikey in a])
    return HttpResponse(output) 

a = ApiKeyToken.objects.all()
'''
def key(self,request):
    if request.user.is_authenticated:
        username = request.user.username
        apikey = ApiKeyToken.objects.all()
        key = ApiKeyToken.objects.only('key').get(user__username = username).key
        sec_key = ApiKeyToken.objects.only('secret_key').get(user__username = username).secret_key
        context = {'key':key, 'sec_key':sec_key}
        return render(request,"apikey/credentials.html",context)
    return render(request,"apikey/credentials.html")
    