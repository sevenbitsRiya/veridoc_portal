from django.contrib import admin
from .models import ApiKeyToken
# Register your models here.
class ApiKeyTokenAdmin(admin.ModelAdmin):
    readonly_fields=('key','secret_key')
admin.site.register(ApiKeyToken,ApiKeyTokenAdmin)