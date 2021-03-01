from django.db import models

# Create your models here.

# inherit from the base class models.Model
class Topic(models.Model):
    # unique is a constraint that all topic_names must be unique
    topic_name = models.CharField(max_length=200, unique=True)

    def __str__(self):
        return self.topic_name


class Webpage(models.Model):    
    topic = models.ForeignKey(Topic, on_delete=models.CASCADE)
    name = models.CharField(max_length=200, unique = True)
    url = models.URLField(unique=True)

    def __str__(self):
        return self.name


class AccessRecord(models.Model):
    name = models.ForeignKey(Webpage, on_delete=models.CASCADE)
    date = models.DateField()
    def __str__(self):
        return str(self.date)

class User(models.Model):
    f_name = models.CharField(max_length=20)
    l_name = models.CharField(max_length=20)
    email = models.EmailField(max_length=20, unique=True)

    def __str__(self):
        return "User: {x} {y}".format(x = self.f_name, y = self.l_name)
