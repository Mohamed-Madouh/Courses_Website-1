from django.urls import path
from .views import profile ,signup
from accounts import views
app_name ='accounts'
urlpatterns = [
    path('signup/', views.signup, name='signup'),
    path('profile/',profile,name='profile'),
   
   

]