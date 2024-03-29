from django import forms

from tweets.models import Tweet

class TweetModelForm(forms.ModelForm):
    content = forms.CharField(label='', widget=forms.Textarea(attrs={'placeholder':"Your message", 'class':"form-control"}))
   #this will edit Meta
    class Meta:
        model = Tweet
        fields = [
            # "user",
            "content"
        ]

    # def clean_content(self):
    #     content = self.cleaned_data.get("content")
    #     if content == "abc":
    #         raise forms.ValidationError("Cannot be ABC")
    #     return content