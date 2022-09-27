from multiprocessing import context
import re
from django.shortcuts import render, redirect
from .models import Show

def add(request):
    return render(request, 'add_new.html')

def create(request):
    Show.objects.create(title = request.POST['title'],
                        network = request.POST['network'],
                        release_date = request.POST['release_date'],
                        description = request.POST['description']
                        )
    new_show_id = Show.objects.get(title = request.POST['title']).id
    return redirect(f'/shows/{new_show_id}')

def show(request, id):
    context = {
        'show' : Show.objects.get(id = id),
    }
    return render(request, 'show.html', context)

def display_all(request):
    context = {
        'shows' : Show.objects.all()
    }
    return render(request, 'all.html', context)

def edit(request, id):
    context = {
        'id': id
    }
    return render(request, 'edit.html', context)

def update(request, id):
    this_show = Show.objects.get(id = id)
    this_show.title = request.POST['title']
    this_show.network = request.POST['network']
    this_show.release_date = request.POST['release_date']
    this_show.description = request.POST['description']
    this_show.save()
    this_show_id = this_show.id
    return redirect(f'/shows/{this_show_id}')

def delete(request, id):
    this_show = Show.objects.get(id = id)
    this_show.delete()
    return redirect('/shows/')

def main(request):
    return redirect('/shows/')
