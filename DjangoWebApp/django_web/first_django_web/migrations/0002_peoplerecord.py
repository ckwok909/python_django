# Generated by Django 3.2.6 on 2021-08-14 15:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('first_django_web', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='PeopleRecord',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('First_Name', models.CharField(max_length=255)),
                ('Last_Name', models.CharField(max_length=255)),
                ('Email', models.EmailField(max_length=254)),
            ],
        ),
    ]
