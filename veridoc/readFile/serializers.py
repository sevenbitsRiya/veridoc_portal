from rest_framework import serializers


class VDG_M_readFileSerializer(serializers.Serializer):
    key = serializers.CharField()
    secret_key = serializers.CharField()
    user = serializers.CharField()
    ID = serializers.IntegerField()
    Fileurl = serializers.URLField(max_length=500)
    Metadata = serializers.CharField(max_length=2000)
    Hash = serializers.CharField( max_length=2000)
    delimeter = serializers.CharField(max_length=200)
    VGuid = serializers.CharField(max_length=200)
    VPage = serializers.IntegerField(default=0)
    CustomeID = serializers.IntegerField(default=0)
    Status = serializers.IntegerField(default=0)
    Created_on = serializers.DateTimeField()
    Modified_on = serializers.DateTimeField()
    Created_by = serializers.IntegerField(default=0)
    Modified_by = serializers.IntegerField(default=0)
    ExcelId = serializers.IntegerField(default=0)
