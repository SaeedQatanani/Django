from django.shortcuts import render, redirect
import random
from time import strftime

def index(request):
    print(request.session['gold'])
    return render(request, 'index.html')

def process(request):
    if 'gold' not in request.session:
        request.session['gold'] = 0
    if request.POST['gold'] == 'farm':
        request.session['earned_num'] = random.randint(10, 20)
        request.session['gold'] += request.session['earned_num']
        request.session['location'] = request.POST['gold']
        request.session['time'] = strftime("%b %d, %Y" "%I:%M %p")
        request.session['color'] = 'green'
        print(request.session['gold'])
    elif request.POST['gold'] == 'cave':
        request.session['earned_num'] = random.randint(10, 20)
        request.session['gold'] += request.session['earned_num']
        request.session['location'] = request.POST['gold']
        request.session['time'] = strftime("%b %d, %Y" "%I:%M %p")
        request.session['color'] = 'green'
        print(request.session['gold'])
    elif request.POST['gold'] == 'house':
        request.session['earned_num'] = random.randint(10, 20)
        request.session['gold'] += request.session['earned_num']
        request.session['location'] = request.POST['gold']
        request.session['time'] = strftime("%b %d, %Y" "%I:%M %p")
        request.session['color'] = 'green'
        print(request.session['gold'])
    elif request.POST['gold'] == 'quest':
        request.session['earned_num'] = random.randint(-50, 50)
        if request.session['earned_num'] < 0:
            request.session['color'] = 'red'
        elif request.session['earned_num'] > 0:
            request.session['color'] = 'green'
        request.session['gold'] += request.session['earned_num']
        request.session['location'] = request.POST['gold']
        request.session['time'] = strftime("%b %d, %Y" "%I:%M %p")
        print(request.session['gold'])
    return redirect('/')
