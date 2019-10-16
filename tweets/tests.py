from django.test import TestCase
from django.contrib.auth import get_user_model
# Create your tests here.

from .models import Tweet

User = get_user_model()

class TweetModelTestCase(TestCase):
    def setUp(self):
        Tweet.objects.create(
            user=User.objects.first(),
            content='Some random content'
        )
    def twst_tweet_item(self):
        obj = Tweet.objects.create(
            user = User.objects.first(),
            content = 'Some random content'
        )
        self.assetTrue(obj.content == 'Some random content')