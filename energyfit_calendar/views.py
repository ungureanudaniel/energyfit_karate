from django.shortcuts import render, redirect
from django.conf import settings
from services.models import Event

# Create your views here.
def calendar_view(request):
    template="energyfit_calendar/calendar.html"

    context = {
        "events": Event.objects.all().order_by('-event_date')
    }
    return render(request, template, context)