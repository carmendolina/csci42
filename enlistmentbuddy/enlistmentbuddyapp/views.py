from calendar import c
# from math import comb
import random
from ast import Index
from tabnanny import check
from django.shortcuts import render, redirect
import re, itertools

from django.http import HttpResponse

#forms
from .forms import IndexCardForm
from .forms import CopyPasteForm
from .forms import ClassCopyPasteForm
from .forms import LockedForm
from .forms import CourseForm, CodeForm

from .models import IndexCard, ClassModel, ClassCode

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

#insert functions here
def index(request):
    return redirect('index_card')

def assignColor(list):
    for thing in list:
        i = 0
        L(thing)
        for course in thing:
            course.color = colorList[i]
            start_sec= (course.start.hour*60+course.start.minute)*60+course.start.second
            end_sec= (course.end.hour*60+course.end.minute)*60+course.end.second
            course.duration = int(((end_sec-start_sec)/60.0)/30)
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
        
def index_card_view(request):

    global num
    global copypaste
    global currentlock

    global schedulelist

    indexcardform = CourseForm(request.POST)
    copypasteform = ClassCopyPasteForm(request.POST)
    lockedform = LockedForm(request.POST)
    classes = ClassModel.objects.all()
    finallist = imtesting()
    listwithcolor = assignColor(finallist)
        
    #for code in ClassCode.objects.all():
        # (code.pk)

    #print (finallist[0])

    #change this number to get different iterations
    if (len(listwithcolor)==0):
        finalsched = []
    else:
        finalsched = listwithcolor[random.randint(0,len(listwithcolor)-1)]

    #finalsched = []

    if (finalsched):
        starttime = finalsched[0].start # first 3 are dummy last 3 are hour/min/sec
        endtime = finalsched[0].end
    else:
        starttime = datetime.datetime(100,1,1,7,00,00).time() # first 3 are dummy last 3 are hour/min/sec
        endtime = datetime.datetime(100,1,1,21,00,00).time() # use >> datetime.datetime(100,1,1,21,30,00) to end at 21:00:00
    #print (finalsched[0].start)
    #print (finalsched[0].end)
    #print ("---")
    for x in finalsched:
        #print (x)
        #print ("---")
        #print (x.start)
        #print ("---")
        #print (x.end)
        if (x.start < starttime):
            starttime = x.start
        if (x.end > endtime):
            endtime = x.end
        #print (x)
        #print (x.start)
        # (x.end)
    #print ("final")
    #print (starttime)
    #print (endtime)
    thislist = setting_time()

    # print(finalsched)
    # for each in finalsched:
    #     print(each)
    #     print(each.duration)
      
    mondaylist = monday(finalsched)
    tuesdaylist = tuesday(finalsched)
    wednesdaylist = wednesday(finalsched)
    thursdaylist = thursday(finalsched)
    fridaylist = friday(finalsched)
    saturdaylist = saturday(finalsched)
    codeform = CodeForm(request.POST)
    listofcourses = listofcoursenames()

    try:
        userClassInput = copypasteform.cleaned_data.get('copypaste')
    except:
        userClassInput = "userClassInput"

    # print(mondaylist)
    # for each in mondaylist:
    #     print(each.color)

    #CHECKING COURSES
    #for course in listofcourses:
    #    print (course)
    #print ("---")

    #CHECKING CLASSES
    #for x in classes:
    #    print (x)
    #print ("---")

    if (num == 1):
        copypaste = None
        currentlock = []

    increment()

    if request.method == 'POST':
    # Checking if the inputs are valid
        if 'indexsubmit' in request.POST:
            indexcardform = CourseForm(request.POST)
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
                return redirect("index_card")
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
                return redirect("index_card")
        elif 'generate' in request.POST:
            schedulelist = [] #for testing purposes dont mind me
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
            finallist = imtesting()
            listwithcolor = assignColor(finallist)
        elif 'pin' in request.POST:
            print("----")
            schedulelist.append(re.split(",",request.POST.get('returnsched')))
            for schedule in schedulelist:
                print(schedule)
            print("----")
                
    else:
        indexcardform = CourseForm()
        codeform = CodeForm()
        copypasteform = ClassCopyPasteForm()
        lockedform = LockedForm()

    return render(request, 'index.html', 
        {
            'indexcardform': indexcardform, 
            'copypasteform': copypasteform,
            'lockedform' : lockedform,
            'codeform' : codeform,
            'class_info': classes, 
            'time': thislist,
            'monday': mondaylist,
            'tuesday': tuesdaylist,
            'wednesday': wednesdaylist,
            'thursday': thursdaylist,
            'friday': fridaylist,
            'saturday': saturdaylist,
            'num': num,
            'copypaste': copypaste,
            'finalsched': finalsched,

            #'testlister':testlist,
            # 'trycourse': thiscourse,
            #over here peeps
        }
    )

#sources:
#https://docs.djangoproject.com/en/4.0/topics/db/queries/
# copy and paste function, rename day of week to corresponding day, then put in def index_card_view, and add it into return

def anotherfoo(request):
   num = request.session.get('num') + 1
   return num
   # and so on, and so on

def increment():
    global num
    num = 2

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

def setting_time():
    starttime = datetime.datetime(100,1,1,7,00,00) # first 3 are dummy last 3 are hour/min/sec
    endtime = datetime.datetime(100,1,1,21,30,00)
    timelist = []

    #print (starttime)
    #print (datetime.timedelta(0,30*60))

    while (starttime < endtime):
        timelist.append(starttime.time)
        starttime += datetime.timedelta(0,30*60) # days, seconds, then other fields.
    return timelist

def checkoccupied(list, code):
    for course in list:
        if (course == code):
            return True
    return False

def checkoverlap(classes, list2):
    for x in list2:
        if (x.start<classes.start<x.end) or (x.start<classes.end<x.end) or (x.start==classes.start):
            return False
    return True

def listofcoursenames():
    namelist = []
    for course in ClassCode.objects.all():
        namelist.append(course.name)
    return namelist

def classtester(occupiedclasses, className):
    for occupied in occupiedclasses:
        if (occupiedclasses == className.code):
            return False
    return True

def scheduleoverlap(classes,ydays):
    for x in ydays:
        if ("SAT" in classes and "SAT" in x.sched):
            return False
        elif ("TH" in classes and "TH" in ydays.sched):
            return False
        elif ("T" in classes and "T" in ydays.sched):
            return False
        elif ("M" in classes and "M" in ydays.sched):
            return False
        elif ("W" in classes and "W" in ydays.sched):
            return False
        elif ("F" in classes and "F" in ydays.sched):
            return False  
    return True

def lockedlistmaker():
    lockedlist = []
    for classes in ClassModel.objects.filter(islocked=True):
        lockedlist.append(classes)
    return lockedlist

# <-- Raffys stuff
def imtesting():
    classesbycourse = []
    finallist = []
    allclasses = ClassModel.objects.all()
    courselist = ClassCode.objects.all()
    lockedlist = []

    #print (courselist)
    for course in courselist:
        templist = []
        for classes in ClassModel.objects.filter(code=course):
            templist.append(classes)
        classesbycourse.append(templist)
    #print (classesbycourse)
    #for thingo in classesbycourse:
        #print (thingo)
            
    possiblecombos = (list(itertools.product(*classesbycourse)))

    for thingo in possiblecombos:
        #print (thingo)
        #print ("------------")
        if not (checkconflict(thingo)):
            finallist.append(thingo)
            #print ("added")
        #else:
            #print ("not added")
    #print (finallist)

    finalfinallist = []
    lockedlist = lockedlistmaker()
    print(lockedlist)

    if (lockedlist):
        for x in finallist:
            if all(item in x for item in lockedlist):
                finalfinallist.append(x)
        return finalfinallist
    return (finallist)

def checkconflict(combo):
    for a, b in itertools.combinations(combo, 2):
        #print (a)
        #print (a.start)
        #print (a.end)
        #print (b)
        #print (b.start)
        #print (b.end)
        #print (checksched(a,b))
        #print (checktime(a,b))
        #print ("--")
        if ((checksched(a,b)) and (checktime(a,b))):
            return True
    return False

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

def checktime(class1, class2):
    if (class1.start <= class2.start < class1.end) or (class1.start < class2.end <= class1.end):
        return True
    return False

#Raffy Testing -->

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