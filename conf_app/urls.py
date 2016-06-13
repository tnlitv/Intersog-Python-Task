from django.conf.urls import url

from .views import *

urlpatterns = [
    url(r'add', EventCreate.as_view(), name='add'),
    url(r'edit/(?P<pk>\d+)', EventUpdate.as_view(), name='edit'),
    url(r'delete/(?P<pk>\d+)', EventDelete.as_view(), name='delete'),
    url(r'event/(?P<pk>\d+)', EventDetailView.as_view(), name='event_id'),
    url(r'archive', ArchiveEventList.as_view(), name='archive'),
    url(r'', ActiveEventList.as_view(), name='active'),
]
