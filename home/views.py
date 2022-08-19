from django.shortcuts import render,HttpResponse,redirect
from home.models import contact
from django.contrib import messages
from blog.models import Post
import requests
from django.db.models import Q
from django.contrib.auth.models import User
import json
from django.contrib.auth import authenticate, login, logout
# Create your views here.
def home(request):
    #return HttpResponse('home')
    allpost = Post.objects.all()
    context = {'allpost':allpost}
    return render(request,'home/home.html',context)

def news(request):
    import requests
    import json
    news_api_request=requests.get("http://newsapi.org/v2/top-headlines?country=in&apiKey=aeb50df0a8ae4b02ba795eeeb817268a")
    api=json.loads(news_api_request.content)
    return render(request,"home/news.html",{'api':api})
   

    

def about(request):
    #return HttpResponse('about')
    return render(request,'home/about.html')

def contact_us(request):
    
    if request.method=='POST':
        name = request.POST['name']
        email = request.POST['email']
        content = request.POST['content']
        print(name,email,content)
        if len(name)<3 or len(email)<8:
            messages.error(request,"Please Fill the Details")
        else:
            c = contact(name=name, email=email ,content=content)
            c.save()
            messages.success(request,"Your Message is submitted")

        
        
            
    return render(request,'home/contact.html')




def blogs(request):
    allpost = Post.objects.all()
    context = {'allpost':allpost}
    return render(request,'home/blogs.html',context)
def search(request):
    
    if request.method == 'GET':
        query= request.GET.get('query')

        submitbutton= request.GET.get('submit')

        if query is not None:
            lookups= Q(title__icontains=query) | Q(content__icontains=query)

            results= Post.objects.filter(lookups).distinct()

            context={'results': results,
                     'submitbutton': submitbutton}

            return render(request, 'home/search.html', context)

        else:
            return render(request, 'home/search.html')
    else:
        return render(request, 'home/search.html')


def handlesignup(request):
    if request.method == 'POST':
        username = request.POST['username']
        fname = request.POST['fname']
        lname = request.POST['lname']
        email = request.POST['email']
        password = request.POST['password']
        #checks
    
        if len(username) > 16:
            messages.error(request,"Username should contain letters and numbers")
            return redirect("home")
        if len(fname) < 3 and len(lname) < 3:
            messages.error(request,"First and Last name should be more than 3 character")
            return redirect("home")
        if len(username) < 4:
            messages.error(request,"Username must contains atleast 5 character")
            return redirect("home")
        if len(password) < 8:
            messages.error("Password Should be more than 8 characters")
            return redirect("home")
        if not username.isalnum():
            messages.error(request,"Username must contain number and characters")
            return redirect("home")

        myuser = User.objects.create_user(username, email, password)
        myuser.first_name = fname
        myuser.last_name = lname
        myuser.save()
        messages.success(request,"Your NotyProgrammer's account is created")
        return redirect('home')
    else:
        return HttpResponse('404- not found')

    

def handlelogin(request):
    if request.method == 'POST':
        loginusername = request.POST['loginusername']
        loginpassword = request.POST['loginpassword']

        user = authenticate(username=loginusername, password=loginpassword)
        if user is not None:
            login(request, user)
            messages.success(request, "successfully logged in")
            return redirect('home')
        else:
            messages.warning(request,"invaild credentials, pls try again")
            return redirect('home')

    return HttpResponse('404- not found')
            

def handlelogout(request):
    logout(request)
    messages.success(request,"successfully logged out")
    return redirect('home')

    return HttpResponse('404- not found')
def signuppage(request):
    return render(request,"home/signup.html")


def loginpage(request):
    return render(request,"home/login.html")