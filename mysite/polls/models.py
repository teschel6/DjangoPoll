import datetime

from django.db import models
from django.utils import timezone

# Create your models here.
#Models define db schema and constraints
class Question(models.Model):
    question_text = models.CharField(max_length=200)
    pub_date = models.DateTimeField('date published')
    #human readable name is first argument of field instance
    def __str__(self): #used for printing data
        return self.question_text
    def was_published_recently(self): #custom model method
        return self.pub_date >= timezone.now() - datetime.timedelta(days=1)


class Choice(models.Model):
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    choice_text = models.CharField(max_length=200)
    votes= models.IntegerField(default=0)
    def __str__(self): #used for printing data
        return self.choice_text
