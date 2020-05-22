from django.urls import path

from . import views

urlpatterns = [
    path("", views.index, name="homepage"),
    path("adduser/", views.adduser_view, name="adduser"),
    path("login/", views.login_view, name="login"),
    path("logout/", views.logout_view, name="logout"),
    path("submitticket/", views.submit_ticket_view, name="submitticket"),
    path("editticket/<slug:slug>", views.edit_ticket, name="editticket"),
    path("ticket/<slug:slug>/", views.ticket_detail, name="ticket_detail"),
    path("user/<int:pk>", views.user_detail, name="user_detail"),
    path("assign/<slug:slug>", views.assign, name="assign"),
    path("complete/<slug:slug>", views.complete, name="complete"),
    path("invalidate/<slug:slug>", views.invalidate, name="invalidate"),
]
