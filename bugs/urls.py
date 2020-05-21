from django.urls import path

from . import views

urlpatterns = [
    path("", views.index, name="homepage"),
    path("adduser/", views.adduser_view, name="adduser"),
    path("login/", views.login_view, name="login"),
    path("logout/", views.logout_view, name="logout"),
    path("submitticket/", views.submit_ticket_view, name="submitticket"),
    path("ticket/<slug:slug>/", views.ticket_detail, name="ticket_detail")
]
