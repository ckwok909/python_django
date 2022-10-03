import os
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'django_web.settings')

import django
django.setup()

import random
from first_django_web.models import AccessRecord,Webpage,Topic,PeopleRecord
from faker import Faker


fakegen = Faker()
topics = ['Search', 'Social', 'Marketplace', 'News', 'Games']


def add_topic():
    t = Topic.objects.get_or_create(top_name=random.choice(topics))[0]
    t.save
    return t


def populate(n=5):
    for entry in range(n):
        top = add_topic()
        fake_url = fakegen.url()
        fake_date = fakegen.date()
        fake_name = fakegen.company()

        webpg = Webpage.objects.get_or_create(topic=top, url=fake_url, name=fake_name)[0]
        acc_rec = AccessRecord.objects.get_or_create(name=webpg, date=fake_date)[0]


def populate_people(n=5):
    for entry in range(n):
        fake_first = fakegen.first_name()
        fake_last = fakegen.last_name()
        fake_email = fakegen.email()

        pprecords = PeopleRecord.objects.get_or_create(First_Name=fake_first, Last_Name=fake_last, Email=fake_email)[0]


if __name__ == '__main__':
    print("populating script")
    populate_people(20)
    print("finished")
