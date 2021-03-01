import os 
os.environ.setdefault('DJANGO_SETTINGS_MODULE','first_project.settings')

import django
django.setup()

# FAKE POPULATION SCRIPT TO POPULATE DATABASE
import random
from first_app.models import User
from faker import Faker

fakegen = Faker()

def populate(N = 5):

    for entry in range(N):
        # get the topic for the entry

        # create the fake data for this entry
        name = fakegen.name().split(" ")
        fake_f_name = "Dinno "
        fake_l_name = name[1]
        fake_email = fakegen.email()

        # create the new webpage entry
        usr_info = User.objects.get_or_create(f_name = fake_f_name, l_name = fake_l_name, email = fake_email)

if __name__ == '__main__':
    print("Populating script with fake user data!")
    populate(10)
    print("Populating completed!")
