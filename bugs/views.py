from django.shortcuts import render, HttpResponseRedirect, reverse, redirect
from django.contrib.auth import authenticate, login, logout
from datetime import datetime
from bugtracker.settings import AUTH_USER_MODEL
from bugs.forms import AddCustomUser, LoginForm, SubmitTicket
from bugs.models import MyUser, Ticket

# order by method found at https://stackoverflow.com/questions/2272370/sortable-table-columns-in-django/2272420#2272420
def index(request):
    html = "index.html"
    filter_by = request.GET.get('filter_by', 'all')
    print(filter_by)
    if filter_by == "all":
        tickets = Ticket.objects.all()
    else:
        tickets = Ticket.objects.all().filter(status=filter_by)
    order_by = request.GET.get('order_by', '-status')
    tickets = tickets.exclude(status="Invalid").order_by(order_by)
    users = MyUser.objects.all()
    if request.user.is_authenticated:
        return render(request, html, {"tickets": tickets, "order_by": order_by, "users": users})
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
            new_user.set_password(raw_password=data['password'])
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
                status='New',
            )
            content = "Ticket added successfully"
            return HttpResponseRedirect(
                request.GET.get('next', reverse('homepage')), {'content: content'})
        return render(request, "submit_ticket_form.html", {"form": form})
    if request.user.is_authenticated:
        form = SubmitTicket()
        return render(request, "submit_ticket_form.html", {"form": form})
    return redirect("/login/")


def ticket_detail(request, slug):
    if request.user.is_authenticated:
        ticket = Ticket.objects.get(slug=slug)
        return render(request, "ticket_detail.html", {"ticket": ticket})
    return redirect("/login/")


def user_detail(request, pk):
    if request.user.is_authenticated:
        user = MyUser.objects.get(pk=pk)
        completed_tickets = Ticket.objects.filter(completed_by=user)
        assigned_tickets = Ticket.objects.filter(assigned_to=user)
        authored_tickets = Ticket.objects.filter(reported_by=user)
        return render(request, "user_detail.html", {
            "user": user, 
            "completed_tickets": completed_tickets,
            "assigned_tickets": assigned_tickets,
            "authored_tickets": authored_tickets
            })


def edit_ticket(request, slug):
    if request.user.is_authenticated:
        if request.method == "POST":
            form = SubmitTicket(request.POST)
            if form.is_valid():
                data = form.cleaned_data
                print(data)
                ticket = Ticket.objects.get(slug=slug)
                ticket.title = data['title']
                ticket.description = data['description']
                ticket.save()
                return HttpResponseRedirect(
                            request.GET.get('next', reverse('homepage'))
                        )
        form = SubmitTicket()
        return render(request, "submit_ticket_form.html", {"form": form})
    return redirect("/login/")


def assign(request, slug):
    if request.user.is_authenticated:
        ticket = Ticket.objects.get(slug=slug)
        ticket.assigned_to = request.user
        ticket.status = "In Process"
        ticket.save()
        return HttpResponseRedirect(
                    request.GET.get('next', reverse('homepage'))
                )
    return redirect("/login/")


def complete(request, slug):
    if request.user.is_authenticated:
        ticket = Ticket.objects.get(slug=slug)
        ticket.assigned_to = None
        ticket.completed_by = request.user
        ticket.completed_date = datetime.now()
        ticket.status = "Done"
        ticket.save()
        return HttpResponseRedirect(
                    request.GET.get('next', reverse('homepage'))
                )
    return redirect("/login/")


def invalidate(request, slug):
    if request.user.is_authenticated:
        ticket = Ticket.objects.get(slug=slug)
        ticket.assigned_to = None
        ticket.completed_by = None
        ticket.status = "Invalid"
        ticket.save()
        return HttpResponseRedirect(
                    request.GET.get('next', reverse('homepage'))
                )
    return redirect("/login/")
