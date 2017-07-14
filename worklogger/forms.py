from django import forms

from .models import Project


class LoginForm(forms.Form):
    password = forms.CharField(widget=forms.PasswordInput(attrs={'class': 'form-control'}))
    username = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control'}))


class LogForm(forms.Form):
    log_hours = forms.FloatField()
    project = forms.ModelChoiceField(queryset=Project.objects.all(), widget=forms.Select(
        attrs={'class': 'form-control'}))
    remarks = forms.CharField(max_length=200, widget=forms.TextInput(attrs={'class': 'form-control'}))