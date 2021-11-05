from django.urls import path
from .import views
from .forms import*



app_name="newbiz"



urlpatterns = [
     
    path("hi", views.home, name="home"),
    path("", views.index, name="index"),
    
    
    
    
    
    
    
 

]
