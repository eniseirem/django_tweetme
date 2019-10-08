from django.conf import settings
from django.db import models
from django.contrib.auth import get_user_model
# Create your models here.
from .validators import validate_content
class Tweet(models.Model):

    user = models.ForeignKey(get_user_model(), null=True, default=1, on_delete=models.DO_NOTHING)
    content     = models.CharField(max_length=280, validators=[validate_content])
    updates     = models.DateTimeField(auto_now=True)
    timestamp   = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return str(self.content)

    # def clean(self, *args, **kwargs):
    #     content = self.content
    #     if content == "abc":
    #         raise ValidationError("Content cannot be ABC")
    #     return super(Tweet, self).clean(*args, **kwargs)
