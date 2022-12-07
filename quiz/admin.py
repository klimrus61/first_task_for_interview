from django.contrib import admin
from .models import CollectionQuestions, Question, Choice, Answer


admin.site.register(CollectionQuestions)
admin.site.register(Question)
admin.site.register(Choice)
admin.site.register(Answer)
