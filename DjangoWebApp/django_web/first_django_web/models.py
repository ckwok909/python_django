from django.db import models


# Create your models here.
class Topic(models.Model):
    top_name = models.CharField(max_length=255, unique=True)

    def __str__(self):
        return self.top_name


class Webpage(models.Model):
    topic = models.ForeignKey('Topic', on_delete=models.CASCADE,)
    name = models.CharField(max_length=255, unique=True)
    url = models.URLField(unique=True)

    def __str__(self):
        return self.name


class AccessRecord(models.Model):
    name = models.ForeignKey('Webpage', on_delete=models.CASCADE,)
    date = models.DateField()

    def __str__(self):
        return str(self.date)


class PeopleRecord(models.Model):
    First_Name = models.CharField(max_length=255, unique=False)
    Last_Name = models.CharField(max_length=255, unique=False)
    Email = models.EmailField()

    def __str__(self):
        return self.First_Name
