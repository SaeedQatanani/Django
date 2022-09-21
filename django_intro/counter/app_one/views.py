from django.shortcuts import render, redirect

def count(request):
    if 'counter' not in request.session:
        request.session['counter'] = 0
    request.session['counter'] += 1
    return render(request, 'index.html')

def destroy(request):
    del request.session['counter']
    return redirect('/')

def addtwice(request):
    request.session['counter'] += 1
    return redirect('/')