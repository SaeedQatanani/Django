from django.shortcuts import render, HttpResponse, redirect
import random

def index(request):
    if 'rand_num' not in request.session:
        request.session['rand_num'] = random.randint(1, 100)
    print(request.session['rand_num'])

    return render(request, 'index.html')

def random_number(request):
    request.session['space'] = request.POST['space']
    if int(request.session['space']) == int(request.session['rand_num']):
        request.session['value'] = 'equal'
        del request.session['rand_num']
        
    elif int(request.session['space']) > int(request.session['rand_num']):
        request.session['value'] = 'higher'
    elif int(request.session['space']) < int(request.session['rand_num']):
        request.session['value'] = 'lower'
    return redirect('/path')

def redirect_route(request):
    return redirect('/')

def again(request):
    del request.session['space']
    return redirect('/')