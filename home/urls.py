from django.contrib import admin
from django.urls import path,include
from . import views

urlpatterns = [
    
   path('', views.home, name='home'),
   path('news', views.news, name='news'),
   path('about', views.about, name='about'),
   path('contact_us', views.contact_us, name='contact'),
   path('blogs', views.blogs, name="blogs"),
   path('search', views.search, name="search"),
   path('signup',views.handlesignup,name="handlesignup"),
   path('login',views.handlelogin,name="handlelogin"),
   path('logout',views.handlelogout,name="handlelogout"),
   path('signuppage',views.signuppage,name="signuppage"),
   path('loginpage',views.loginpage,name="loginpage"),

]
