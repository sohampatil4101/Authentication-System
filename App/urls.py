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
]

if settings.DEBUG :
    urlpatterns = urlpatterns + static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)

