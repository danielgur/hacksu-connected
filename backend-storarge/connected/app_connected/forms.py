from django import forms
from django.contrib.auth.models import User
from django.forms import ModelForm
from app_connected.models import Member


class RegistrationForm(ModelForm):
    name = forms.CharField(label = (u'Name'))
    username = forms.CharField(label = (u'User Name'))
    email = forms.EmailField(label = (u'Email Address'))
    password = forms.CharField(label = (u'Password'), widget=forms.PasswordInput(render_value=False))
    password1 = forms.CharField(label = (u'Verify Password'), widget=forms.PasswordInput(render_value=False))
    phone_number = forms.CharField(label = (u'Phone number'))
    facebook = forms.CharField(label = (u'Facebook'))
    twitter = forms.CharField(label = (u'Twitter'))
    bio = forms.CharField(label = (u'Bio'), widget=forms.Textarea)

    
    class Meta:
        model = Member
        exclude = ('user',)

    def clean_username(self):
        username = self.cleaned_data['username']
        try:
            User.objects.get(username=username)
        except User.DoesNotExist:
            return username
        raise forms.ValidationError("That username is already taken, please try a new one!")

    def clean(self):
        if self.cleaned_data['password'] != self.cleaned_data['password1']:
            raise forms.ValidationError("The passwords you input did not match. Please try again.")
        return self.cleaned_data

class LoginForm(forms.Form):
    username = forms.CharField(label = (u'User Name'))
    password = forms.CharField(label = (u'Password'), widget=forms.PasswordInput(render_value=False))



