from django.contrib.auth import get_user_model
from django.contrib.auth.forms import UserCreationForm

# LOOK UP THE DOCUMENTATION

class UserCreateForm(UserCreationForm):
    class Meta():
        fields = ('username', 'email', 'password1', 'password2')
        model = get_user_model()

    def __init__(self, *args, **kvargs):
        super().__init__(*args, **kvargs)
        self.fields['username'].label = 'Display Name'
        self.fields['email'].label = 'Email Address'
