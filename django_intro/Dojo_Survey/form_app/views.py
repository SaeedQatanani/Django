from django.shortcuts import render, redirect

def index(request):
    return render(request, 'index.html')

def process(request):
    request.session['name'] = request.POST['name']
    request.session['location'] = request.POST['location']
    request.session['language'] = request.POST['language']
    request.session['comment'] = request.POST['comment']
    return redirect('/final_result')

def show(request):    
    return render(request, 'result.html')



