from django.shortcuts import render
from .models import ApiKeyToken
from django.http import HttpResponse
from django.http import HttpResponseRedirect

# Create your views here.
def get_api_key(self,request):
    if request.user.is_authenticated:
        username = request.user.username
        apikey = ApiKeyToken.objects.all()
        if apikey.user == username:
            return apikey.Key
        args = {'apikey': apikey}
    else:
        return HttpResponseRedirect('/accounts/user_login/')
    return render(request,args)
