from django import forms
from first_app.models import User

class NewUserForm(forms.ModelForm):
    class Meta():
        # should be always called model
        model = User
        fields = '__all__'