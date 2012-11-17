# app_connected/api.py

from tastypie import fields
from tastypie.resources import ModelResource
from app_connected.models import Member

class MemberResource(ModelResource):
    loops = fields.ToManyField('self', 'loop', full=True, null=True)    

    class Meta:
        queryset = Member.objects.all()
        resource_name = 'member'


