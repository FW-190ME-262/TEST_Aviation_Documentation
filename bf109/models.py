from django.contrib.admindocs.utils import ROLES
from django.db import models
from django.contrib.auth.models import User

# Create your models here.
# class Classifikeishen(models.Model):
#     fighter_jet =
#     transport =
#     multi_purpose =
from django.utils import timezone

from django.db import models


class Object(models.Model):
    name = models.CharField(max_length=250)
    photo = models.ImageField()
    text = models.TextField()
    specifications = models.TextField()
    historik = models.TextField()
    avariem_situation = models.TextField()
    date_publication = models.DateField()
    # blender_model = models.FileField(upload_to='blender_models/', blank=True, null=True)


class Praktic_avariem_play(models.Model):
    aircraft = models.ForeignKey(Object, on_delete=models.CASCADE, related_name='emergency_situations')
    avariem_situation1 = models.TextField()
    avariem_situation2 = models.TextField()
    avariem_situation4 = models.TextField()
    avariem_situation5 = models.TextField()
    avariem_situation6 = models.TextField()
    avariem_situation7 = models.TextField()
    avariem_situation8 = models.TextField()
    avariem_situation9 = models.TextField()
    avariem_situation10 = models.TextField()

    # classifikeishen = models.CharField(max_length=255, default='default_value')


# praktic_avariem_play = models.ForeignKey(Praktic_avariem_play, on_delete=models.CASCADE)


class MyModel(models.Model):
    my_file = models.FileField(upload_to='files/')
    my_image = models.ImageField(upload_to='images/')


class Profile(models.Model):
    recaptcha = ()
    username = models.CharField(max_length=100)
    email = models.EmailField(max_length=100)
    password = models.CharField(max_length=100)
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    balance = models.PositiveIntegerField(default=0)  # Store balance as coins


class PromoCode(models.Model):
    code = models.CharField(max_length=50, unique=True)
    discount = models.PositiveIntegerField(default=0)  # Discount as percentage or coin value
    is_for_balance = models.BooleanField(default=False)  # True for balance top-up, False for free download
    is_active = models.BooleanField(default=True)


class SiteVisitor(models.Model):
    date = models.DateField(default=timezone.now)
    count = models.PositiveIntegerField(default=0)
