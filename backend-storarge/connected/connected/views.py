from django.http import HttpResponseRedirect
from django.shortcuts import render_to_response
from django.template import RequestContext
from django.forms import ModelForm

def MemberRegistration(request):
    if request.user.is_authenticated():
        return HttpResponseRedirect('/profile/')
        # Let's maybe come back to this. What is a good url to redirect to?
    if request.method == 'POST':
        pass
    else:
        form = RegistrationForm()
        context = { 'form': form }
        return render_to_response('register.html', context,
                context_instance=RequestContext(request))

def loop(request, member_id):
    members = Member.objects.get(id=member_id)
    return render_to_response('app_connected/loop.html', {'members':members})

def menu(request):
    return render_to_response('app_connected/menu.html')

def bump(request):
    return render_to_response('app_connected/bump.html', {"member_id": 1})

def myinfo(request, member_id):
    me = Member.objects.get(id=member_id)
    return render_to_response('app_connected/myinfo.html', {'me':me})

