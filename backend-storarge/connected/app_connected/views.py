from django.http import HttpResponseRedirect
from django.http import HttpResponseRedirect
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from django.shortcuts import render_to_response
from django.template import RequestContext
from app_connected.forms import RegistrationForm, LoginForm
from app_connected.models import Member
from django.contrib.auth import authenticate, login, logout

def MemberRegistration(request):
    if request.user.is_authenticated():
        return HttpResponseRedirect('/menu/')
        # Let's maybe come back to this. What is a good url to redirect to?

    if request.method == 'POST':
        form = RegistrationForm(request.POST)
        if form.is_valid():
            user = User.objects.create_user(username = form.cleaned_data['username'], email = form.cleaned_data['email'], password = form.cleaned_data['password'])
            user.save()
            member = Member(user=user, name = form.cleaned_data['name'])
            member.save()
            return HttpResponseRedirect('/menu/')
        else:
            return render_to_response('app_connected/register.html', {'form': form}, context_instance=RequestContext(request))
    else:
        form = RegistrationForm()
        context = { 'form': form }
        return render_to_response('app_connected/register.html', context, context_instance=RequestContext(request))


def LoginRequest(request):
    if request.user.is_authenticated():
        return HttpResponseRedirect('/menu/')
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            member = authenticate(username=username, password=password)
            if member is not None:
                login(request, member)
                return HttpResponseRedirect('/menu/')
            else:
                return render_to_response('app_connected/login.html', {'form':form}, context_instance=RequestContext(request))
        else:
            return render_to_response('app_connected/login.html', {'form':form}, context_instance=RequestContext(request))
    else:
        form = LoginForm()
        context = {'form':form}
        return render_to_response('app_connected/login.html', context, context_instance=RequestContext(request))


def LogoutRequest(request):
    logout(request)
    return HttpResponseRedirect('/')



