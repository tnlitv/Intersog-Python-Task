from django.conf.urls import url

from .views import *

urlpatterns = [
    url(r'add', EventCreate.as_view(), name='add'),
    # url(r'edit', views.edit, name='edit'),
    # url(r'delete', views.delete, name='delete'),
    url(r'event/(?P<pk>\d+)/', EventDetailView.as_view(), name='event/id'),
    url(r'archive', ArchiveEventList.as_view(), name='archive'),
    url(r'', ActiveEventList.as_view(), name='active'),
]