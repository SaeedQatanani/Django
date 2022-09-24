from django.shortcuts import render, redirect
import random

def index(request):
    if 'rand_num' not in request.session:
        request.session['rand_num'] = random.randint(1, 100)
    print(request.session['rand_num'])
    return render(request, 'index.html')

def compare_numbers(request):
    request.session['space'] = request.POST['space']
    if int(request.session['space']) == int(request.session['rand_num']):
        request.session['value'] = 'equal'
    elif int(request.session['space']) > int(request.session['rand_num']):
        request.session['value'] = 'higher'
    elif int(request.session['space']) < int(request.session['rand_num']):
        request.session['value'] = 'lower'
    return redirect('/path')

def redirect_route(request):
    return redirect('/')

def again(request):
    del request.session['rand_num']
    del request.session['space']
    return redirect('/')