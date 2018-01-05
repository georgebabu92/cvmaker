from django.conf.urls import include, url
from django.conf import settings
from django.views import static
from django.contrib import admin

# admin.autodiscover()
from applications.general.views import GeneralDashboard

urlpatterns = [
    url(r'^$', GeneralDashboard.as_view(), name='dashboard'),
    url(r'^cvmaker-admin/', include(admin.site.urls)),
    url(r'^accounts/', include('applications.accounts.urls', namespace='accounts')),
]

urlpatterns = [
                  url(r'^media/(?P<path>.*)$', static.serve, {'document_root': settings.MEDIA_ROOT, }),
                  url(r'', include('django.contrib.staticfiles.urls')),
              ] + urlpatterns

if not settings.DEBUG:
    urlpatterns += [
        url(r'^media/(?P<path>.*)$', static.serve,
            {'document_root': settings.MEDIA_ROOT, }),
        url(r'^static/(?P<path>.*)$', static.serve,
            {'document_root': settings.STATIC_ROOT}),
    ]
