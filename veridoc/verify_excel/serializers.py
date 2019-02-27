from rest_framework import serializers

class VDG_M_excelDetailsSerializer(serializers.Serializer):
    ID = serializers.AutoField(primary_key=True)
    Filename = serializers.CharField(max_length=2000,null=False)
    extention = serializers.CharField(max_length=200,null=False)
    publicGuid = serializers.CharField(max_length=200,null=False)
    Customer_ID = serializers.IntegerField(null=False,default=0)
    Filepath = serializers.CharField(max_length=200,null=False)
    progressStatus = serializers.IntegerField(null=False,default=0)    