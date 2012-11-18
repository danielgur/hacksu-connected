from models import Member, Login
from django.db import models
from django.forms import ModelForm

class LoginForm(ModelForm):
    class Meta:
        model = Login
