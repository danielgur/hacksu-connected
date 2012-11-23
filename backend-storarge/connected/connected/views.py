from django.http import HttpResponseRedirect
from django.shortcuts import render_to_response
from django.template import RequestContext
from app_connected.forms import RegistrationForm
from app_connected.models import Member
from django.contrib.auth.models import User

def loop(request):
    user = request.user
    member = Member.objects.get(user=user)
    return render_to_response('app_connected/loop.html', {'member':member}, context_instance=RequestContext(request))

def menu(request):
    user = request.user
    member = Member.objects.get(user=user)
    return render_to_response('app_connected/menu.html', {'member':member}, context_instance=RequestContext(request))

def bump(request):
    user = request.user
    member = Member.objects.get(user=user)
    return render_to_response('app_connected/bump.html', {'member':member}, context_instance=RequestContext(request))

def myinfo(request):
    user = request.user
    member = Member.objects.get(user=user)
    return render_to_response('app_connected/myinfo.html', {'member':member}, context_instance=RequestContext(request))

