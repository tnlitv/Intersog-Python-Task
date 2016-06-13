from registration.forms import RegistrationForm

from conf_app.models import CustomUser


class CustomUserForm(RegistrationForm):
    class Meta:
        model = CustomUser
        fields = ['username',
                  'first_name',
                  'last_name',
                  'email',
                  'userpic',
                  'company',
                  ]
