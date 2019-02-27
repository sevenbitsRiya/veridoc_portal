from django.db import models
import hashlib
from functools import partial

# Create your models here.
class VDG_M_ExcelDetails(models.Model):
    ID = models.AutoField(primary_key=True)
    Filename = models.CharField(max_length=2000,null=False)
    extention = models.CharField(max_length=200,null=False)
    publicGuid = models.CharField(max_length=200,null=False)
    Customer_ID = models.IntegerField(null=False,default=0)
    Filepath = models.CharField(max_length=200,null=False)
    progressStatus = models.IntegerField(null=False,default=0)    
    
    def __str__(self):
        return self.publicGuid
    


   


    