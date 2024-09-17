from django.shortcuts import render

# Create your views here.
def EmergenciasReportadas(request):

    return render(request, "emergenciasRecibidas.html")