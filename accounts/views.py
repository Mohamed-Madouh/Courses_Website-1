from imaplib import _Authenticator

from django.shortcuts import render , redirect
from .forms import Signupform  ,UpdateUserForm,UpdateProfileForm # Import the required forms
from .models import profile , UserAddress ,UserPhoneNumber
from django.contrib.auth.models import User


# Create your views here.

def signup(request):
    # If the request method is POST
    if request.method == 'POST':
        form = Signupform(request.POST) # Create a Signupform instance with POST data
        if form.is_valid(): # If the form is valid
            
            username = form.cleaned_data.get('username')
            email = form.cleaned_data.get('email')
            password = form.cleaned_data.get('password1')
            user = _Authenticator(username=username, password=password)
            form.save()
            return redirect('/accounts/login')# Save the user to the database
        else:
            # Get the user's profile
            Profile = profile.objects.get(user__username=username) # Set the profile's active field to False
            Profile.save() # Save the updated profile
            return render (request,'registration/profile.html',{'form':form})

    else:
        form =Signupform() # Create a Signupform instance with no data
        return render(request,'registration/signup.html',{'form' :form}) # Render the signup template with the form

def Profile(request):
    # Get the user's profile
    Profile = profile.objects.get(user = request.user)
    User_Address = UserAddress.objects.filter(user=request.user)
    PhoneNumber = UserPhoneNumber.objects.filter(user=request.user)
    return render(request,'registration/profile.html',{'Profile':Profile ,'User_Address':User_Address ,'PhoneNumber':PhoneNumber}) # Render the profile template with the user's profile, address, and phone number

def profile_edit(request):
    # Get the user's profile
    Profile = profile.objects.get(user=request.user)

    if request.method == 'POST':
        userform = UpdateUserForm(request.POST,instance=request.user) # Create an UpdateUserForm instance with POST data and the user instance
        profileform = UpdateProfileForm(request.POST,request.FILES,instance=Profile) # Create an UpdateProfileForm instance with POST data, uploaded files, and the profile instance

        if userform.is_valid() and profileform.is_valid(): # If both forms are valid
            userform.save() # Save the updated user
            new_profile = profileform.save(commit=False) # Save the profile with no commitment
            new_profile.user = request.user # Set the user for the new profile
            new_profile.save() # Save the updated profile
            return redirect('/accounts/profile') # Redirect to the profile page

    else:
        userform = UpdateUserForm(instance=request.user) # Create an UpdateUserForm instance with the user instance
        profileform = UpdateProfileForm(instance=Profile) # Create an UpdateProfileForm instance with the profile instance

    return render(request ,'accounts/profile_edit.html',context={'form1':userform,'form2':profileform}) # Render the profile edit template with both forms