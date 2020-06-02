from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse
from django.core.validators import RegexValidator

# Create your models here.

class UserProfileInfo(models.Model):

    user = models.OneToOneField(User,on_delete=models.CASCADE)

    def __str__(self):
      return self.user.username

    def get_absolute_url(self):
       return reverse('basic_app:detail',kwargs={'pk':self.pk})

BLOOD_GROUPS = [
    ('A+', 'A+'),
    ('A-', 'A-'),
    ('B+', 'B+'),
    ('B-', 'B-'),
    ('AB+', 'AB+'),
    ('AB-', 'AB-'),
    ('O+', 'O+'),
    ('O-', 'O-'),
]
class UserProfile(models.Model):
    user = models.ForeignKey(User,related_name='students',on_delete=models.CASCADE)
    name = models.CharField(max_length=100, blank=True, null= True)
    age = models.PositiveIntegerField(null=True, blank=True)
    phone_regex = RegexValidator(regex=r'^\+?1?\d{9,15}$', message="Entered the number in the format: '+999999999'. Up to 15 digits allowed.")
    phone = models.CharField(validators=[phone_regex], max_length=17, blank=True,null=True)
    address = models.CharField(max_length=500, blank=True, null=True)
    blood_group = models.CharField(choices=BLOOD_GROUPS, max_length=3, blank=True, null=True)


    def __str__(self):
        return "Profile for {}".format(self.user)