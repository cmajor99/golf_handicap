from django.http import HttpResponse
from django.shortcuts import render


def roundEntry(request):
    #return HttpResponse("Here is where you enter scores")
    return render(request, 'homepage.html')
