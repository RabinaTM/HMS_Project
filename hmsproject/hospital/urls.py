from django.urls import path, include
from . import views


urlpatterns = [
    path('',views.index,name="home"),
    path('about/',views.about,name="about"),
    path('admin_login/',views.Login,name="login"),
    path('logout/',views.logout_admin,name="logout"),
    path('view_doctor/',views.view_doctor,name='view_doctor'),
    path('add_doctor/',views.add_doctor,name='add_doctor'),
    path('delete_doctor/<int:pid>/', views.delete_doctor, name='delete_doctor'),
    path('view_patient/',views.view_patient,name='view_patient'),
    path('add_patient/',views.add_patient,name='add_patient'),
    path('delete_patient/<int:pid>/', views.delete_patient, name='delete_patient'),
    path('view_appointment/',views.view_appointment,name='view_appointment'),
    path('add_appointment/',views.add_appointment,name='add_appointment'),
    path('delete_appointment^<int:pid>/', views.delete_appointment, name='delete_appointment'),

    
    path('booking/',views.booking,name='booking'),
    path('doctors/',views.doctors,name='doctors'),
    path('contact/',views.contact,name='contact'),
    path('department/',views.department,name='department'),

    
]
