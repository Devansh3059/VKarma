from django.shortcuts import render,redirect
from basic_app.forms import UserForm

from django.views.generic import View,TemplateView,ListView, DetailView, CreateView, UpdateView, DeleteView


from django.urls import reverse
from django.contrib.auth.decorators import login_required
from django.http import HttpResponseRedirect, HttpResponse
from django.contrib.auth import authenticate,login,logout
# Create your views here.

class IndexView(TemplateView):
    template_name  = 'index.html'

def home(request):
    return render(request,"home.html")

def home_profile(request):
    return render(request,"basic_app/home_profile.html")

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
# def addDetail(request,pk):
#     detailadded = False
#     if request.method == 'POST':
#         detail_form = StudentDetailForm(data=request.POST)
#         if detail_form.is_valid():
#             student = detail_form.save() 
#             student.save()
#             detailadded = True
#         else:
#             print(detail_form.errors)
#     else:
#         detail_form = StudentDetailForm()
#     return render(request,'basic_app/student_detail_form.html',{'detail_form':detail_form,
#                                                             'detailadded':detailadded})


# class StudentCreateView(CreateView):
#     fields = ('name','age','school','grade')
#     model = models.Student