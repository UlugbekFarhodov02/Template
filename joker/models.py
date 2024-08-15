from django.db import models 
from ckeditor.fields import RichTextField
from hitcount.models import HitCountMixin,HitCount
from django.contrib.contenttypes.fields import GenericRelation


class About(models.Model):
    description = models.TextField()
    image = models.ImageField(upload_to='Images/about')
    title = models.CharField(max_length=70)
   
    def __str__(self):
        return self.title

class Index(models.Model):
    description = models.TextField()
    image = models.ImageField(upload_to='Images/index')
    title = models.CharField(max_length=70)
   
    def __str__(self):
        return self.title


class Contact(models.Model):
    full_name = models.CharField(max_length=50)
    subject = models.CharField(max_length=50)
    email_addres= models.EmailField(max_length=50)
    content = models.TextField()

    def __str__(self):
        return f"{self.full_name} {self.email_addres}"
    
class Story(models.Model):
    title = models.CharField(max_length=70)
    description = models.TextField()
    image = models.ImageField(upload_to='Images/story')
  
   
    def __str__(self):
        return self.title

class Faq(models.Model):
    title = models.CharField(max_length=70)
   
    def __str__(self):
        return self.title

class Product(models.Model):
    description = models.TextField()
    image = models.ImageField(upload_to='Images/product')
    title = models.CharField(max_length=70)
   
    def __str__(self):
        return self.title

class Products(models.Model):
    description = models.TextField()
    image = models.ImageField(upload_to='Images/products')
    title = models.CharField(max_length=70)
   
    def __str__(self):
        return self.title


class Sign_in(models.Model):
    description = models.TextField()
    image = models.ImageField(upload_to='Images/sign_in')
    title = models.CharField(max_length=70)
   
    def __str__(self):
        return self.title

class Sign_up(models.Model):
    description = models.TextField()
    image = models.ImageField(upload_to='Images/sign_up')
    title = models.CharField(max_length=70)
   
    def __str__(self):
        return self.title
