import os 
os.environ.setdefault('DJANGO_SETTINGS_MODULE','first_project.settings')

import django
django.setup()

# FAKE POPULATION SCRIPT TO POPULATE DATABASE
import random
from first_app.models import AccessRecord, Webpage, Topic
from faker import Faker

fakegen = Faker()

topics = ['Search', 'Socail', 'Marketplace', 'News', 'Games']

def add_topic():
    t = Topic.objects.get_or_create(topic_name = random.choice(topics))[0] # it outputs a tuple and the zeroth term is what we need
    t.save()
    return t

def populate(N = 5):

    for entry in range(N):
        # get the topic for the entry
        top = add_topic()

        # create the fake data for this entry
        fake_url = fakegen.url()
        fake_date = fakegen.date()
        fake_name = fakegen.company()

        # create the new webpage entry
        webpg = Webpage.objects.get_or_create(topic = top, name = fake_name, url = fake_url)[0]

        # create a fake access record for this wepage
        acc_rec = AccessRecord.objects.get_or_create(name = webpg, date = fake_date)[0]

if __name__ == '__main__':
    print("Populating script with fake data!")
    populate(10)
    print("Populating completed!")
