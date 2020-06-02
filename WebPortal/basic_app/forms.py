from django import forms
from django.contrib.auth.models import User
from basic_app.models import UserProfileInfo,UserProfile

class UserForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput())
    class Meta:
        model = User
        fields = ('username', 'email', 'password')          #imported form User model

class UserDetailForm(forms.ModelForm):
    class Meta:
        model = UserProfile
        fields = ('name', 'age', 'phone','address', 'blood_group')
    
    # def __init__(self, *args, **kwargs):
    #     super(UserDetailForm, self).__init__(*args, **kwargs)
    #     if self.instance:
    #         self.fields['user'].queryset = User.objects.filter(user_type="user")