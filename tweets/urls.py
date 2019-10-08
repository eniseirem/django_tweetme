from django.urls import path

from tweets import views

urlpatterns = [
    path('', views.TweetListView.as_view(), name="list"),
    path('create/', views.TweetCreateView.as_view(), name="create"),
    path('<pk>/', views.TweetDetailView.as_view(), name="detail"),
    path('<pk>/update/', views.TweetUpdateView.as_view(), name="update"),
    path('<pk>/delete/', views.TweetDeleteView.as_view(), name="delete")
]
