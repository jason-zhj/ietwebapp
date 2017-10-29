from django.conf.urls import patterns, include, url
from django.contrib import admin
from django.conf.urls.static import static
from iet import settings

urlpatterns = patterns('',
    # Examples:
    url(r'^$', 'iet_webapp.views.home'),
    url(r'^about$', 'iet_webapp.views.about'),
    url(r'^event$', 'iet_webapp.views.event'),
    url(r'^event/(?P<eventId>\d+)$', 'iet_webapp.views.eventDetail'),
    url(r'^event/suggestionSubmitted$', 'iet_webapp.views.eventSuggestionSubmitted'),
    url(r'^successfulSubmission$', 'iet_webapp.views.successfulSubmission'),
    url(r'^error$', 'iet_webapp.views.errorHandler'),
    url(r'^join$', 'iet_webapp.views.join'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^admin/', include(admin.site.urls)),
)



# urlpattern to serve media files
urlpatterns +=static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)