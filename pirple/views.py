from django.http import HttpResponse
from django.shortcuts import render

def documentation(request):
    return render(request, "doc.html")
    