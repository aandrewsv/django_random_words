from django.shortcuts import redirect, render
from django.utils.crypto import get_random_string

def index(request):
    return redirect("/random_word")

def random_word(request):
    if 'counter' not in request.session:
        request.session['counter'] = 0
    if 'word' not in request.session:
        request.session['word'] = get_random_string(length=14)
    return render(request, "index.html")

def generate(request):
    request.session['word'] = get_random_string(length=14)
    request.session['counter'] += 1
    return redirect ("/")

def reset(request):
    del request.session['word']
    del request.session['counter']
    return redirect("/")
