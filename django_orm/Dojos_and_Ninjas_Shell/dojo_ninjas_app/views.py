from multiprocessing import context
from django.shortcuts import render, redirect
from .models import Dojo, Ninja

def index(request):
    context = {
        'dojos':Dojo.objects.all(),
    }
    return render(request, 'index.html', context)

def add_dojo(request):
    Dojo.objects.create(name = request.POST['name'],
                        city = request.POST['city'],
                        state = request.POST['state'],
                        desc = 'An avaialble dojo')
    return redirect('/')

def add_ninja(request):
    dojo_id=request.POST['dojo_in_ninja']
    Ninja.objects.create(first_name = request.POST['first_name'],
                        last_name = request.POST['last_name'],
                        dojo = Dojo.objects.get(id = dojo_id))
    return redirect('/')