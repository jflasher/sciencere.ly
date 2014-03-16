from django.contrib import admin
from django.contrib.auth.forms import UserChangeForm, UserCreationForm
from account.models import UserProfile
from django import forms


class MyUserChangeForm(UserChangeForm):
    class Meta(UserChangeForm.Meta):
        model = UserProfile


class MyUserCreationForm(UserCreationForm):
    class Meta(UserCreationForm.Meta):
        model = UserProfile

    def clean_username(self):
        username = self.cleaned_data['username']
        try:
            UserProfile.objects.get(username=username)
        except UserProfile.DoesNotExist:
            return username
        raise forms.ValidationError(self.error_messages['duplicate_username'])

admin.site.register(UserProfile)