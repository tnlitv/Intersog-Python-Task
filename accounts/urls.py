from django.conf.urls import url, include
from registration.backends.hmac.views import RegistrationView

from .forms import CustomUserForm
from .views import CustomUserDetailView

urlpatterns = [
    url(r'register/$',
        RegistrationView.as_view(
            form_class=CustomUserForm
        ),
        name='registration_register',
        ),
    url(r'profile/$', CustomUserDetailView.as_view(), name='profile'),
    url(r'', include('registration.backends.hmac.urls')),
    url(r'', include('django.contrib.auth.urls')),
]
