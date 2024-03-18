from django.shortcuts import render, redirect

# Create your views here.
def slideShow(request):
    return render(request, 'slideShow.html')