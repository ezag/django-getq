from django.conf.urls.defaults import patterns, include, url

urlpatterns = patterns('',
    url(r'^$', include('django_getq.getq_example.urls')),
)
