from django.shortcuts import render, redirect
import random
from time import strftime


def index(request):
    request.session['message'] = []
    request.session['gold'] = 0
    return redirect('/gold')


def process(request):
    if 'gold' not in request.session:
        request.session['gold'] = 0

    request.session['location'] = request.POST['gold']
    request.session['time'] = strftime("%b %d, %Y" "%I:%M %p")

    if request.POST['gold'] == 'quest':
        request.session['earned_num'] = random.randint(-50, 50)
        request.session['gold'] += request.session['earned_num']
        if request.session['earned_num'] < 0:
            request.session['message'].insert(0, ['You failed a ' 
                            + request.session['location'] + ' and lost ' 
                            + str(request.session['earned_num']) + ' gold. OUCH!'
                            +'(' + str(request.session['time'])+')', 'red'])
            print(request.session['message'])
        elif request.session['earned_num'] > 0:
            request.session['message'].insert(0, ['You completed a ' 
                            + request.session['location'] + ' and earned ' 
                            + str(request.session['earned_num']) + ' gold. '
                            +'(' + str(request.session['time'])+')', 'green'])

    else:
        request.session['earned_num'] = random.randint(10, 20)
        request.session['gold'] += request.session['earned_num']
        request.session['message'].insert(0, ['You entered a ' + request.session['location'] 
                        + ' and earned ' 
                        + str(request.session['earned_num']) + ' gold. '+'(' 
                        + str(request.session['time'])+')', 'green'])

    return redirect('/gold')


def direction(request):
    return render(request, 'index.html')
