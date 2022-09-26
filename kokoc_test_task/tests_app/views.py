from django.contrib.auth import logout, login
from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from django.views import View
from django.views.generic import CreateView, DetailView
from django.contrib.auth.views import LoginView
from .forms import RegisterUserForm, LoginUserForm
from .models import *


class Index(View):
    """Выдаём все тесты на сайт"""

    def get(self, request):
        tests = TestsNames.objects.all()
        context = {'tests_names': tests}
        return render(request, 'tests_app/index.html', context)


def logout_user(request):
    logout(request)
    return redirect('login')


def status(request):
    users = UsersPoints.objects.all()
    context = {'users': users}
    return render(request, 'tests_app/status.html', context)


class Register(CreateView):
    form_class = RegisterUserForm
    template_name = 'tests_app/register.html'
    success_url = reverse_lazy('login')

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        return context

    def form_valid(self, form):
        user = form.save()
        user_points = UsersPoints.objects.all()
        user_points.create(id=user.id, login=user, color='white', points=0)

        login(self.request, user)
        return redirect('home')


class Login(LoginView):
    form_class = LoginUserForm
    template_name = 'tests_app/login.html'

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        return context

    def get_success_url(self):
        return reverse_lazy('home')


class TestDetail(DetailView):
    """Отдельная страница для каждого опроса"""

    def get(self, request, pk=None):
        questions = TestsQuestions.objects.all()
        answers = TestsAnswers.objects.all()
        context = {'pk': pk, 'test_questions': questions, 'answers': answers}
        return render(request, 'tests_app/test_detail.html', context)

    def post(self, request, pk=None):
        all_answers_list = []
        [all_answers_list.append(i) for i in request.POST.values()]

        user_bonus = 0
        user_test = None
        user_inner = None
        for bonus in all_answers_list[1:]:
            bonus = bonus.split('|')
            print(bonus, bonus[0])
            user_bonus += int(bonus[0])
            if not user_test:
                user_test = bonus[1]
            if not user_inner:
                user_inner = bonus[2]

        user = UsersPoints.objects.get(login=user_inner)
        user.points += user_bonus

        if user.done_tests == '0':
            user.done_tests = user_test
        else:
            if user_test not in user.done_tests:
                user.done_tests += user_test
        user.save()
        # questions = TestsQuestions.objects.all()
        context = {'user_bonus': user_bonus, 'user_test': user_test}
        return render(request, 'tests_app/test_done.html', context)


class LoginDetail(DetailView):
    """Личный кабинет каждого пользователя"""

    def get(self, request, pk=None):
        goods = Goods.objects.all()
        users_points = UsersPoints.objects.filter(pk=pk)[0]
        context = {'pk': pk, 'user_points': users_points, 'goods': goods}
        return render(request, 'tests_app/login_detail.html', context)

    def post(self, request, pk=None):
        purchased_color = request.POST.get('shop');
        goods = Goods.objects.all()
        users_points = UsersPoints.objects.filter(pk=pk)[0]
        context = {'pk': pk, 'user_points': users_points, 'goods': goods}

        tapped_good = goods.get(name=purchased_color)
        print(users_points.points, tapped_good.price)
        if users_points.color != purchased_color:
            if users_points.points - tapped_good.price >= 0:
                users_points.points = users_points.points - tapped_good.price
                users_points.color = purchased_color
        users_points.save()
        return render(request, 'tests_app/login_detail.html', context)
