from django.shortcuts import render
from  django import forms
from django.forms.utils import ErrorList
from django.views.generic import ListView,DetailView, CreateView
from .forms import TweetModelForm
from .models import Tweet
# Create your views here.
#
# Create
class TweetCreateView (CreateView):
    form_class = TweetModelForm
    template_name = 'tweets/create_view.html'
    success_url = '/tweet/'
    def form_valid(self, form):
        if self.request.user.is_authenticated:
            form.instance.user = self.request.user
            return super(TweetCreateView, self).form_valid(form)
        else:
            form.errors[forms.forms.NON_FIELD_ERRORS] = ErrorList(["User must be logged in to continue"])
            return self.form_invalid(form)

# def tweet_create_view(request):
#     form = TweetModelForm(request.POST or None)
#     if form.is_valid():
#         instance = form.save(commit=false)
#         instance.user = request.user
#         instance.save()
#     context ={
#         "form":form
#     }
#     return render(request, 'tweets/create_view.html',context)
# Retrieve
#
# Update
#
# Delete
#
# List / Search

class TweetDetailView(DetailView):
    # template_name = "tweets/detail_view.html"
    queryset = Tweet.objects.all()

    # def get_object(self):
    #     pk = self.kwargs.get("pk")
    #     return Tweet.objects.get(id=pk)

class TweetListView(ListView):
    # template_name = "tweets/list_view.html"
    queryset = Tweet.objects.all()
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        # context["another list"] = Tweet.objects.all()
        return context

#Function Based
# def tweet_detail_view(request, pk=None):
#     obj = Tweet.objects_or_404(Tweet, pk=pk) #GET from db
#     print(obj)
#     context = {
#         "object": obj
#     }
#     return render(request,"tweets/detail_view.html",context)
#
#
# def tweet_list_view(request):
#     queryset = Tweet.objects.all()
#     print(queryset)
#     for object in queryset:
#         print(object.content)
#     context = {
#         "object_list": queryset
#     }
#     return render(request, "tweets/list_view.html", context)