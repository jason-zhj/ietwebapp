from django.db import models

SMALL_IMG_SIZE="150px * 150px"
MEDIUM_IMG_SIZE="250px * 250px"

class Position(models.Model):
    title=models.CharField(max_length=200)
    # level 1 is highest, for P/VP
    # level 2 is maincommittee
    level=models.IntegerField()

    def __unicode__(self):
        return self.title
    def __str__(self):
        return self.title

class CommitteeMember(models.Model):
    name=models.CharField(max_length=256)
    email=models.CharField(max_length=500)
    position=models.ForeignKey(Position)
    head_shot=models.FileField(upload_to = 'headshot',help_text=SMALL_IMG_SIZE)

    def __unicode__(self):
        return self.name
    def __str__(self):
        return self.name



class Event(models.Model):
    STATUS_CHOICES=((0,'Upcoming'),(1,'Ongoing'),(2,'Past'))

    status=models.IntegerField(choices=STATUS_CHOICES)
    # 0-upcoming, 1-ongoing, 2-past
    title=models.CharField(max_length=200)
    description=models.TextField(max_length=3000)
    startEventTime=models.DateTimeField()
    endEventTime=models.DateTimeField()
    venue=models.CharField(max_length=500)
    participationRequirement=models.TextField(max_length=1000,blank=True)
    numberOfParticipants=models.IntegerField(default=0)
    numberOfApplicants=models.IntegerField(default=0) # to record the number of current applicants
    maximumNumberOfParticipants=models.IntegerField(default=100)
    mainPoster=models.FileField(upload_to='event')

    enableRegistration=models.BooleanField(default=False)

    def __unicode__(self):
        return self.title
    def __str__(self):
        return self.title

# in one-to-one with Event
class EventRecord(models.Model):
    description=models.TextField(max_length=5000)
    event=models.ForeignKey(Event)

    def __unicode__(self):
        return self.description
    def __str__(self):
        return self.description

# one Event - many Event Photos
class EventPhoto(models.Model):
    description=models.TextField(max_length=500)
    photo=models.FileField(upload_to='event/photos',help_text=MEDIUM_IMG_SIZE)
    event=models.ForeignKey(Event)

    def __unicode__(self):
        return self.description
    def __str__(self):
        return self.description

class Applicant(models.Model):
    SCHOOL_CHOICES=(
        ('SCE','SCE'),('CBE','CBE'),
        ('EEE','EEE'),('SPMS','SPMS'),
    )

    YEAR_CHOICES=(
        (1,'1'),(2,'2'),
        (3,'3'),(4,'4'),
    )
    name=models.CharField(max_length=200)
    email=models.EmailField(max_length=200)
    matricNumber=models.CharField(max_length=50)

    school=models.CharField(max_length=10,choices=SCHOOL_CHOICES)  # to be changed to choices

    year=models.IntegerField(choices=YEAR_CHOICES)  # 1 to 4

    phone=models.CharField(max_length=10)

    def __unicode__(self):
        return self.name
    def __str__(self):
        return self.name

# one event- many EventApplicants
class EventApplicant(Applicant):
    event=models.ForeignKey(Event)

class EventSuggestion(models.Model):
    TYPE_CHOICES=(
        (0,'Feedback to past events'),
        (1,'Idea of new Events'),
    )
    type=models.IntegerField(choices=TYPE_CHOICES)
    title=models.CharField(max_length=200)
    content=models.TextField(max_length=3000)


    def __unicode__(self):
        return self.title
    def __str__(self):
        return self.title

class MemberApplicant(Applicant):
    APPLICATION_CHOICES=(
        (0,'Apply for IET global member only'),
        (1,'Apply for IET-NTUSS committee member only'),
        (2,'Apply for both'),
    )
    applicationChoice=models.IntegerField(choices=APPLICATION_CHOICES)
