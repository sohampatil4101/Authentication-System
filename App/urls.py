from django.urls import path
from App import views
from django.conf import settings
from django.conf.urls.static import static


urlpatterns = [
    path('',views.home, name="home" ),
    path('register_doctor',views.register_doctor, name="register_doctor" ),
    path('register_patient',views.register_patient, name="register_patient" ),
    path('login',views.login, name="login" ),
    path('logged_patient',views.logged_patient, name="logged_patient" ),
    path('logged_doctor',views.logged_doctor, name="logged_doctor" ),
    path('createblog',views.createblog, name="createblog" ),
    path('deleteblog/<str:obj1>/<str:obj2>/<str:obj3>',views.deleteblog, name="deleteblog" ),
    path('deletedraft/<str:obj1>/<str:obj2>/<str:obj3>',views.deletedraft, name="deletedraft" ),
    path('draftblog',views.draftblog, name="draftblog" ),
    path('checkblog',views.checkblog, name="checkblog" ),
    path('checkblog_patient',views.checkblog_patient, name="checkblog_patient" ),
    path('mental_health',views.mental_health, name="mental_health" ),
    path('heart_dieases',views.heart_dieases, name="heart_dieases" ),
    path('covid_19',views.covid_19, name="covid_19" ),
    path('immunization',views.immunization, name="immunization" ),
    path('view/<str:obj1>/<str:obj2>/<str:obj3>',views.view, name="view" ),
    path('edit/<str:obj1>/<str:obj2>/<str:obj3>',views.edit, name="edit" ),
    path('draftview',views.draftview, name="draftview" ),
    path('mental_health_patient',views.mental_health_patient, name="mental_health_patient" ),
    path('heart_dieases_patient',views.heart_dieases_patient, name="heart_dieases_patient" ),
    path('covid_19_patient',views.covid_19_patient, name="covid_19_patient" ),
    path('immunization_patient',views.immunization_patient, name="immunization_patient" ),
    path('bookappoinment',views.bookappoinment, name="bookappoinment" ),
    path('checkappoinment',views.checkappoinment, name="checkappoinment" ),
    path('checkappoinment_doctor',views.checkappoinment_doctor, name="checkappoinment_doctor" ),
    path('bookappoinment_patient/<str:obj1>',views.bookappoinment_patient, name="bookappoinment_patient" ),
    path('cancelappoinment_patient/<str:obj1>/<str:obj2>',views.cancelappoinment_patient, name="cancelappoinment_patient" ),
    path('cancelappoinment_doctor/<str:obj1>/<str:obj2>',views.cancelappoinment_doctor, name="cancelappoinment_doctor" ),
    path('book/<str:obj1>',views.book, name="book" ),
    path('search/',views.search, name="search" )
]

if settings.DEBUG :
    urlpatterns = urlpatterns + static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)

