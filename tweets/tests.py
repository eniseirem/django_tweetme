from django.test import TestCase
from django.contrib.auth import get_user_model
# Create your tests here.
from django.urls import reverse

from .models import Tweet

User = get_user_model()

class TweetModelTestCase(TestCase):
    def setUp(self):
       some_random_user = User.objects.create(username='enise33333333')
    def test_tweet_item(self):
        obj = Tweet.objects.create(
            user=User.objects.first(),
            content='Some random content'
        )
        self.assertTrue(obj.content == 'Some random content')
        self.assertTrue(obj.id == 1)
        #self.assertEqual(obj.id, 1)

        absolute_url = reverse("tweet:detail", kwargs={"pk":1})
        self.assertEqual(obj.get_absolute_url(), absolute_url)

    def test_tweet_url(self):
        obj = Tweet.objects.create(
            user=User.objects.first(),
            content='Some random content'
        )
        absolute_url = reverse("tweet:detail", kwargs={"pk":obj.pk})
        self.assertEqual(obj.get_absolute_url(), absolute_url)
