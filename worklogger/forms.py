from django import forms
from django.contrib.auth import models

from bootstrap3_datetime.widgets import DateTimePicker

from .models import Log, Project


class LoginForm(forms.ModelForm):

    class Meta:
        model = models.User
        fields = ['username', 'password']
        widgets = {
            'password': forms.PasswordInput(),
        }


class LogForm(forms.Form):
    log_hours = forms.FloatField(max_value=24)
    project = forms.ModelChoiceField(queryset=Project.objects.all())
    remarks = forms.CharField(max_length=200)