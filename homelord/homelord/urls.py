from django.conf.urls import patterns, include, url
from django.contrib import admin
from django.views.generic import TemplateView
urlpatterns = patterns('',
                       url(r'^finances', include('finances.urls')),
                       url(r'^search', include('searches.urls')),
                       url(r'^$', TemplateView.as_view(template_name='main.html'), name='main'),
                       url(r'^admin/', include(admin.site.urls)),
)
