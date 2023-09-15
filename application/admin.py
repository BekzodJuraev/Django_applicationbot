from django.contrib import admin
from .models import Proposal
# Register your models here.
@admin.register(Proposal)
class Proposal(admin.ModelAdmin):
    list_display=['user','id_request','id_user','fullname','text','created','status']
    