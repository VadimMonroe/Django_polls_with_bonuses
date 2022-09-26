from django.db import models
from django.contrib.auth.models import User


class TestsNames(models.Model):
    test_name = models.CharField('Наименование теста', max_length=1000)

    # test_questions = models.ForeignKey(TestsQuestions, on_delete=models.CASCADE)

    def __str__(self):
        return self.test_name

    class Meta:
        verbose_name = 'Опрос'
        verbose_name_plural = 'Опросы'
        db_table = 'TestsNames'


class TestsQuestions(models.Model):
    test_name = models.ForeignKey(TestsNames, on_delete=models.CASCADE)
    question = models.CharField('Вопрос', max_length=1000)
    right_answer = models.CharField('Правильный ответ', max_length=500)

    def __str__(self):
        return self.question

    class Meta:
        verbose_name = 'Вопрос'
        verbose_name_plural = 'Вопросы'
        db_table = 'TestQuestions'


class TestsAnswers(models.Model):
    test_name = models.ForeignKey(TestsQuestions, on_delete=models.CASCADE)
    answer = models.CharField('Ответ', max_length=1000)
    bonus = models.IntegerField('Цена начисления за правильный ответ')

    def __str__(self):
        return self.answer

    class Meta:
        verbose_name = 'Ответ'
        verbose_name_plural = 'Ответы'
        db_table = 'TestAnswers'


class Goods(models.Model):
    name = models.CharField('Наименование услуги', max_length=50)
    color = models.CharField('Значение цвета', max_length=50)
    price = models.IntegerField('Цена покупки услуги')

    def __str__(self):
        return f'{self.name} | {self.color} | {self.price}'

    class Meta:
        verbose_name = 'Услуга сайта'
        verbose_name_plural = 'Услуги сайта'
        db_table = 'Goods'


class UsersPoints(models.Model):
    login = models.ForeignKey(User, on_delete=models.CASCADE)
    color = models.CharField('Цвет фона', max_length=50)
    points = models.IntegerField('Баллы')
    done_tests = models.CharField('Пройденные тесты', max_length=1000)

    def __str__(self):
        return f'{self.login.username} | {self.color} | {self.points}'

    class Meta:
        verbose_name = 'Баллы пользователя'
        verbose_name_plural = 'Баллы пользователей'
        db_table = 'Users'
