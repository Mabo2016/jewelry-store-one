from django.shortcuts import render
import datetime

def index(request):
    date_today = datetime.datetime.now()

    context = {
        'date_today': date_today,
    }

    return render(request, "index.html", context = context)
