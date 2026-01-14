# autofix/views.py
from django.shortcuts import render
from django.http import HttpResponse

def index(request):
    context = {
        'gallery_range': range(8)  # 0 to 7
    }
    return render(request, 'home.html', context)


def services(request):
    return render(request, 'services.html')

def about(request):
    return render(request, 'about.html')

def gallery(request):
    return render(request, 'gallery.html')

def booking(request):
    return render(request, 'booking.html')

def contact(request):
    return render(request, 'contacts.html')

def booking_submit(request):
    if request.method == "POST":
        name = request.POST.get("name")
        email = request.POST.get("email")
        phone = request.POST.get("phone")
        message = request.POST.get("message")

        # Here you can save to a model or send an email
        print(f"Booking request from {name} ({email}): {message}")

        return render(request, 'booking.html', {'success': True})
    else:
        return render(request, 'booking.html')
