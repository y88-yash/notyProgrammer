from django.shortcuts import render,HttpResponse,redirect
from blog.models import Post,BlogComment
from django.http import HttpResponseRedirect
from django.shortcuts import get_object_or_404
from django.contrib import messages
import datetime
from django.urls import reverse
from .forms import *
from blog.templatetags import extras

# Create your views here.

def bloghome(request):
    allpost = Post.objects.all()
  #  allpost = Post.objects.filter(testfield=12).order_by('-id')[0]
    context = {'allpost':allpost}
    #obj= Model.objects.filter(testfield=12).order_by('-id')[0]
    return render(request,"home/home.html",context)

def blogpost(request,slug):
    post=Post.objects.filter(slug=slug).first()
    comments = BlogComment.objects.filter(post=post,parent=None)
    replies = BlogComment.objects.filter(post=post).exclude(parent=None)
   
    replyDict = {}
    for reply in replies:
        if reply.parent.Sno not in replyDict.keys():
            replyDict[reply.parent.Sno]=[reply]
        else:
            replyDict[reply.parent.Sno].append(reply)
            
    context={'post':post,'comments':comments,'user':request.user,'replyDict':replyDict}

    return render(request,"blogtemp/blogpost.html",context)

def createposts(request):
    if request.method=='POST':
        form = PostForm(request.POST, request.FILES) 
        if form.is_valid(): 

            post=form.save(commit=False)
            post.author = request.user
            post.save()
            messages.success(request,"Post Created")
            return redirect('createposts') 
    else: 
        form = PostForm() 
    return render(request,"blogtemp/createpost.html",{'form' : form})


def postComment(request):
    if request.method=='POST':
         
        comment = request.POST.get("comment")
        user = request.user
        postSno =  request.POST.get("postSno")
        post = Post.objects.get(Sno=postSno)
        ParentSno =request.POST.get("ParentSno")
        if ParentSno == "":
            comment = BlogComment(comment=comment,user=user,post=post)
            comment.save()
            messages.success(request,"Your comment has been posted successfully!")
        else:
            parent=BlogComment.objects.get(Sno=ParentSno)
            comment = BlogComment(comment=comment,user=user,post=post,parent=parent)
            comment.save()
            messages.success(request,"Your reply has been posted successfully!")
    return redirect(f"/blog/{post.slug}")


