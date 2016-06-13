from django.conf.urls import url
from django.views.generic import TemplateView

from chat.views import ChatList, ChatDetailView, ChatCreate, ChatUpdate, ChatDelete

urlpatterns = [
    url(r'add/$', ChatCreate.as_view(), name='add'),
    url(r'edit/(?P<pk>\d+)', ChatUpdate.as_view(), name='edit'),
    url(r'delete/(?P<pk>\d+)', ChatDelete.as_view(), name='delete'),
    url(r'chat/(?P<pk>\d+)$', TemplateView.as_view(template_name='chat/chat_detail.html'), name='chat_detail'),
    url(r'^$', ChatList.as_view(), name='chat_list'),
]
