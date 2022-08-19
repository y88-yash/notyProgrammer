from django.db import models

# Create your models here.
class contact(models.Model):
    idno = models.AutoField(primary_key=True)
    name = models.CharField(max_length=25)
    email = models.CharField(max_length=20)
    content = models.TextField()
    timestamp = models.DateTimeField(auto_now_add=True,blank=True)
    
    def __str__(self):

        return 'message from ' + self.name


