from django.shortcuts import render, HttpResponseRedirect, reverse, redirect
from django.contrib.auth import authenticate, login, logout
from bugtracker.settings import AUTH_USER_MODEL
from bugs.forms import AddCustomUser, LoginForm, SubmitTicket
from bugs.models import MyUser, Ticket


def index(request):
    html = "index.html"
    all_tickets = Tickets.objects.get()
    if request.user.is_authenticated:
        return render(request, html, {"all_tickets": all_tickets})
    return redirect("/login/")


def login_view(request):
    if request.method == "POST":
        form = LoginForm(request.POST)
        if form.is_valid():
            data = form.cleaned_data
            user = authenticate(
                request,
                username=data['username'],
                password=data['password']
            )
            if user:
                login(request, user)
                return HttpResponseRedirect(
                    request.GET.get('next', reverse('homepage'))
                )
    form = LoginForm()
    return render(request, "login_form.html", {'form': form})


def logout_view(request):
    logout(request)
    return HttpResponseRedirect(reverse('homepage'))


def adduser_view(request):
    if request.method == "POST":
        form = AddCustomUser(request.POST)
        if form.is_valid():
            data = form.cleaned_data
            MyUser.objects.create(
                username=data['username'],
                password=data['password'],
                display_name=data['display_name'],
                first_name=data['first_name'],
                last_name=data['last_name'],
                email=data['email']
            )
            new_user = MyUser.objects.last()
            new_user.set_password("")
            new_user.save()
            content = "User added successfully"
            return HttpResponseRedirect(
                request.GET.get('next', reverse('homepage')), {'content: content'})
        return render(request, "adduser_form.html", {"form": form})
    if request.user.is_authenticated:
        form = AddCustomUser()
        return render(request, "adduser_form.html", {"form": form})
    return redirect("/login/")

def submit_ticket_view(request):
    if request.method == "POST":
        form = SubmitTicket(request.POST)
        if form.is_valid():
            data = form.cleaned_data
            Ticket.objects.create(
                title=data['title'],
                description=data['description'],
                reported_by=request.user,
                status='N',
            )
            content = "Ticket added successfully"
            return HttpResponseRedirect(
                request.GET.get('next', reverse('homepage')), {'content: content'})
        return render(request, "submit_ticket_form.html", {"form": form})
    if request.user.is_authenticated:
        form = SubmitTicket()
        return render(request, "submit_ticket_form.html", {"form": form})
    return redirect("/login/")