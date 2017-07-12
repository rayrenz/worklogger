from django.db import models
from django.utils import timezone


class Project(models.Model):
    title = models.CharField(max_length=100)
    description = models.CharField(max_length=200)

    def __str__(self):
        return self.title


class Log(models.Model):
    user = models.ForeignKey('auth.User')
    project = models.ForeignKey(Project, on_delete=models.SET_NULL, null=True)
    log_hours = models.FloatField(blank=False)
    remarks = models.CharField(max_length=200, null=True)
    date_logged = models.DateTimeField(blank=False)
    created = models.DateTimeField(default=timezone.now())
    late = models.BooleanField(default=False)
