from django.views.generic import ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView

from .models import Chat


class ChatList(ListView):
    model = Chat
    paginate_by = 5


class ChatDetailView(DetailView):
    model = Chat
    context_object_name = 'chat'


class ChatCreate(CreateView):
    model = Chat
    fields = ['title', 'users']
    success_url = '/chat'


class ChatUpdate(UpdateView):
    model = Chat
    fields = ['title', 'users']
    success_url = '/chat'


class ChatDelete(DeleteView):
    model = Chat
    success_url = '/chat'
