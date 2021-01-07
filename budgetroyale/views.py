from django.shortcuts import render

# Create your views here.
def index(request):
    return render(request, 'index.html')

def submit(request):
    return render(request, 'submit.html')

def judge(request):
    return render(request, 'judge.html')
