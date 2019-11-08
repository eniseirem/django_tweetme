from django.urls import path
from django.views.generic.base import RedirectView

# from tweets import views

from .views import (TweetListAPIView)

urlpatterns = [
#     path('', RedirectView.as_view(url='None')),
      path('', TweetListAPIView.as_view(), name="list"), # /api/tweet
#     path('create/', views.TweetCreateView.as_view(), name="create"),
#     path('<pk>/', views.TweetDetailView.as_view(), name="detail"),
#     path('<pk>/update/', views.TweetUpdateView.as_view(), name="update"),
#     path('<pk>/delete/', views.TweetDeleteView.as_view(), name="delete")
]
