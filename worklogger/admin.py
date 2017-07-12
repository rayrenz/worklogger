from django.contrib import admin

from .models import Project, Log


class ProjectAdmin(admin.ModelAdmin):
    fields = ['title', 'description']
    search_fields = ['title', 'description']


class LogAdmin(admin.ModelAdmin):
    fields = ['user', 'project', 'log_hours', 'date_logged']
    list_display = ['project', 'user', 'log_hours', 'date_logged']

admin.site.register(Project, ProjectAdmin)
admin.site.register(Log, LogAdmin)
