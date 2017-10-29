__author__ = 'Administrator'
from django.forms import ModelForm
from django import forms
from iet_webapp.models import EventSuggestion,MemberApplicant,EventApplicant

class EventSuggestionForm(ModelForm):
    class Meta:
        model=EventSuggestion
        Fields=['isNewIdea','title','content']

class MemberApplicantForm(ModelForm):
    class Meta:
        model=MemberApplicant
        Fields=['name','matricNumber','school','year','email','phone','applyIETGlobalMember','applyIETNTUSSMember']

class EventApplicationForm(ModelForm):
    class Meta:
        model=EventApplicant
        exclude=['event']
        Fields=['name','matricNumber','school','year','email','phone']