from django.shortcuts import render, redirect
from .forms import TicketForm
from .models import Ticket
from .utils import classify_ticket

def create_ticket(request):
    if request.method == "POST":
        form = TicketForm(request.POST)
        if form.is_valid():
            ticket = form.save(commit=False)
            category, priority = classify_ticket(ticket.description)
            ticket.category = category
            ticket.priority = priority
            ticket.save()
            return redirect("ticket_list")
    else:
        form = TicketForm()
    return render(request, "tickets/create_ticket.html", {"form": form})

def ticket_list(request):
    tickets = Ticket.objects.order_by("-created_at")
    return render(request, "tickets/ticket_list.html", {"tickets": tickets})
