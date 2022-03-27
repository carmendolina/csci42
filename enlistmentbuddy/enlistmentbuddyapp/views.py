from django.shortcuts import render, redirect

from django.http import HttpResponse

#forms
from .forms import IndexCardForm
from .forms import CopyPasteForm

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
    indexcardform = IndexCardForm(request.POST)
    copypasteform = CopyPasteForm(request.POST)
    classes = IndexCard.objects.all()
    thislist = setting_time()
    mondaylist = monday()
    tuesdaylist = tuesday()
    wednesdaylist = wednesday()
    thursdaylist = thursday()
    fridaylist = friday()
    saturdaylist = saturday()
    courselist = coursecodes()
    thiscourse = courselist[1];
    #over here peeps

    if request.method == 'POST':
    # Checking if the inputs are valid
        if 'indexsubmit' in request.POST:
            indexcardform = IndexCardForm(request.POST)
            if indexcardform.is_valid():
                indexcardform.save()
                return redirect("index_card")
        elif 'copypastesubmit' in request.POST:
            copypasteform = CopyPasteForm(request.POST)
            if copypasteform.is_valid():
                #copypasteform.save()
                #https://stackoverflow.com/questions/12518517/request-post-getsth-vs-request-poststh-difference
                text = request.POST.get('copypaste')
                print(text)
                #if len(text.split("\t")) > 14:
                #smth smth join every 14 together
                fieldlist = split(text)
                print(fieldlist[0])
                newClass = IndexCard(code=fieldlist[0], section=fieldlist[1], sched=fieldlist[2], start=fieldlist[3], end=fieldlist[4], venue=fieldlist[5], professor=fieldlist[6], copypaste=text)
                newClass.save()
                return redirect("index_card")
    else:
        indexcardform = IndexCardForm()
        copypasteform = CopyPasteForm()

    return render(request, 'index.html', 
        {
            'indexcardform': indexcardform, 
            'copypasteform': copypasteform,
            'class_info': classes, 
            'time': thislist,
            'monday': mondaylist,
            'tuesday': tuesdaylist,
            'wednesday': wednesdaylist,
            'thursday': thursdaylist,
            'friday': fridaylist,
            'saturday': saturdaylist,

            'courses': courselist,
            'trycourse': thiscourse,
            #over here peeps
        }
    )

#sources:
#https://docs.djangoproject.com/en/4.0/topics/db/queries/
# copy and paste function, rename day of week to corresponding day, then put in def index_card_view, and add it into return

def timeConvert(text):
    return text[:2] + ':' + text[2:]

def split(text):
    splitfields = []
    moresplit = []
    timesplit = []
    namesplit = []
    finalfields = []
    #for copiedText in text:
    listOfClasses = text
    splitByTabIndents = text.split("\t")
    for x in splitByTabIndents:
        splitfields.append(x)
    for y in splitfields[4].split(" "):
        moresplit.append(y)
    for z in moresplit[1].split("-"):
        timesplit.append(z)
    for a in splitfields[6].split(","):
        namesplit.append(a)
    finalfields.append(splitfields[0])
    finalfields.append(splitfields[1])
    finalfields.append(moresplit[0])
    finalfields.append(timeConvert(timesplit[0]))
    finalfields.append(timeConvert(timesplit[1]))
    finalfields.append(splitfields[5])
    finalfields.append(namesplit[0])

    return finalfields

def monday():
    mondays = []
    for mondayclass in IndexCard.objects.filter(sched__contains='M'):
        mondays.append(mondayclass)
    return mondays

def tuesday():
    tuesdays = []
    tueslist = IndexCard.objects.filter(sched__contains='T-') |  IndexCard.objects.filter(sched__iexact='T')
    for tuesdayclass in tueslist:
        tuesdays.append(tuesdayclass)
    return tuesdays

def wednesday():
    wednesdays = []
    for wednesdayclass in IndexCard.objects.filter(sched__contains='W'):
        wednesdays.append(wednesdayclass)
    return wednesdays

def thursday():
    thursdays = []
    for thursdayclass in IndexCard.objects.filter(sched__contains='TH'):
        thursdays.append(thursdayclass)
    return thursdays

def friday():
    fridays = []
    for fridayclass in IndexCard.objects.filter(sched__contains='F'):
        fridays.append(fridayclass)
    return fridays

def saturday():
    saturdays = []
    for saturdayclass in IndexCard.objects.filter(sched__contains='SAT'):
        saturdays.append(saturdayclass)
    return saturdays

def setting_time():
    starttime = datetime.datetime(100,1,1,7,00,00) # first 3 are dummy last 3 are hour/min/sec
    endtime = datetime.datetime(100,1,1,21,30,00)
    timelist = []
    while (starttime < endtime):
        timelist.append(starttime.time)
        starttime += datetime.timedelta(0,30*60) # days, seconds, then other fields.
    return timelist

def coursecodes():
    courselist = []
    for course in IndexCard.objects.all():
        if course.code not in courselist:
            courselist.append(course.code)
    return courselist

def checkoverlap():
    return null

#sources:
#Time - https://stackoverflow.com/questions/100210/what-is-the-standard-way-to-add-n-seconds-to-datetime-time-in-python