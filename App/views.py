from django.shortcuts import render, redirect
from App.models import *
import random
# Create your views here.

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
        print("Soham is great", title, category, content, summary, image)
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
    

