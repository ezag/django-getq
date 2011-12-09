from django.conf.urls.defaults import patterns

urlpatterns = patterns('getq_example.views',
    (r'^$', 'index'),
)
