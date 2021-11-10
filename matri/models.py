from django.db import models
from django.contrib.auth.models import User
from django.db.models.fields import BooleanField
from django.db.models.fields.related import OneToOneField
import datetime

# Create your models here.

EDUCATION = {
    ("Bachelors", "Bachelors"),
    ("Masters", "Masters"),
    ("PHD", "PHD"),
    
}
OCCUPATION = {
    ("Teacher", "Teacher"),
    ("Businessman", "Businessman"),
    ("Software Developer", "Software Developer"),
    ("Banker", "Banker"),
    
    
}
CASTE = {
    ("Brahmin", "Brahmin"),
    ("Newar", "Newar"),
    ("Tamang", "Tamang"),
    ("Rai", "Rai"),
    
    
}
SALARY = {
    ("less than 20000", "less than 20000"),
    ("20000-30000", "20000-30000"),
    ("30000-40000", "30000-40000"),
    ("40000 above", "40000 above"),
    
    
}


class Profile(models.Model):
    firstname=models.CharField(max_length=200)
    lastname=models.CharField(max_length=200)
    gender=models.CharField(max_length=200)
    username= models.OneToOneField(User, null=True, on_delete=models.CASCADE)
    age=models.IntegerField()
    image = models.ImageField(upload_to="profiles/", blank=True, null=True)
    phone=models.IntegerField(unique=True)
    details=models.TextField()
    salary=models.CharField(max_length=200,choices=SALARY)
   
    view_count=models.PositiveIntegerField(default=0)
    education=models.CharField(max_length=200, choices=EDUCATION)
    caste=models.CharField(max_length=200, choices=CASTE)
    occupation=models.CharField(max_length=200, choices=OCCUPATION)
    address=models.CharField(max_length=200)

    def __str__(self): 
        return self.firstname


class RequestProfile(models.Model):

    gender=models.CharField(max_length=200)
    age1=models.IntegerField()
    age2=models.IntegerField()
    
    salary=models.CharField(max_length=200,choices=SALARY)
    username= models.OneToOneField(User, null=True, on_delete=models.CASCADE)
    education=models.CharField(max_length=200, choices=EDUCATION)
    caste=models.CharField(max_length=200, choices=CASTE)

 
