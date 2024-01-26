from django.contrib import admin
from django.urls import path
from . import views

from django.conf.urls.static import static
from django.conf import settings

urlpatterns = [
    path('',views.home,name='home'),
    path('signup/',views.signup,name='signup'),
    path('about/',views.about,name='about'),
    path('login/',views.login,name='login'),
    path('dashboard/',views.dashboard,name='dashboard'),
    path('teams/',views.teams,name='teams'),
    path('transactions/',views.trans,name='transactions'),
    path('create-record/',views.create_record,name='create-record'),
    path('update-record/<int:pk>',views.update_record,name='update-record'),
    path('view-record/<int:pk>',views.view_record,name='view-record'),
    path('delete-record/<int:pk>',views.delete_record,name='delete-record'),
    path('email/',views.email,name='email'),
    
]+static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)
