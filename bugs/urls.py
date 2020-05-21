from django.urls import path

from . import views

urlpatterns = [
    path("", views.index, name="homepage"),
    path("adduser/", views.adduser_view, name="adduser"),
    path("login/", views.login_view, name="login"),
    path("logout/", views.logout_view, name="logout")
]
