from django.shortcuts import render, redirect
from App.models import *
import random



# imports for calendar
import os.path
import datetime as dt
from datetime import datetime, timedelta
from google.auth.transport.requests import Request
from google.oauth2.credentials import Credentials
from google_auth_oauthlib.flow import InstalledAppFlow
from googleapiclient.discovery import build
from googleapiclient.errors import HttpError
SCOPES = ["https://www.googleapis.com/auth/calendar"]


   
def book(request,obj1):
    context = {'success': False}
    if request.method == "POST":
        username = request.session.get('username')
        doctor = obj1
        specialist = request.POST['specialist']
        date = request.POST['date']
        time = request.POST['time']

        start = time
        time_obj = datetime.strptime(start, "%H:%M")
        new_time_obj = time_obj + timedelta(minutes=45)
        end = new_time_obj.strftime("%H:%M")
        
    creds = None

    if os.path.exists("token.json"):
        creds = Credentials.from_authorized_user_file("token.json")
    
    if not creds or not creds.valid:

        if creds and creds.expired and creds.refresh_token:
            creds.refresh(Request())
        
        else:
            flow = InstalledAppFlow.from_client_secrets_file("calendar-api.json", SCOPES)
            creds = flow.run_local_server(port = 0)

        with open("token.json", "w") as token:
            token.write(creds.to_json())
    
    try:
        service = build("calendar", "v3", credentials=creds)
        

        # Event adding
        event = {
            "summary": specialist,
            "loaction": "Somewhere online",
            "description": "Some more details",
            "colorId": 6,
            "start":{
                'dateTime': f"{date}T{start}:00+05:30",
                'timeZone': 'Asia/Kolkata',
                    },
            "end":{
                'dateTime': f"{date}T{end}:00+05:30",
                'timeZone': 'Asia/Kolkata',
                     },
            "recurrence":[
                # "RRULE:FREQ=DAILY;COUNT=3"
                "EXDATE;VALUE=DATE:20230630,20230701"
            ],
            "attendees":[
                {"email": "soham@123gmail.com"},
                {"email": "samu@123gmail.com"}
            ]
        }


        event = service.events().insert(calendarId = "primary", body = event).execute()
        print(f"Event created  {event.get('htmlLink')}")
        
        
    except HttpError as error:
        print("Error is ", error)


    ins = Appoinment.objects.create(username = username, doctor = doctor, specialist = specialist, date = date, time = time)
    ins.save()
    data = Appoinment.objects.filter(username = request.session.get('username'), doctor = doctor, specialist = specialist, date = date, time = time)
    context = {'success': True, 'data': data}
    return render(request, 'confirm.html', context)



def home(request):
    return render(request, 'home.html')

def register_doctor(request):
    context = {'success': False, 'successs':False, 'mssg':""}
    if request.method == "POST":
        username = request.POST['username']
        first_name = request.POST['first_name']
        last_name = request.POST['last_name']
        password1 = request.POST['password1']
        password2 = request.POST['password2']
        address = request.POST['address']
        email = request.POST['email']
        image = request.FILES['image']

        if ( len(username) and len(first_name) and len(last_name) and len(email) and len(password1) and len(password2) ) == 0:
            context={'successs':True,'mssg':"Please enter every field!!"}

        elif  len(username)>= 21:
            context={'successs':True,'mssg':"Please enter username with less than 20 characters!!"}


        elif (password1 != password2):
            context={'successs':True,'mssg':"Both password must be same!!"}

        elif (Doctor.objects.filter(username=username).exists() ):
            context={'successs':True,'mssg':"Username exists!!"}

        elif (Patient.objects.filter(username=username).exists() ):
            context={'successs':True,'mssg':"Username exists!!"}
            
        elif (Doctor.objects.filter(email=email).exists() ):
            context={'successs':True,'mssg':"Email exists!!"}

        elif (Patient.objects.filter(email=email).exists() ):
            context={'successs':True,'mssg':"Email exists!!"}

        else:
            ins = Doctor.objects.create(username = username, first_name = first_name, last_name = last_name, email = email, password = password1, image = image, address = address)
            ins.save()
            context = {'success': True}
            return render(request, 'register_doctor.html', context)


    return render(request, 'register_doctor.html', context)

def register_patient(request):
    
    context = {'success': False, 'successs':False, 'mssg':""}
    if request.method == "POST":
        username = request.POST['username']
        first_name = request.POST['first_name']
        last_name = request.POST['last_name']
        password1 = request.POST['password1']
        password2 = request.POST['password2']
        address = request.POST['address']
        email = request.POST['email']
        image = request.FILES['image']

        if ( len(username) and len(first_name) and len(last_name) and len(email) and len(password1) and len(password2) ) == 0:
            context={'successs':True,'mssg':"Please enter every field!!"}

        elif  len(username)>= 21:
            context={'successs':True,'mssg':"Please enter username with less than 20 characters!!"}


        elif (password1 != password2):
            context={'successs':True,'mssg':"Both password must be same!!"}

        elif (Doctor.objects.filter(username=username).exists() ):
            context={'successs':True,'mssg':"Username exists!!"}

        elif (Patient.objects.filter(username=username).exists() ):
            context={'successs':True,'mssg':"Username exists!!"}
            
        elif (Doctor.objects.filter(email=email).exists() ):
            context={'successs':True,'mssg':"Email exists!!"}

        elif (Patient.objects.filter(email=email).exists() ):
            context={'successs':True,'mssg':"Email exists!!"}

        else:
            ins = Patient.objects.create(username = username, first_name = first_name, last_name = last_name, email = email, password = password1, image = image, address = address)
            ins.save()
            context = {'success': True}
            return render(request, 'register_patient.html', context)

    return render(request, 'register_patient.html', context)


def login(request):
    context = {'success': False, 'successs':False}
    if request.method == "POST":
        username = request.POST['username']
        password = request.POST['password']
        request.session['username'] = username


        if (Doctor.objects.filter(username=username, password = password).exists()):
            data = Doctor.objects.filter(username = request.session.get('username'))
            context = {'username': request.session.get('username'), 'name': username, 'data': data}
            return render(request, 'logged_doctor.html', context)


        elif (Patient.objects.filter(username=username, password = password).exists()):
            data = Patient.objects.filter(username = request.session.get('username'))
            context = {'username': request.session.get('username'), 'name': username, 'data': data}
            return render(request, 'logged_patient.html', context)


        else:
            context= {'successs':True, 'mssg':"Please enter correct username or password!!!"}
            return render(request, 'login.html', context)



    return render(request, 'login.html', context)
    
def logged_patient(request):
    return render(request, 'logged_patient.html')
    
def logged_doctor(request):
    return render(request, 'logged_doctor.html')
    
def draftblog(request):
    context = {'success': False, 'successs': False}
    if request.method == "POST":
        username = request.session.get('username')
        title = request.POST['title']
        category = request.POST['category']
        content = request.POST['content']
        summary = request.POST['summary']
        image = request.FILES['image']
        ins = Draftblog.objects.create(username = username, title = title, category = category, content = content, summary = summary, image = image)
        ins.save()
        context = {'success': False, 'successs': True}
        return render(request, 'createblog.html', context)
    return render(request, 'createblog.html')
    
def createblog(request):
    context = {'success': False}
    if request.method == "POST":
        username = request.session.get('username')
        title = request.POST['title']
        category = request.POST['category']
        content = request.POST['content']
        summary = request.POST['summary']
        image = request.FILES['image']
        ins = Createblog.objects.create(username = username, title = title, category = category, content = content, summary = summary, image = image)
        ins.save()
        context = {'success': True}
        return render(request, 'createblog.html', context)
    return render(request, 'createblog.html')
    
    
def checkblog(request):
    mental_health = random.sample(list(Createblog.objects.filter(username = request.session.get('username'), category = "Mental Health")), 3) 
    heart_dieases = random.sample(list(Createblog.objects.filter(username = request.session.get('username'), category = "Heart Disease")), 3) 
    covid_19 = random.sample(list(Createblog.objects.filter(username = request.session.get('username'), category = "Covid19")), 3) 
    immunization = random.sample(list(Createblog.objects.filter(username = request.session.get('username'), category = "Immunization")), 3) 
    context = {'mental_health' : mental_health, 'heart_dieases' : heart_dieases, 'covid_19' : covid_19, 'immunization' : immunization}
    return render(request, 'checkblog.html', context)
    
    
    
def checkblog_patient(request):
    mental_health = random.sample(list(Createblog.objects.filter(category = "Mental Health")), 3) 
    heart_dieases = random.sample(list(Createblog.objects.filter(category = "Heart Disease")), 3) 
    covid_19 = random.sample(list(Createblog.objects.filter(category = "Covid19")), 3) 
    immunization = random.sample(list(Createblog.objects.filter(category = "Immunization")), 3) 
    context = {'mental_health' : mental_health, 'heart_dieases' : heart_dieases, 'covid_19' : covid_19, 'immunization' : immunization}
    return render(request, 'checkblog_patient.html', context)
    

def mental_health(request):
    context = {'data': Createblog.objects.filter(username = request.session.get('username'), category = "Mental Health")}
    return render(request, 'data.html', context)
    


def heart_dieases(request):
    context = {'data': Createblog.objects.filter(username = request.session.get('username'), category = "Heart Disease")}
    return render(request, 'data.html', context)
    


def covid_19(request):
    context = {'data': Createblog.objects.filter(username = request.session.get('username'), category = "Covid19")}
    return render(request, 'data.html', context)
    


def immunization(request):
    context = {'data': Createblog.objects.filter(username = request.session.get('username'), category = "Immunization")}
    return render(request, 'data.html', context)
    

def view(request, obj1, obj2, obj3):
    context = {'data': Createblog.objects.filter(username = obj1, category = obj2, title = obj3)}
    return render(request, 'view.html', context)
    



def draftview(request):
    context = {'data': Draftblog.objects.filter(username = request.session.get('username'))}
    return render(request, 'draftview.html', context)


def edit(request, obj1, obj2, obj3):
    
    context = {'data': Draftblog.objects.filter(username = request.session.get('username'), category = obj2, title = obj3)}
    return render(request, 'edit.html', context)
    

def mental_health_patient(request):
    context = {'data': Createblog.objects.filter(category = "Mental Health")}
    return render(request, 'data.html', context)
    


def heart_dieases_patient(request):
    context = {'data': Createblog.objects.filter(category = "Heart Disease")}
    return render(request, 'data.html', context)
    


def covid_19_patient(request):
    context = {'data': Createblog.objects.filter(category = "Covid19")}
    return render(request, 'data.html', context)
    


def immunization_patient(request):
    context = {'data': Createblog.objects.filter(category = "Immunization")}
    return render(request, 'data.html', context)
    


def deleteblog(request, obj1, obj2, obj3):
    abc = Createblog.objects.get(username = request.session.get('username'), category = obj2, title = obj3)
    abc.delete()
    return redirect("/checkblog")
    



def deletedraft(request, obj1, obj2, obj3):
    abc = Draftblog.objects.get(username = request.session.get('username'), category = obj2, title = obj3)
    abc.delete()
    return redirect("/draftview")
    

def bookappoinment(request):
    data = Doctor.objects.all()
    context = {'data': data}
    return render(request, 'bookappoinment.html', context)



    
def search(request):
    context = {'nopage': False}
    search = request.GET['search']

    data = Doctor.objects.filter(username__icontains = search)

    if(data):
        data = Doctor.objects.filter(username__icontains = search)
        context = {'data': data, 'nopage': False}
        return render(request, 'search.html', context)

    else:
        context = {'nopage': True, 'error': search}
        return render(request, 'search.html', context)
    

def bookappoinment_patient(request, obj1):
    data = Doctor.objects.filter(username = obj1)
    context = {'data': data}
    return render(request, 'bookappoinment_patient.html', context)
 
def checkappoinment(request):
    data = Appoinment.objects.filter(username = request.session.get('username'))
    context = {'data': data}
    return render(request, 'checkappoinment.html', context)


def checkappoinment_doctor(request):
    data = Appoinment.objects.filter(doctor = request.session.get('username'))
    context = {"data": data}
    return render(request, 'checkappoinment_doctor.html', context)

def cancelappoinment_patient(request, obj1, obj2):
    data = Appoinment.objects.get(username = obj1, specialist = obj2)
    data.delete()
    return redirect("/checkappoinment")

def cancelappoinment_doctor(request, obj1, obj2):
    data = Appoinment.objects.get(username = obj1, specialist = obj2)
    data.delete()
    return redirect("/checkappoinment_doctor")

def chatroom_doctor(request):
    data = Patient.objects.all()
    context = {'data': data}
    return render(request, 'chatroom_doctor.html', context)

def chatroom_patient(request):
    data = Doctor.objects.all()
    context = {'data': data}
    return render(request, 'chatroom_patient.html', context)

def chat_doctor(request, room_name):
    data = Patient.objects.filter(username = room_name)
    context = {"data": data, "room_name": room_name}
    return render(request, 'chat_doctor.html', context)

def chat_patient(request, room_name):
    data = Doctor.objects.filter(username = room_name)
    context = {"data": data, "room_name": room_name}
    return render(request, 'chat_patient.html', context)