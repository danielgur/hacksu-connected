from django.shortcuts import render_to_response
from app_connected.models import Member, Login

def index(request):
    members = Member.objects.all()
    login = Login.objects.all()
    return render_to_response('app_connected/index.html', {'members': members, 'login': login})# Create your views here.
