from django.conf.urls import patterns, include, url
from blog import views

urlpatterns = patterns('',
    url(r'^base', include('blog.urls')),
)
