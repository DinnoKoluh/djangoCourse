from django import forms

# django validation 
from django.core import validators

# my custom validatior
# the first character has to be between 'A' and 'Z'
def custom_validator(value):
    if value[0] < 'A' or value[0] > 'Z':
        raise forms.ValidationError("Name has to start with upper case letter")




class UserInput(forms.Form):
    name = forms.CharField(validators=[custom_validator])
    email = forms.EmailField()
    v_email = forms.EmailField(label="Enter email again")

    # form validation, for bots
    # required = False means that this field won't show up on the page but it will stick in the HTML
    # django's built in validator
    botcatcher = forms.CharField(required = False, widget = forms.HiddenInput, validators=[validators.MaxLengthValidator(0)]) 

    # # DOING FORM VALIDATION MANUALLY
    # # clean is a keyword for checking form validation you add _attribute as to what attribute we want to validate
    # def clean_botcatcher(self):
    #     botcatcher = self.cleaned_data['botcatcher']

    #     # a bot came into the HTML and filled out the field botcatcher
    #     if len(botcatcher) > 0:
    #         raise forms.ValidationError(" Gotcha bot ")
    #     return botcatcher

    def clean(self):
        all_clean_data = super().clean() # grabs all the data from the form
        email = all_clean_data['email']
        v_email = all_clean_data['v_email']
        if email != v_email:
            raise forms.ValidationError("Emails are not the same")
