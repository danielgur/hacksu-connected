from django.template import RequestContext
from django.shortcuts import render_to_response
from app_connected.models import Member, Login

def index(request):
    return render_to_response('app_connected/index.html')

def login(request):
     m = Login.objects.get(username=request.POST['username'])
     if m.password == request.POST['password']:
        request.session['member_id'] = m.id
        return render_to_response('app_connected/menu.html')
     else:
        return HttpResponse("Your username and password didn't match.")

def loop(request, member_id):
    members = Member.objects.get(id=request.session['member_id'])
    return render_to_response('app_connected/loop.html', {'members':members})

def menu(request):
    return render_to_response('app_connected/menu.html')

def bump(request):
    return render_to_response('app_connected/bump.html', {"member_id":request.session['member_id']})

def logout(request):
    try:
        del request.session['member_id']
    except KeyError:
        pass
    return HttpResponse("You're logged out.")

def myinfo(request, member_id):
    me = Member.objects.get(id=member_id)
    return render_to_response('app_connected/myinfo.html', {'me':me})

