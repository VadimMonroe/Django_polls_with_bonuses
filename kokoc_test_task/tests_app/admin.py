from django.contrib import admin
from .models import TestsNames, TestsQuestions, Goods, UsersPoints, TestsAnswers

admin.site.register(TestsNames)
admin.site.register(TestsQuestions)
admin.site.register(TestsAnswers)
admin.site.register(Goods)
admin.site.register(UsersPoints)
