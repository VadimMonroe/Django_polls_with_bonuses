from django.contrib import admin
from .models import TestsNames, TestsQuestions, Goods, UsersPoints, TestsAnswers


@admin.register(UsersPoints)
class UsersPointsAdmin(admin.ModelAdmin):
    """Настройка Пользовательских опций"""

    list_display = ("id", "login", "color", "points", "done_tests")
    list_display_links = ("login",)
    readonly_fields = ("done_tests",)


@admin.register(Goods)
class GoodsAdmin(admin.ModelAdmin):
    list_display = ("id", "name", "color", "price")
    list_display_links = ("name",)


@admin.register(TestsAnswers)
class TestsAnswersAdmin(admin.ModelAdmin):
    list_display = ("id", "test_name", "answer", "bonus")
    list_display_links = ("test_name",)
    list_filter = ("test_name",)


class AnswersInline(admin.TabularInline):
    model = TestsAnswers
    extra = 1


@admin.register(TestsQuestions)
class TestsQuestionsAdmin(admin.ModelAdmin):
    """Настройка Вопросов в Админке"""

    list_display = ("id", "test_name", "question", "right_answer")
    list_display_links = ("test_name",)
    list_filter = ("test_name",)
    inlines = [AnswersInline]
    list_editable = ("question", "right_answer")


class QuestionsInline(admin.TabularInline):
    model = TestsQuestions
    extra = 1


@admin.register(TestsNames)
class TestsNamesAdmin(admin.ModelAdmin):
    """Настройка Опросов в Админке"""

    list_display = ("id", "test_name",)
    list_display_links = ("test_name",)
    inlines = [QuestionsInline]
