from django.contrib import admin
from iet_webapp.models import *

# Register your models here.

class EventAdmin(admin.ModelAdmin):
    readonly_fields = ('numberOfApplicants',)

class MemberApplicantAdmin(admin.ModelAdmin):
    list_display=('name','email','applicationChoice',)
    list_filter=('applicationChoice',)
    search_fields=('applicationChoice',)

class EventApplicantAdmin(admin.ModelAdmin):
    list_display=('name','email','event',)
    list_filter=('event',)
    search_fields=('name',)

class CommitteeMemberAdmin(admin.ModelAdmin):
    list_display=('name','email','position',)
    list_filter=('position',)
    search_fields=('name',)


class PositionAdmin(admin.ModelAdmin):
    list_display=('title','level',)
    list_filter=('level',)
    search_fields=('title',)

class EventSuggestionAdmin(admin.ModelAdmin):
    list_display=('title','type',)
    list_filter=('type',)
    search_fields=('title',)

admin.site.register(Position,PositionAdmin)
admin.site.register(CommitteeMember,CommitteeMemberAdmin)
admin.site.register(Event,EventAdmin)
admin.site.register(EventRecord)
admin.site.register(EventPhoto)
admin.site.register(EventApplicant,EventApplicantAdmin)
admin.site.register(MemberApplicant,MemberApplicantAdmin)
admin.site.register(EventSuggestion,EventSuggestionAdmin)
