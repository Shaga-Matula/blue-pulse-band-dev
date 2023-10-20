from django.shortcuts import render

# Create your views here.

def index(request):
    return render(request, 'home/index.html')


def musicapp(request):
    return render(request, 'musicapp/musicapp.html')
