from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='home'),
    path('login', views.Login.as_view(), name='login'),
    path('login_detail/<int:pk>', views.LoginDetail.as_view(), name='login_detail'),
    path('register', views.Register.as_view(), name='register'),
    path('logout', views.logout_user, name='logout'),
    path('status', views.status, name='status'),
    path('test_detail/<int:pk>', views.TestDetail.as_view(), name='test_detail'),
]
