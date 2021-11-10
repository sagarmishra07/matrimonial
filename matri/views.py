from django.shortcuts import render, redirect
from django.contrib import messages
from django.http import HttpResponse
from .models import *
from django.contrib.auth.models import User

import datetime


# Create your views here.


def Homepage(request):
    profile = Profile.objects.all()[:3]

    return render(request, 'homepage.html', {'profile': profile})


def CreateProfile(request):
    usr = Profile.objects.all()
    
    if request.method == 'POST':
        firstname = request.POST['firstname']
        lastname = request.POST['lastname']
        username = request.user
        gender = request.POST['gender']
        age = request.POST['age']

        img = request.FILES['image']

        phone = request.POST['phone']
        details = request.POST['details']
        salary = request.POST['salary']

        education = request.POST['education']
        caste = request.POST['caste']

        occupation = request.POST['occupation']

        address = request.POST['address']


        

        
           
          
      
        profile = Profile(firstname=firstname, lastname=lastname, age=age, username=username, gender=gender,image=img,
                              phone=phone, details=details, salary=salary, education=education,
                              caste=caste, occupation=occupation, address=address)
        profile.save()
        return redirect('/')
    else:
        return render(request, 'createprofile.html')


def ProfileDetail(request, id):
    profile = Profile.objects.get(id=id)
    profile.view_count = profile.view_count+1
    profile.save()
    return render(request, 'profiledetail.html', {'profile': profile})

def MyProfile(request):
    profiles = Profile.objects.filter(username=request.user)
    return render(request, 'myprofile.html',{'profiles':profiles})



def MyProfileEdit(request, id):
    profile = Profile.objects.get(id=id)
    return render(request, 'profileedit.html', {'profile': profile})

def UpdateProfile(request, id):
   
 
    if request.method == 'POST':
        firstname = request.POST['firstname']
        lastname = request.POST['lastname']
    

        age = request.POST['age']

        img = request.FILES['image']
        gender = request.POST['gender']
        phone = request.POST['phone']
        details = request.POST['details']
        salary = request.POST['salary']

        education = request.POST['education']
        caste = request.POST['caste']

        occupation = request.POST['occupation']

        address = request.POST['address']
       
        usr = User.objects.get(id=request.user.id)
        username=usr
        profile = Profile(id=id,firstname=firstname,username=usr, lastname=lastname, age=age,gender=gender, image=img,
                              phone=phone, details=details, salary=salary, education=education,
                              caste=caste, occupation=occupation, address=address)
        profile.view_count = profile.view_count+1
        profile.save()
        return redirect('/')
    
    else:
        return render(request, 'myprofile.html')

def DeleteProfile(request, id):
    profile = Profile.objects.get(id=id)
    profile.delete()
    return redirect('/')


def ConnectionInfo(request):

    if request.method == 'POST':
        gender = request.POST['gender']
        username = request.user
        
        age1 = request.POST['age1']
        age2 = request.POST['age2']
        user = Profile.objects.get(id=request.user.id)
        
        education = request.POST['education']
        caste = request.POST['caste']

      



        

        
           
          
      
        requestprofile = RequestProfile(gender=gender, username=username, age1=age1,age2=age2,
                            education=education,caste=caste)
        requestprofile.save()
        return redirect('/')
    else:
        return render(request, 'connectioninfo.html')




def MyConnection(request):
    requestprofile = RequestProfile.objects.filter(username=request.user)
    return render(request, 'myconnection.html',{'requestprofile':requestprofile})



def MyConnectionEdit(request, id):
    requestprofile = RequestProfile.objects.get(id=id)
    return render(request, 'myconnectionedit.html', {'requestprofile': requestprofile})

def ConnectionUpdate(request, id):
   
 
    if request.method == 'POST':
        
        age1 = request.POST['age1']
        age2 = request.POST['age2']

      
        gender = request.POST['gender']
      


        education = request.POST['education']
        caste = request.POST['caste']

       
        usr = User.objects.get(id=request.user.id)
        username=usr
        requestprofile = RequestProfile(id=id,username=usr, age1=age2,gender=gender,age2=age2,
                           education=education,
                              caste=caste)
       
        requestprofile.save()
        return redirect('/')
    
    else:
        return render(request, 'myprofile.html')

def ConnectionDelete(request, id):
    requestprofile = RequestProfile.objects.get(id=id)
    requestprofile.delete()
    return redirect('/')




def YourMatches(request):
    requestprofile = RequestProfile.objects.get(username=request.user)

    age1=requestprofile.age1
    age2=requestprofile.age2
    
    gender=requestprofile.gender
    education=requestprofile.education
    caste=requestprofile.caste


    
    requestprofile = RequestProfile.objects.filter(gender=gender) & RequestProfile.objects.filter(education=education) & RequestProfile.objects.filter(caste=caste) & RequestProfile.objects.filter().exclude(username=request.user)
    
    return render(request, 'matches.html',{'requestprofile':requestprofile})

def Search(request):
 

    return render(request, 'search.html')


def Feedback(request):
    return render(request, 'feedback.html')
