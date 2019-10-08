from django.shortcuts import render
from django.contrib.auth.mixins import LoginRequiredMixin #use this as a ready to use mixin
from django.db.models import Q
from django.views.generic import \
    (
    CreateView,
    ListView,
    DeleteView,
    DetailView,
    UpdateView)
from django.urls import reverse_lazy
from .forms import TweetModelForm
from .mixins import FormUserNeededMixin, UserOwnerMixin
from .models import Tweet


class TweetCreateView(FormUserNeededMixin, CreateView):
    form_class = TweetModelForm
    template_name = 'tweets/create_view.html'
    # success_url = reverse_lazy('tweet:create')
    #login_url =''


class TweetUpdateView(LoginRequiredMixin, UserOwnerMixin, UpdateView):
    queryset = Tweet.objects.all()
    form_class = TweetModelForm
    template_name = 'tweets/update_view.html'
    success_url = "/tweet/"

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

class TweetDeleteView(LoginRequiredMixin, DeleteView):
    model = Tweet
    form_class = TweetModelForm
    template_name = 'tweets/delete_confirm.html'
    success_url = reverse_lazy('tweet:list')

# List / Search

class TweetDetailView(DetailView):
    queryset = Tweet.objects.all()


class TweetListView(ListView):

    def get_queryset(self, *args, **kwargs):
        qs = Tweet.objects.all()
        query = self.request.GET.get("q", None)
        if query is not None:
            qs = qs.filter(
                Q(content__icontains=query)|
                Q(user__username__icontains=query))
        return qs

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