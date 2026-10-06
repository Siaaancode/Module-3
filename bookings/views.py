from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse

# Create your views here.

def index(request):
    return render(request, 'index.html')

def menu(request):
    return render(request, "menu.html")

def signup(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)

        if form.is_valid():
            form.save()
            messages.success(
                request,
                'Your account has been created successfully.'
            )
            return redirect('login')
    else:
        form = UserCreationForm()

    return render(request, 'signup.html', {'form': form})

@login_required
def create_booking(request):
    # Booking form and booking logic
    if request.method == "POST":
        booking_date = request.POST.get("booking_date")

        print(booking_date)
    return render(request, "booking.html")

