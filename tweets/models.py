from django.db import models
from django.contrib.auth import get_user_model
# Create your models here.

class Tweet(models.Model):

    user = models.ForeignKey(get_user_model(), null=True, default=1, on_delete=models.DO_NOTHING)
    content     = models.CharField(max_length=280)
    updates     = models.DateTimeField(auto_now=True)
    timestamp   = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return str(self.content)

