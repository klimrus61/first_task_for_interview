from django.db import models
from django.contrib.auth.models import User
from webquiz import settings


class CollectionQuestions(models.Model):
    '''Набор вопросов'''
    title = models.CharField(max_length=1024)
    


class Question(models.Model):
    '''1 вопрос из набора'''
    title = models.CharField(max_length=4096)
    visible = models.BooleanField(default=False)
    max_points = models.FloatField()
    collection_question = models.ForeignKey(CollectionQuestions, on_delete=models.DO_NOTHING)

    def __str__(self):
           return self.title

class Choice(models.Model):
    '''Вариант выбора к вопросу'''
    question = models.ForeignKey(Question, on_delete=models.DO_NOTHING)
    title = models.CharField(max_length=4096)
    points = models.FloatField()
    lock_other = models.BooleanField(default=False)

    def __str__(self):
        return self.title


class Answer(models.Model):
    '''Ответ пользователя'''
    user = models.ForeignKey(User, on_delete=models.DO_NOTHING)
    question = models.ForeignKey(Question, on_delete=models.DO_NOTHING)
    choice = models.ForeignKey(Choice, on_delete=models.DO_NOTHING)
    created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.choice.title

