from django.contrib import admin
from django.urls import include,path
from . import views


urlpatterns = [
   
    path('postComment',views.postComment,name="postComment"),
    path('', views.bloghome, name='bloghome'),
    path('createposts', views.createposts, name='createposts'),
    path('<str:slug>', views.blogpost, name='blogpost'),
  
    
    
  

]
