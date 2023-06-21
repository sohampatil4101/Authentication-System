from django.shortcuts import render, redirect
from App.models import *
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