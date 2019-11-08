from rest_framework import serializers

from accounts.api.serializers import UserDisplaySerializer
from tweets.models import Tweet

class TweetModelSerializer (serializers.ModelSerializer):
    user= UserDisplaySerializer() #this data will be in user
    class Meta:
        model = Tweet
        fields = [
            'user',
            'content'
        ]



