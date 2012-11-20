from django.db import models
from django.db.models.signals import post_save
from django.contrib.auth.models import User

class Member(models.Model):
    user = models.OneToOneField(User)
    name = models.CharField(max_length=100)
    phone_number = models.CharField(max_length=20, blank=True)
    email = models.CharField(max_length=200)
    twitter = models.CharField(max_length=100, blank=True)
    facebook = models.CharField(max_length=100, blank=True)
    bio = models.CharField(max_length=200, blank=True)
    loop = models.ManyToManyField('self', blank=True)
    def __unicode__(self):
        return self.name


