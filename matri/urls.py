from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
     path('', views.Homepage, name="home"),
     path("createprofile/", views.CreateProfile, name="createprofile"),
     path("profile/<int:id>/", views.ProfileDetail, name="profiledetail"),
     path("myprofile/", views.MyProfile, name="myprofile"),
     path("myprofile/<int:id>", views.MyProfileEdit, name="myprofileedit"),
     path("updateprofile/<int:id>", views.UpdateProfile, name="updateprofile"),
     path("deleteprofile/<int:id>", views.DeleteProfile, name="deleteprofile"),
     
     path("connectioninfo/", views.ConnectionInfo, name="connectioninfo"),
     path("myconnection/", views.MyConnection, name="myconnection"),
     path("myconnectionedit/<int:id>", views.MyConnectionEdit, name="myconnectionedit"),
     path("connectionupdate/<int:id>", views.ConnectionUpdate, name="connectionupdate"),
     path("deleteconnection/<int:id>", views.ConnectionDelete, name="connectiondelete"),
     
    
     
     path('showmatches/', views.YourMatches, name="showmatches"),

     path('search/', views.Search, name="search"),
     path('feedback/', views.Feedback, name="feedback"),

]
