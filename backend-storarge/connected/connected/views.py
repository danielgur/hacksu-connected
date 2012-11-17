from django.template import RequestContext
from django.shortcuts import render_to_response
from app_connected.models import Member, Login

def index(request):
    return render_to_response('app_connected/index.html')

def loop(request, member_id):
    members = Member.objects.get(id=member_id)
    return render_to_response('app_connected/loop.html', {'members':members})

def menu(request):
    return render_to_response('app_connected/menu.html')

def bump(request):
    return render_to_response('app_connected/bump.html')