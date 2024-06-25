
from django.urls import path
from .views import *
# from .import views

urlpatterns = [
    path("set/",set,name="set"),
    path("get/",get,name="get"),
    path("delete/",delete,name="delete"),
    
    
    # next dea project
    
    
    
    # path("",home,name='home'),
    # path("",about,name='home'),
    # path("",conteact,name='home'),
    # path("",login,name='home'),
]