
from django.conf.urls.defaults import *
from piston.resource import Resource
from pyopenvz.api.views import Containers, Container

containers = Resource(Containers)
container = Resource(Container)

urlpatterns = patterns('',
   url(r'^containers/', containers),
   url(r'^containers/(?P<id>\d+)/', container),
)
