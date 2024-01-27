from django.shortcuts import render , redirect
from django.core.mail import send_mail
from .forms import Signupform ,UserActivateform ,UpdateUserForm,UpdateProfileForm
from .models import profile , UserAddress ,UserPhoneNumber
from django.contrib.auth.models import User


# Create your views here.


def singnup(request):
    if request.method == 'POST':
        form = Signupform(request.POST)
        if form.is_valid():
            
            username= form.cleaned_data['username']
            email= form.cleaned_data['email']
            password= form.cleaned_data['password1']
            myform =form.save()
            
            Profile = profile.objects.get(user__username=username)
            Profile.active=False
            Profile.save()
            #send email
            send_mail(
                subject="Activate Your Account",
                message=f"use this code {profile.code} to activate your account .",
                from_email="mm9073595@gmail.com",
                recipient_list=[email],
                fail_silently=False
            )
            return redirect(f'/accounts/{username}/activate')
    else:
        form = Signupform()
    return render(request,'registration/signup.html',{'form' :form})
     
     
     
     
     
     
     
      
def user_activate(request,username):
    Profile = profile.objects.get(user__username=username)
    if request.method == 'POST':
        form = UserActivateform(request.POST)
        if form.is_valid():
           code =form.cleaned_data['code']
           if profile.code == code:
               profile.active = True
               profile.code =''
               profile.code_used = True
               return redirect('/accounts/login')
            
        
    else:
        form = UserActivateform()
    return render(request,'registration/activation.html',{'form':form})
       
    


def Profile(request): 
    Profile = profile.objects.get(user = request.user)
    User_Address = UserAddress.objects.filter(user=request.user)
    PhoneNumber = UserPhoneNumber.objects.filter(user=request.user)
    return render(request,'registration/profile.html',{'Profile':profile ,'User_Address':User_Address ,'PhoneNumber':PhoneNumber})
 
     
def profile_edit(request):
  	#Get the profile
    Profile = profile.objects.get(user=request.user)
    
    if request.method == 'POST':
        userform = UpdateUserForm(request.POST,instance=request.user)
        profileform = UpdateProfileForm(request.POST,request.FILES,instance=profile)
        
        if userform.is_valid and profileform.is_valid:
            userform.save()
            new_profile = profileform.save(commit=False)
            new_profile.user = request.user
            new_profile.save()
            return redirect('/accounts/profile')
    else:
        userform = UpdateUserForm(instance=request.user)
        profileform = UpdateProfileForm(instance=profile)
    
    return render(request ,'accounts/profile_edit.html',context={'form1':userform,'form2':profileform})