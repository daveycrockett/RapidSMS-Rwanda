from django.conf.urls.defaults import *
from django.conf import settings
from django.contrib import admin
admin.autodiscover()
from reporters.views import add_group, edit_group, index

urlpatterns = patterns('',
    url(r'^$', 'rapidsms.views.dashboard', name='rapidsms-dashboard'),
    (r'^admin/', include(admin.site.urls)),
    (r'^account/', include('rapidsms.urls.login_logout')),
    (r'^ajax/', include('rapidsms.contrib.ajax.urls')),
    (r'^export/', include('rapidsms.contrib.export.urls')),
    (r'^httptester/', include('rapidsms.contrib.httptester.urls')),
    (r'^locations/', include('rapidsms.contrib.locations.urls')),
    (r'^messaging/', include('rapidsms.contrib.messaging.urls')),
    (r'^messagelog/', include('rapidsms.contrib.messagelog.urls')),
    (r'^ubuzima/', include('ubuzima.urls')),
    (r'^reporters/', include('reporters.urls')),

    url(r'^groups/$', index),
    url(r'^groups/add$', add_group),
    url(r'^groups/(?P<pk>\d+)$', edit_group),

    (r'^ambulances/', include('ambulances.urls')),
    (r'^logger/', include('logger.urls')),
)

if settings.DEBUG:
    urlpatterns += patterns('',
        # helper URLs file that automatically serves the 'static' folder in
        # INSTALLED_APPS via the Django static media server (NOT for use in
        # production)
        (r'^', include('rapidsms.urls.static_media')),
    )
