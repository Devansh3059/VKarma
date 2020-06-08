from django.shortcuts import render,redirect
from basic_app.forms import UserForm,UserDetailForm

from django.views.generic import View,TemplateView,ListView, DetailView, CreateView, UpdateView, DeleteView
from .models import *

from django.urls import reverse
from django.contrib.auth.decorators import login_required
from django.http import HttpResponseRedirect, HttpResponse
from django.contrib.auth import authenticate,login,logout
from django.contrib.auth.mixins import LoginRequiredMixin

import string
import random
# Create your views here.

def id_generator(size=6, chars=string.ascii_uppercase + string.digits):
    return ''.join(random.choice(chars) for _ in range(size))


class IndexView(TemplateView):
    template_name  = 'index.html'

def home(request):
    return render(request,"home.html")

def home_profile(request):
    return render(request,"basic_app/home_profile.html")

def profile_delete(request):
    return render(request,'basic_app/profile_delete.html')

def register(request):
    registered = False
    if request.method == 'POST':
        user_form = UserForm(data=request.POST)
        if user_form.is_valid():
            user = user_form.save()        
            user.set_password(user.password)       
            user.save()
            registered = True
        else:
            print(user_form.errors)
    else:
        user_form = UserForm()
    return render(request,'basic_app/registration.html',{'user_form':user_form,
                                                            'registered':registered})

@login_required
def user_logout(request):
    logout(request)
    return redirect("/")
    # return HttpResponseRedirect(reverse('basic_app:index'))


def user_login(request):
    loggedin = False
    if request.method == 'POST':
        username = request.POST.get('username')    #.get(username) is from name attribute of login.html username field
        password = request.POST.get('password')

        user = authenticate(username=username,password=password)

        if user:
            if user.is_active:
                login(request,user)  #user obect returned from the authenticate method
                loggedin =True
                return redirect("/",{'loggedin':loggedin,'user':user})
                # return HttpResponseRedirect(reverse('index'))

            else:
                return HttpResponse("Account not Active")

        else:
            print("Someone tried to login and failed!")
            print('Username:{} and Password:{}'.format(username,password))
            return HttpResponse("Invalid Login Details")

    else:
        return render(request,'basic_app/login.html',{})

@login_required(login_url='/login/')
def AddDetail(request):
    detailadded = False
    user = request.user
    try:
        profile = UserProfile.objects.get(user=user)
    except:
        profile = UserProfile.objects.create(user=user)
    if request.method == 'POST':
        form = UserDetailForm(request.POST, instance=profile)
        if form.is_valid():
            form.save()
            # return redirect('basic_app:addDetail')
            detailadded = True
    else:
        form = UserDetailForm(instance=profile)
    return render(request, 'basic_app/student_detail_form.html', {'form': form, 'detailadded':detailadded, 'user':user})

class StudentDetailView(LoginRequiredMixin, ListView):
    login_url = '/login/'
    redirect_field_name = 'basic_app:login'

    def get_queryset(self):
        return UserProfile.objects.filter(user=self.request.user)

@login_required(login_url='/login/')
def DeleteUserProfile(request):
    user = request.user
    deletedetail =False
    profile = UserProfile.objects.get(user=user)
    if request.method == 'POST':
        profile.delete()
        deletedetail =True
        return render(request, 'basic_app/profile_delete.html', {'user':user,'deletedetail':deletedetail})
        # messages.add_message(request, messages.INFO, "Your Message")
    else:
        return render(request, 'basic_app/profile_delete.html', {'user':user,'deletedetail':deletedetail})