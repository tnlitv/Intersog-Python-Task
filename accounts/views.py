from django.views.generic.detail import DetailView
from conf_app.models import CustomUser


class CustomUserDetailView(DetailView):
    model = CustomUser
    context_object_name = 'user'
    template_name = 'accounts/profile_detail.html'

    def get_object(self, **kwargs):
        return self.request.user
