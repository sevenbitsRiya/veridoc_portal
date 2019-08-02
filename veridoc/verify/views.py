from django.shortcuts import render,redirect
from django.http import HttpResponse
from .forms import DocumentForm
import urllib
import urllib.request as urllib2
from hashlib import sha256
import hashlib
from django.contrib.auth.models import User
from verify_doc.models import VDG_M_documentDetails 
from django.contrib.auth.decorators import login_required

# Create your views here.
@login_required
def mydoc_view(request):
    user_id = request.user.id
    hash_arr = VDG_M_documentDetails.objects.all().filter(CustomeID = user_id)
    return render(request,'verify/mydocument.html',{'user_id':user_id,'hash_arr': hash_arr})

def verify_page(request,uniqeId):
    if request.method == 'GET':
        if not uniqeId:
            return HttpResponse("Page not found")
        id1 = VDG_M_documentDetails.objects.filter( VGuid = uniqeId).first()
        if not id1:
            return HttpResponse("Page not found")
        
        file_url1=id1.Fileurl
        hash1=""
        try:
            sha256 = hashlib.sha256()
            txt = urllib2.urlopen(file_url1).read()
            sha256.update(txt) 
            hash1 = sha256.hexdigest()
            
        except urllib.error.URLError as e:
            return render(request,'verify/verify.html',{'status':False,'failedStage':1})
        print(hash1)
        if id1.Hash != hash1:
            return render(request,'verify/verify.html',{'status':False,'failedStage':2})
        
        customer_ID = id1.CustomeID        
        unique_id = id1.VGuid
        created_on1=""

    return render(request,'verify/verify.html',{'customer_ID':customer_ID,'unique_id':unique_id ,'hash1':hash1,'created_on1':created_on1,'file_url1':file_url1})

def doc_view(request):

    return render(request,'verify/doc.html')

