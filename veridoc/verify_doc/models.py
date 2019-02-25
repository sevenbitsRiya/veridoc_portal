from django.db import models
import hashlib
from functools import partial

# Create your models here.
class VDG_M_documentDetails(models.Model):
    ID = models.AutoField(primary_key=True)
    Fileurl = models.URLField(max_length=500,null=False)
    Metadata = models.CharField(max_length=2000,null=False)
    Hash = models.CharField( max_length=2000,null=False)
    delimeter = models.CharField(max_length=200,null=False)
    VGuid = models.CharField(max_length=200,null=False)
    VPage = models.IntegerField(default=0,null=False)
    CustomeID = models.IntegerField(default=0,null=False)
    Status = models.IntegerField(default=0,null=False)
    Created_on = models.DateTimeField(auto_now_add=True,null=False)
    Modified_on = models.DateTimeField(auto_now=True,null=False)
    Created_by = models.IntegerField(default=0,null=False)
    Modified_by = models.IntegerField(default=0,null=False)
    ExcelId = models.IntegerField(default=0,null=False)
    
    def __str__(self):
        return self.Hash

    def hash_file(Fileurl, block_size=65536):
        hasher = hashlib.md5()
        for buf in iter(partial(Fileurl.read, block_size), b''):
            hasher.update(buf)
        return hasher.hexdigest()
    



    