from django.views.generic import ListView
from django.views.generic.detail import DetailView
import datetime

from django.views.generic.edit import CreateView

from .models import *


class ActiveEventList(ListView):
    template_name = './conf_app/event_list.html'
    queryset = Event.objects \
        .filter(
            end_time__gte=datetime.datetime.now() - datetime.timedelta(days=3)
        ).order_by('end_time')
    paginate_by = 5
    context_object_name = 'events'


class ArchiveEventList(ListView):
    template_name = './conf_app/event_list.html'
    queryset = Event.objects \
        .filter(
            end_time__lt=datetime.datetime.now() - datetime.timedelta(days=3)
        ).order_by('-end_time')
    paginate_by = 5
    context_object_name = 'events'


class EventDetailView(DetailView):
    model = Event
    context_object_name = 'event'


class EventCreate(CreateView):
    model = Event
    fields = '__all__'
    exclude = ['members'] #todo: exclude

    def get_form(self, form_class=None):
        form = super(EventCreate, self).get_form(form_class)
        form.fields['start_time'].widget.attrs.update({'class': 'datepicker'})
        return form
