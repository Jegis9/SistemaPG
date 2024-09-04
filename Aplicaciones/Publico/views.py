from django.shortcuts import render, redirect


# Create your views here.
def reportEmergency(request):
    return render(request, 'reportEmergency.html')


