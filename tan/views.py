from django.shortcuts import render

# Create your views here.

def index(request):
    print('123')
    return render(request,'tan.html')