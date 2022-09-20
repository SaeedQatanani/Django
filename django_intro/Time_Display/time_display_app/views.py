from django.shortcuts import render, redirect
from time import gmtime, strftime

def index(request):
    context = {
        "date": strftime("%b %d, %Y"),
        "time": strftime("%I:%M:%S %p")
    }
    return render(request,'index.html', context)

def redirect_fun(request):
    return redirect('/')
