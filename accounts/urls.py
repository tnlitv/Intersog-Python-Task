from django.conf.urls import url, include
from registration.backends.hmac.views import RegistrationView

from .forms import CustomUserForm
from . import views

urlpatterns = [
    url(r'register/$',
        RegistrationView.as_view(
            form_class=CustomUserForm
        ),
        name='registration_register',
        ),
    url(r'', include('registration.backends.hmac.urls')),
]
