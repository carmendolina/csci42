from calendar import c
# from math import comb
import random
from ast import Index
import sched
from tabnanny import check
from django.shortcuts import render, redirect
import re, itertools

from django.http import HttpResponse

#forms
from .forms import CopyPasteForm
from .forms import ClassCopyPasteForm
from .forms import LockedForm, FilterForm
from .forms import CourseForm, CodeForm

from .models import ClassModel, ClassCode

from django.views import View
from django.views.generic.list import ListView
from django.views.generic.edit import DeleteView
from django.views.generic.detail import DetailView

import datetime

colorList = [
    'red',
    'orange',
    'yellow',
    'green',
    'teal',
    'blue',
    'purple',
    'lavender',
    'pink',
    'magenta',
    'lightgray',
    'darkgray',
]

num = 1
schedulelist = []
for objects in ClassModel.objects.all():
    objects.islocked = False;

def assignColor(list):
    for thing in list:
        i = 0
        L(thing)
        for course in thing:
            course.color = colorList[i]
            start_sec= (course.start.hour*60+course.start.minute)*60+course.start.second
            end_sec= (course.end.hour*60+course.end.minute)*60+course.end.second
            course.duration = int(((end_sec-start_sec)/60.0)/30)
            course.days = course.sched
            # if course.islocked == False:
            #     course.locked = "unlocked"
            # else:
            #     course.locked = "locked"
            i = i + 1
            # L(course).append(course.color)
    return list


# def return_lock(request):
#     currentlock = request.data['field']
#     print(currentlock)
#     print("hello!")
#     return JsonResponse({'success':True})
        
def enlistmentbuddy_view(request):

    global num
    global copypaste
    global currentlock
    global schedulelist

    if request.method == 'POST':
        deletedtabs = request.POST.get('returndeltab')
        print("HERE")
        print(deletedtabs)
        print("HERE")
        if (deletedtabs and deletedtabs != "undefined"):
            for i in re.split(",",request.POST.get('returndeltab')):
                i = int(i)
                #print(schedulelist[i])
                schedulelist[i] = None
                #print(schedulelist)
            schedulelist = list(filter(None, schedulelist))

    copypasteform = ClassCopyPasteForm(request.POST)
    lockedform = LockedForm(request.POST)
    filterform = FilterForm(request.POST)
    codeform = CodeForm(request.POST)

    listofcourses = listofcoursenames()
    classes = ClassModel.objects.all()

    filterstarttime = datetime.datetime(100,1,1,7,00,00).time() # first 3 are dummy last 3 are hour/min/sec
    filterendtime = datetime.datetime(100,1,1,21,00,00).time() # use >> datetime.datetime(100,1,1,21,30,00) to end at 21:00:00

    if request.method == 'POST':
        filterform = FilterForm(request.POST)
        if (filterform.is_valid()):
            filteredClasses = classes.filter(start__gte=filterform.cleaned_data['filter_start']) & classes.filter(end__lte=filterform.cleaned_data['filter_end'])
            filterstarttime = filterform.cleaned_data['filter_start']
            filterendtime = filterform.cleaned_data['filter_end']
        if 'generate' in request.POST:
            currentlock = (request.POST.get('returnlock'))
            if (currentlock):
                currentlock = re.split(',', currentlock)
                for x in currentlock:
                    thislock = re.split(' ', x)
                    thiscode = thislock[2:4]
                    thiscode = (' '.join(thiscode))
                    thissection = thislock[4]
                    for x in ClassModel.objects.all():
                        if (x.code.name == thiscode):
                            if (x.section == thissection):
                                x.islocked = True
                                x.save()
            currentunlock = (request.POST.get('returnunlock'))
            if (currentunlock):
                currentunlock = re.split(',', currentunlock)
                for x in currentunlock:
                    thisunlock = re.split(' ', x)
                    thiscode = thisunlock[2:4]
                    thiscode = (' '.join(thiscode))
                    thissection = thisunlock[4]
                    for x in ClassModel.objects.all():
                        if (x.code.name == thiscode):
                            if (x.section == thissection):
                                x.islocked = False
                                x.save()
    finallist = schedulelistmaker(filterstarttime, filterendtime)
    listwithcolor = assignColor(finallist)

    #change this number to get different iterations
    if (len(listwithcolor)==0):
        finalsched = []
    else:
        finalsched = listwithcolor[random.randint(0,len(listwithcolor)-1)]

    #timelist = settingtime(filterstarttime, filterendtime)
    timelist = settingtime()
    mondaylist = monday(finalsched)
    tuesdaylist = tuesday(finalsched)
    wednesdaylist = wednesday(finalsched)
    thursdaylist = thursday(finalsched)
    fridaylist = friday(finalsched)
    saturdaylist = saturday(finalsched)

    completeml = []
    completetl = []
    completewl = []
    completethl = []
    completefl = []
    completesatl = []
    for sched in listwithcolor:
        completeml.append(monday(sched))
        completetl.append(tuesday(sched))
        completewl.append(wednesday(sched))
        completethl.append(thursday(sched))
        completefl.append(friday(sched))
        completesatl.append(saturday(sched))

    zipped = zip(completeml, completetl, completewl, completethl, completefl, completesatl)

    try:
        userClassInput = copypasteform.cleaned_data.get('copypaste')
    except:
        userClassInput = "userClassInput"

    if (num == 1):
        copypaste = None
        currentlock = []

    num = num + 1

    if request.method == 'POST':
    # Checking if the inputs are valid
        if 'indexsubmit' in request.POST:
            codeform = CodeForm(request.POST)
            if codeform.is_valid():
                text = request.POST.get('name')
                newCode = ClassCode(name=text)
                print (newCode)
                # Check if the code being input is already in the system
                if (newCode.name not in listofcourses):
                    newCode.save()
                    print ("its not in")
                    newClass = ClassModel(code=newCode, section=request.POST.get('section'), sched=request.POST.get('sched'), start=request.POST.get('start'), end=request.POST.get('end'), venue=request.POST.get('venue'), professor=request.POST.get('professor'))
                # If not set the course code to the pre-existing code
                else:
                    for course in ClassCode.objects.all():
                        if (course.name == newCode.name):
                            newClass = ClassModel(code=course, section=request.POST.get('section'), sched=request.POST.get('sched'), start=request.POST.get('start'), end=request.POST.get('end'), venue=request.POST.get('venue'), professor=request.POST.get('professor'))
                # Set class information
                newClass.save()
                return redirect("home_page")
        elif 'copypastesubmit' in request.POST:
            copypaste = request.POST.get('copypaste')
            copypasteform = ClassCopyPasteForm(request.POST or None)
            print (copypaste)
            if copypasteform.is_valid():
                ClassCode.objects.all().delete()
                listofcourses.clear()
                #https://stackoverflow.com/questions/12518517/request-post-getsth-vs-request-poststh-difference
                userClassInput = copypasteform.cleaned_data.get('copypaste')
                bigText = re.split('\t', userClassInput)
                for i in range(0, len(bigText), 14): #every 14 indexes
                    oneClass = bigText[i:i + 14]
                    splitClass = re.split('\r\n', oneClass[13])
                    oneClass = oneClass[0:13] + splitClass
                    oneClass = oneClass[0:14] #actual 14
                    text = ('\t'.join(oneClass)) #put together
                    fieldlist = split(text)

                    newCode = ClassCode(name=fieldlist[0])

                    if (newCode.name not in listofcourses):
                        newCode.save()
                        listofcourses.append(newCode.name)
                        #newClass = ClassModel(code=newCode, section=fieldlist[1], sched=fieldlist[2], start=fieldlist[3], end=fieldlist[4], venue=fieldlist[5], professor=fieldlist[6], copypaste=text, islocked=False)
                        if ("#" in oneClass[13]):
                            newClass = ClassModel(code=newCode, section=fieldlist[1], sched=fieldlist[2], start=fieldlist[3], end=fieldlist[4], venue=fieldlist[5], professor=fieldlist[6], copypaste=text, islocked=True)
                        else:
                            newClass = ClassModel(code=newCode, section=fieldlist[1], sched=fieldlist[2], start=fieldlist[3], end=fieldlist[4], venue=fieldlist[5], professor=fieldlist[6], copypaste=text, islocked=False)
                        newClass.save()
                    else:
                        for course in ClassCode.objects.all():
                            if (course.name == newCode.name):
                                #newClass = ClassModel(code=course, section=fieldlist[1], sched=fieldlist[2], start=fieldlist[3], end=fieldlist[4], venue=fieldlist[5], professor=fieldlist[6], copypaste=text, islocked=False)
                                if ("#" in oneClass[13]):
                                    newClass = ClassModel(code=course, section=fieldlist[1], sched=fieldlist[2], start=fieldlist[3], end=fieldlist[4], venue=fieldlist[5], professor=fieldlist[6], copypaste=text, islocked=True)
                                else:
                                    newClass = ClassModel(code=course, section=fieldlist[1], sched=fieldlist[2], start=fieldlist[3], end=fieldlist[4], venue=fieldlist[5], professor=fieldlist[6], copypaste=text, islocked=False)

                        newClass.save() 
                    bigText = bigText[0:i+13] + splitClass + bigText[i+14:] #fixes the og list
                return redirect("home_page")
        elif 'pin' in request.POST:
            templist = []
            for x in re.split(",",request.POST.get('returnsched')):
                for y in classes:
                    if (str(x[13:-1]) == str(y)):
                        templist.append(y)
            schedulelist.append(templist)
            schedulelist = assignColor(schedulelist)
        elif 'unpin' in request.POST:
            schedulelist = []
                
    else:
        codeform = CodeForm()
        copypasteform = ClassCopyPasteForm()
        lockedform = LockedForm()
        filterform = FilterForm()

    return render(request, 'index.html', 
        {
            'copypasteform': copypasteform,
            'lockedform' : lockedform,
            'codeform' : codeform,
            'classinfo': classes, 
            'time': timelist,
            'monday': mondaylist,
            'tuesday': tuesdaylist,
            'wednesday': wednesdaylist,
            'thursday': thursdaylist,
            'friday': fridaylist,
            'saturday': saturdaylist,
            'num': num,
            'filterform':filterform,
            'copypaste': copypaste,
            'finalsched': finalsched,
            'schedulelist': schedulelist,
            'starttime': filterstarttime,
            'endtime': filterendtime,
        }
    )

#sources:
#https://docs.djangoproject.com/en/4.0/topics/db/queries/
# copy and paste function, rename day of week to corresponding day, then put in def index_card_view, and add it into return

def timeConvert(text):
    return text[:2] + ':' + text[2:4]

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

def monday(classlist):
    mondays = []
    for classes in classlist:
        if "M" in classes.sched:
            mondays.append(classes)
    return mondays

def tuesday(classlist):
    tuesdays = []
    for classes in classlist:
        if "T-" in classes.sched or classes.sched == "T":
            tuesdays.append(classes)
    return tuesdays

def wednesday(classlist):
    wednesdays = []
    for classes in classlist:
        if "W" in classes.sched:
            wednesdays.append(classes)
    return wednesdays

def thursday(classlist):
    thursdays = []
    for classes in classlist:
        if "TH" in classes.sched:
            thursdays.append(classes)
    return thursdays

def friday(classlist):
    fridays = []
    for classes in classlist:
        if "F" in classes.sched:
            fridays.append(classes)
    return fridays

def saturday(classlist):
    saturdays = []
    for classes in classlist:
        if "SAT" in classes.sched:
            saturdays.append(classes)
    return saturdays

def listofcoursenames():
    namelist = []
    for course in ClassCode.objects.all():
        namelist.append(course.name)
    return namelist

def settingtime():
    starttime = datetime.datetime(100,1,1,7,00,00) # first 3 are dummy last 3 are hour/min/sec
    #starttime = starttime.replace(hour = st.hour, minute = st.minute)
    endtime = datetime.datetime(100,1,1,21,30,00)
    #endtime = endtime.replace(hour = et.hour, minute = et.minute)
    timelist = []

    while (starttime < endtime):
        timelist.append(starttime.time)
        starttime += datetime.timedelta(0,30*60) # days, seconds, then other fields.
    return timelist

def lockedlistmaker():
    lockedlist = []
    for classes in ClassModel.objects.filter(islocked=True):
        lockedlist.append(classes)
    return lockedlist

# takes st - starting time and et - end time input by the user
# makes finallist of schedules that fit within filters
def schedulelistmaker(st, et):
    classesbycourse = []
    finallist = []
    allclasses = ClassModel.objects.all()
    courselist = ClassCode.objects.all()
    lockedlist = lockedlistmaker()

    # makes an array with each element being a list containing classes for each class code 
    # i.e classesbycourse[0] is all CSCI 40, classesbycourse[1] is all SocSci 12
    for course in courselist:
        templist = []
        for classes in ClassModel.objects.filter(code=course):
            templist.append(classes)
        classesbycourse.append(templist)
            
    # uses itertools to multiply each element of classesbycourse to each other
    # this makes an array with each element have no overlapping class codes
    possibleschedules = (list(itertools.product(*classesbycourse)))

    # each layer is a parameter to filter specific schedules into finallist
    if (possibleschedules):
        for schedule in possibleschedules:
            tempst = st
            tempet = et
            for classes in schedule:
                if (classes.start < tempst):
                    tempst = classes.start
                if (classes.end > tempet):
                    tempet = classes.end
            if (lockedlist):
                if not (checkconflict(schedule)) and tempst >= st and tempet <= et:
                    if all(item in schedule for item in lockedlist):
                        finallist.append(schedule)
            else:
                if not (checkconflict(schedule)) and tempst >= st and tempet <= et:
                    finallist.append(schedule)
    return finallist

# checks two different classes to see if there are schedule conflicts i.e same time and same day
def checkconflict(pair):
    for class1, class2 in itertools.combinations(pair, 2):
        if ((checksched(class1,class2)) and (checktime(class1,class2))):
            return True
    return False

# checks two different classes to see if there are conflicts regarding day
def checksched(class1, class2):
    if ("M"   in class1.sched and "M"   in class2.sched or
        "T-"   in class1.sched and "T-"   in class2.sched or
        "W"   in class1.sched and "W"   in class2.sched or
        "TH"  in class1.sched and "TH"  in class2.sched or
        "F"   in class1.sched and "F"   in class2.sched or
        "SAT" in class1.sched and "SAT" in class2.sched):
        return True  
    else:
        return False

# checks two different classes to see if there are conflicts regarding time
def checktime(class1, class2):
    if (class1.start <= class2.start < class1.end) or (class1.start < class2.end <= class1.end):
        return True
    return False

#sources:
#Time - https://stackoverflow.com/questions/100210/what-is-the-standard-way-to-add-n-seconds-to-datetime-time-in-python

class L(list):
    def __new__(self, *args, **kwargs):
        return super(L, self).__new__(self, args, kwargs)

    def __init__(self, *args, **kwargs):
        if len(args) == 1 and hasattr(args[0], '__iter__'):
            list.__init__(self, args[0])
        else:
            list.__init__(self, args)
        self.__dict__.update(kwargs)

    def __call__(self, **kwargs):
        self.__dict__.update(kwargs)
        return self