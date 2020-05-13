from django.urls import path
from . import views

urlpatterns = [
    #path('', views.home, name='user-home'),
    path('user_profile/', views.user_profile, name='user-profile'),
    
]
