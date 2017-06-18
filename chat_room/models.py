from django.db import models
from django.contrib.auth.models import User
from django.conf import settings


class Message(models.Model):
    created = models.DateTimeField(auto_now_add=True)
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    message = models.CharField(max_length=200)
    receiver = models.CharField(max_length=40, null=False)

    def __unicode__(self):
        return self.message
