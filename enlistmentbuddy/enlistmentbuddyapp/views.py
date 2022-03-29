from ast import Index
from tabnanny import check
from django.shortcuts import render, redirect
import re

from django.http import HttpResponse

#forms
from .forms import IndexCardForm
from .forms import CopyPasteForm
from .forms import ClassCopyPasteForm
from .forms import CourseForm, CodeForm

from .models import IndexCard, ClassModel, ClassCode

from django.views import View
from django.views.generic.list import ListView
from django.views.generic.edit import DeleteView
from django.views.generic.detail import DetailView

import datetime

#insert functions here
def index(request):
    return redirect('index_card')


def index_card_view(request):
    indexcardform = CourseForm(request.POST)
    copypasteform = ClassCopyPasteForm(request.POST)
    classes = ClassModel.objects.all()
    thislist = setting_time()
    mondaylist = monday()
    tuesdaylist = tuesday()
    wednesdaylist = wednesday()
    thursdaylist = thursday()
    fridaylist = friday()
    saturdaylist = saturday()
    codeform = CodeForm(request.POST)
    courselist = coursecodes()
    # thiscourse = courselist[1]
    #testlist = sortClasses()
    listofcourses = []
    for course in ClassCode.objects.all():
        listofcourses.append(course.name)

    #elpme = imtesting()
    #over here peeps

    if request.method == 'POST':
    # Checking if the inputs are valid
        if 'indexsubmit' in request.POST:
            indexcardform = CourseForm(request.POST)
            codeform = CodeForm(request.POST)
            if codeform.is_valid():
                text = request.POST.get('name')
                newCode = ClassCode(name=text)
                
                if (newCode.name not in listofcourses):
                    newCode.save()
                    print ("its not in")
                    newClass = ClassModel(code=newCode, section=request.POST.get('section'), sched=request.POST.get('sched'), start=request.POST.get('start'), end=request.POST.get('end'), venue=request.POST.get('venue'), professor=request.POST.get('professor'))
                else:
                    for course in ClassCode.objects.all():
                        if (course.name == newCode.name):
                            newClass = ClassModel(code=course, section=request.POST.get('section'), sched=request.POST.get('sched'), start=request.POST.get('start'), end=request.POST.get('end'), venue=request.POST.get('venue'), professor=request.POST.get('professor'))
                        
                newClass.save()
                return redirect("index_card")
        elif 'copypastesubmit' in request.POST:
            copypasteform = ClassCopyPasteForm(request.POST)
            if copypasteform.is_valid():
                #copypasteform.save()
                #https://stackoverflow.com/questions/12518517/request-post-getsth-vs-request-poststh-difference
                #text = request.POST.get('copypaste')
                userClassInput = request.POST.get('copypaste')
                #print(text)
                bigText = re.split('\t', userClassInput)
                #print(bigText)
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
                        newClass = ClassModel(code=newCode, section=fieldlist[1], sched=fieldlist[2], start=fieldlist[3], end=fieldlist[4], venue=fieldlist[5], professor=fieldlist[6], copypaste=text)
                    else:
                        for course in ClassCode.objects.all():
                            if (course.name == newCode.name):
                                newClass = ClassModel(code=course, section=fieldlist[1], sched=fieldlist[2], start=fieldlist[3], end=fieldlist[4], venue=fieldlist[5], professor=fieldlist[6], copypaste=text)
                    newClass.save()
                    bigText = bigText[0:i+13] + splitClass + bigText[i+14:] #fixes the list
                return redirect("index_card")
    else:
        indexcardform = CourseForm()
        codeform = CodeForm()
        copypasteform = ClassCopyPasteForm()

    return render(request, 'index.html', 
        {
            'indexcardform': indexcardform, 
            'copypasteform': copypasteform,
            'codeform' : codeform,
            'class_info': classes, 
            'time': thislist,
            'monday': mondaylist,
            'tuesday': tuesdaylist,
            'wednesday': wednesdaylist,
            'thursday': thursdaylist,
            'friday': fridaylist,
            'saturday': saturdaylist,
            #'testlister':testlist,
            'courses': courselist,
            # 'trycourse': thiscourse,
            #over here peeps
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

def monday():
    mondays = []
    for mondayclass in ClassModel.objects.filter(sched__contains='M'):
        mondays.append(mondayclass)
    return mondays

def tuesday():
    tuesdays = []
    tueslist = ClassModel.objects.filter(sched__contains='T-') |  ClassModel.objects.filter(sched__iexact='T')
    for tuesdayclass in tueslist:
        tuesdays.append(tuesdayclass)
    return tuesdays

def wednesday():
    wednesdays = []
    for wednesdayclass in ClassModel.objects.filter(sched__contains='W'):
        wednesdays.append(wednesdayclass)
    return wednesdays

def thursday():
    thursdays = []
    for thursdayclass in ClassModel.objects.filter(sched__contains='TH'):
        thursdays.append(thursdayclass)
    return thursdays

def friday():
    fridays = []
    for fridayclass in ClassModel.objects.filter(sched__contains='F'):
        fridays.append(fridayclass)
    return fridays

def saturday():
    saturdays = []
    for saturdayclass in ClassModel.objects.filter(sched__contains='SAT'):
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
    for course in ClassModel.objects.all():
        if course.code not in courselist:
            courselist.append(course.code)
    return courselist

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

def imtesting():
    baseclasslist = []
    classesbycourse = []
    courselist = coursecodes()
    tempclasses = []

    for course in courselist:
        tempclasses = []
        #print (course)
        tempclasses.append(course)
        tempclasses.append(ClassModel.objects.filter(code__contains=course))
        #print(tempclasses)
        classesbycourse.append(tempclasses)
    
    #print (len(classesbycourse))
    for x in range(0,len(classesbycourse)):
        print (classesbycourse[x][0])
        for y in range(0,len(classesbycourse[x][1])):
            print (classesbycourse[x][1][y])
    #for course in classesbycourse:
    #    print (course[0])
    #    for classes in course[1]:
    #        print (classes)

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

#def sortClasses():
#    classlist = []
#    classoccupy = []
#
#    while(len(classoccupy) != ClassCode.objects.all().count()):
#        for classes in ClassModel.objects.all():
#            if (classtester(classoccupy,classes)):
#                print("pakyu")
#                if (scheduleoverlap(classes.sched,classoccupy) and checkoverlap(classes,classlist)):
#                    print("pakshet")
#                    classlist.append(classes)
#                    classoccupy.append(classes.code)
#                    print(len(classoccupy))
#                    print(ClassCode.objects.all().count())
#                        break
#                    sortClasses()
#                    
#                    classlist.pop()
#                    classoccupy.pop()
#                
#        return classlist
#    return classlist

                    
    
    #classlist = []
    #classoccupy = []
#
    #for course in ClassModel.objects.all():
    #    for x in classlist:
    #        if (checkoccupied(classoccupy,course.code) or (checkoverlap(x.start,x.end,course.start,course.end) and scheduleoverlap(x.sched,course.sched))):
    #            break
    #        elif (classlist.index(x)==len(classlist)-1):
    #            classoccupy.append(course.code)
    #            classlist.append(course)
    #    if len(classoccupy) == 0:
    #        classoccupy.append(course.code)
    #        classlist.append(course)
    #return classlist
        



#sources:
#Time - https://stackoverflow.com/questions/100210/what-is-the-standard-way-to-add-n-seconds-to-datetime-time-in-python