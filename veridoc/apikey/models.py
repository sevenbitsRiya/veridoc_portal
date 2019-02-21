from __future__ import unicode_literals
from django.db import models
from django.contrib.auth.models import User
import binascii
import random
import string
import os
from django.conf import settings
from django.db.models.signals import post_save
from django.dispatch import receiver

# Create your models here.
class ApiKeyToken(models.Model):
    key = models.CharField(max_length=40, primary_key=True)
    secret_key = models.CharField(max_length=60,)
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    is_active = models.BooleanField(default=True)

    def save(self, *args, **kwargs):
        if not self.key:
            self.key = self.generate_key()
            self.secret_key = self.generate_secret_key()
        return super(ApiKeyToken, self).save(*args, **kwargs)
    
    def refresh(self, *args, **kwargs):
        if self.key:
            self.key = self.generate_key()
            self.secret_key = self.generate_secret_key()
        return super(ApiKeyToken, self).save(*args, **kwargs)
    
    def generate_key(self):
        return binascii.hexlify(os.urandom(20)).decode()

    def generate_secret_key(self):
        return ''.join(random.choice(string.ascii_letters + string.digits) for _ in range(60))
    
    def __unicode__(self):
        return self.key,self.secret_key
    
    def get_api_key(self):
        return self.key
    
    def get_sectret_key(self):
        return self.secret_key

    @receiver(post_save, sender=User)
    def create_auth_token(sender, instance=None, created=False, **kwargs):
        if created:
            ApiKeyToken.objects.create(user=instance)
