from django.db import models

class Login(models.Model):
    username = models.CharField(max_length=200)
    password = models.CharField(max_length=200)
    def __unicode__(self):
        return self.username

class Member(models.Model):
    name = models.CharField(max_length=200)
    phone_number = models.CharField(max_length=20, blank=True)
    email = models.CharField(max_length=200)
    twitter = models.CharField(max_length=100, blank=True)
    facebook = models.CharField(max_length=100, blank=True)
    bio = models.CharField(max_length=200, blank=True)
    loop = models.ManyToManyField('self')
    def __unicode__(self):
        return self.name


