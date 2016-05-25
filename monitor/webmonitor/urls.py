from django.conf.urls import patterns, include, url

urlpatterns = patterns('webmonitor.views',
    (r'^$','index'),
    (r'add_do/','adddo'),
    (r'add/','add'),
    (r'monitorlist/','monitorlist'),
)