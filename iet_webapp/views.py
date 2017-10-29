from django.shortcuts import render, render_to_response,HttpResponseRedirect
from iet_webapp.models import CommitteeMember,Position,Event,EventSuggestion
from iet.settings import MEDIA_URL
from iet_webapp.forms import *
from django.views.decorators.csrf import csrf_exempt
from django.core.mail import send_mail

# Create your views here.
def home(request):
    events=Event.objects.all().order_by('startEventTime')[0:3]
    return render_to_response("home.html",{'events':events})

def about(request):
    committeeMembers=CommitteeMember.objects.all()
    return render_to_response("about.html",{'committeeMembers':committeeMembers,'MEDIA_URL':MEDIA_URL})

@csrf_exempt
def event(request):
    upcomingEvents=Event.objects.filter(status=0)
    ongoingEvents=Event.objects.filter(status=1)
    pastEvents=Event.objects.filter(status=2)
    form=EventSuggestionForm()
    if (request.method=='POST'):
        # this is a suggestion submission

        form=EventSuggestionForm(request.POST)
        if (form.is_valid()):
            type=form.cleaned_data['type']
            title=form.cleaned_data['title']
            content=form.cleaned_data['content']

            # save into database
            newSuggestion=EventSuggestion(type=type,title=title,content=content)
            newSuggestion.save()

            # redirect to success page
            return HttpResponseRedirect('/event/suggestionSubmitted')

    # if it's a GET request or the submitted form is invalid
    return render_to_response("event.html",{'upcomingEvents':upcomingEvents,'ongoingEvents':ongoingEvents,'pastEvents':pastEvents,'eventSuggestionForm':form})


def eventSuggestionSubmitted(request):
    return render_to_response("eventSuggestionSubmitted.html")

def errorHandler(request):
    nextPage=request.GET['next']
    return render_to_response("error.html",{'nextPage':nextPage})


@csrf_exempt
def join(request):
    form=MemberApplicantForm()

    if (request.method=='POST'):
        # process the submitted form
        form=MemberApplicantForm(request.POST)
        if (form.is_valid()):
            # save the data
            name=form.cleaned_data['name']
            email=form.cleaned_data['email']
            matricNumber=form.cleaned_data['matricNumber']
            school=form.cleaned_data['school']
            year=form.cleaned_data['year']
            phone=form.cleaned_data['phone']
            applicationChoice=form.cleaned_data['applicationChoice']

            newMemberApplicant=MemberApplicant(name=name,email=email,matricNumber=matricNumber,\
                                               school=school,year=year,phone=phone,applicationChoice=applicationChoice)
            newMemberApplicant.save()

            #redirect to successful submission page
            return HttpResponseRedirect('/successfulSubmission?next=join')

    # if Get request or invalid form submitted
    return render_to_response('join.html',{'MemberApplicantForm':form})



@csrf_exempt
def successfulSubmission(request):
    nextPage=request.GET['next']
    return render_to_response('successfulSubmission.html',{'nextPage':nextPage})

@csrf_exempt
def eventDetail(request,eventId):

    form=EventApplicationForm()
    event=Event.objects.get(id=eventId)

    if (request.method=='POST'):
        # process the submitted form
        form=EventApplicationForm(request.POST)
        if (form.is_valid()):
            # save the data
            name=form.cleaned_data['name']
            email=form.cleaned_data['email']
            matricNumber=form.cleaned_data['matricNumber']
            school=form.cleaned_data['school']
            year=form.cleaned_data['year']
            phone=form.cleaned_data['phone']
            event=Event.objects.get(id=eventId)
            newEventApplicant=EventApplicant(name=name,email=email,matricNumber=matricNumber,\
                                               school=school,year=year,phone=phone,event=event)
            newEventApplicant.save()
            # increment number of applicants for that event
            event.numberOfApplicants =event.numberOfApplicants+1
            event.save()

            #redirect to successful submission page
            return HttpResponseRedirect('/successfulSubmission?next=event/'+str(eventId))


    # if Get request or invalid form
    if (event==None):
        # event not found, redirect to error page
        return  HttpResponseRedirect("error.html?next=event")
    else:
        return render_to_response("eventDetail.html",{'event':event,'form':form})