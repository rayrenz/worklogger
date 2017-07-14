from datetime import datetime

from django.shortcuts import render, redirect
from django.core.urlresolvers import reverse
from django.http import HttpResponseRedirect
from django.contrib.auth import login, logout, authenticate
from django.utils import timezone

from .forms import LoginForm, LogForm
from .models import Project, Log


def index(request):
    if request.user.is_authenticated() and request.user.is_active:
        if request.method == 'POST':
            date = request.POST['date']
            if date != '':
                request.session['log_date'] = date
                return redirect('log:logs')
        return render(request, 'worklogger/index.html')

    return HttpResponseRedirect(reverse('log:login'))


def login_view(request):
    message = ''
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            username = request.POST['username']
            password = request.POST['password']
            user = authenticate(username=username, password=password)
            if user is not None:
                login(request, user)
                if user.is_staff:
                    return HttpResponseRedirect(reverse('admin:index'))
                return HttpResponseRedirect(reverse('log:index'))
            message = 'Invalid username/password!'
    else:
        form = LoginForm()
    return render(request, 'worklogger/login.html', {'form': form, 'message': message})


def logout_view(request):
    logout(request)
    return HttpResponseRedirect(reverse('log:index'))


def logs(request):
    # convert the text format date to a date object
    date = (datetime.strptime(request.session['log_date'], "%Y-%m-%d").date())
    if request.method == 'POST':
        # get the form and its values
        form = LogForm(request.POST)
        if form.is_valid():
            project_id = request.POST['project']
            project = Project.objects.filter(id=int(project_id))[0]
            mylog = Log()
            mylog.project = project
            mylog.remarks = request.POST['remarks']
            mylog.date_logged = date
            mylog.user = request.user
            mylog.log_hours = request.POST['log_hours']
            mylog.save()
            return HttpResponseRedirect(reverse('log:logs'))
    else: # form is a new instance for a get request
        form = LogForm()

    # get queryset of log objects
    logs = Log.objects.filter(
        user=request.user,
        date_logged__day=date.day,
        date_logged__month=date.month,
        date_logged__year=date.year
    ).order_by('-date_logged')

    # total the log hours
    total = 0
    for log in logs:
        total += log.log_hours

    return render(request, 'worklogger/logs.html', {
        'form': form,
        'logs': logs,
        'total': total,
        'date': date,
    })
