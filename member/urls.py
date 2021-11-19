from django.urls import path
from .import views
from .views import UserRegisterView

urlpatterns = [
    path('register', UserRegisterView.as_view(), name='register'),
    path('login', views.login_user, name="login"),
    path('logout', views.logOutPageView, name="logout"),
]