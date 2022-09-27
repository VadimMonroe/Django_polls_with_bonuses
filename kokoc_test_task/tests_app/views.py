from django.contrib.auth import logout, login
from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from django.views.generic import CreateView, DetailView
from django.contrib.auth.views import LoginView
from .forms import RegisterUserForm, LoginUserForm
from .models import *
from .services import get_test_results, save_buy_color_user_info


def index(request):
    tests = TestsNames.objects.all()
    return render(request, 'tests_app/index.html', {'tests_names': tests})


def logout_user(request):
    logout(request)
    return redirect('login')


def status(request):
    users = UsersPoints.objects.all()
    return render(request, 'tests_app/status.html', {'users': users})


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
        user_bonus, user_test = get_test_results(request)
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
        goods = Goods.objects.all()
        users_points = UsersPoints.objects.filter(pk=pk)[0]
        context = {'pk': pk, 'user_points': users_points, 'goods': goods}
        save_buy_color_user_info(request, goods, users_points)
        return render(request, 'tests_app/login_detail.html', context)
