from django.shortcuts import render
from basic_app.forms import UserForm

from django.views.generic import View,TemplateView,ListView, DetailView, CreateView, UpdateView, DeleteView
# Create your views here.

class IndexView(TemplateView):
    template_name  = 'index.html'

def register(request):

    registered = False

    if request.method == 'POST':
        user_form = UserForm(data=request.POST)

        if user_form.is_valid():

            user = user_form.save()         #saving info in database
            user.set_password(user.password)        #hashing the password
            user.save()

            registered = True

        else:
            print(user_form.errors)

    else:
        user_form = UserForm()

    return render(request,'basic_app/registration.html',{'user_form':user_form,
                                                            'registered':registered})
