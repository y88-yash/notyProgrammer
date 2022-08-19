from django.db import models

# For slug
from .utils import unique_slug_generator    
from django.utils.timezone import now
from django.db.models.signals import pre_save
from django.contrib.auth.models import User

# Create your models here.

       
class Post(models.Model):
    Sno=models.AutoField(primary_key=True)
    title=models.CharField(max_length=255)
    content=models.TextField()
    author=models.CharField(max_length=13)
    slug=models.CharField(max_length=130)
    timestamp=models.DateTimeField(auto_now_add=True,blank=True)
    img = models.ImageField( upload_to="blogImg",default="blogImg/2.jpg")
    
   
    class Meta:
       ordering = ['-timestamp']     
    
    def __str__(self):
        return self.title + ' by ' + self.author

    def slug_generator(sender, instance, *args, **kwargs):
        if not instance.slug:
            instance.slug = unique_slug_generator(instance)
            pre_save.connect(slug_generator, sender = Post)

   



class BlogComment(models.Model):
    Sno = models.AutoField(primary_key=True)
    comment = models.TextField()
    user = models.ForeignKey(User,on_delete=models.CASCADE)
    post = models.ForeignKey(Post,on_delete=models.CASCADE)
    parent = models.ForeignKey('self',on_delete=models.CASCADE,null=True)
    timestamp = models.DateTimeField(default=now)
    def __str__(self):
        return self.comment[0:13] + "..." + "by " + self.user.username
    
