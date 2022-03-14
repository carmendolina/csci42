from django.shortcuts import render, redirect

from django.http import HttpResponse

#forms
from .forms import IndexCardForm

from .models import IndexCard

from django.views import View
from django.views.generic.list import ListView
from django.views.generic.edit import DeleteView
from django.views.generic.detail import DetailView

import datetime

#insert functions here
def index(request):
    return redirect('index_card')


def index_card_view(request):
    form = IndexCardForm(request.POST)
    classes = IndexCard.objects.all()
    thislist = setting_time()
    mondaylist = monday()
    wednesdaylist = wednesday()

    if request.method == 'POST':
    # Checking if the inputs are valid
        if form.is_valid():
            form.save()
            return redirect("index_card")
    else:
        form = IndexCardForm()

    return render(request, 'index.html', {'form': form, 'class_info': classes, 'time': thislist, 'monday': mondaylist, 'wednesday': wednesdaylist})


def monday():
    mondays = []
    for mondayclass in IndexCard.objects.filter(sched__contains='M'):
        mondays.append(mondayclass)
    return mondays

def wednesday():
    wednesdays = []
    for wednesdayclass in IndexCard.objects.filter(sched__contains='W'):
        wednesdays.append(wednesdayclass)
    return wednesdays

def setting_time():
    starttime = datetime.datetime(100,1,1,7,00,00) # first 3 are dummy last 3 are hour/min/sec
    endtime = datetime.datetime(100,1,1,21,30,00)
    timelist = [];
    while (starttime < endtime):
        timelist.append(starttime.time);
        starttime += datetime.timedelta(0,30*60) # days, seconds, then other fields.
    return timelist;

#sources:
#Time - https://stackoverflow.com/questions/100210/what-is-the-standard-way-to-add-n-seconds-to-datetime-time-in-python