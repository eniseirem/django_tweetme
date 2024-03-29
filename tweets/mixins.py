from  django import forms
from django.forms.utils import ErrorList

class FormUserNeededMixin(object):
#This could be in views part also.
    def form_valid(self, form):
        if self.request.user.is_authenticated:
            form.instance.user = self.request.user
            return super(FormUserNeededMixin, self).form_valid(form)
        else:
            form.errors[forms.forms.NON_FIELD_ERRORS] = ErrorList(["User must be logged in to continue"])
            return self.form_invalid(form)

class UserOwnerMixin(FormUserNeededMixin, object):
    def form_valid(self, form):
        if form.instance.user == self.request.user:
             return super(UserOwnerMixin, self).form_valid(form)
        else:
            form.errors[forms.forms.NON_FIELD_ERRORS] = ErrorList(["This user cannot edit this tweet."])
            return self.form_invalid(form)