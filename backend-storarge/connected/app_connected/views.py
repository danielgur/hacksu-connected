from django.http import HttpResponseRedirect
from django.shortcuts import render_to_response
from django.template import RequestContext
from app_connected.forms import RegistrationForm

def MemberRegistration(request):
    if request.user.is_authenticated():
        return HttpResponseRedirect('/profile/')
# Let's maybe come back to this. What is a good url to redirect to?

    if request.method == 'POST':
        pass
    else:
        form = RegistrationForm()
        context = { 'form': form }
        return render_to_response('app_connected/register.html', context, context_instance=RequestContext(request))
