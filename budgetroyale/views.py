from django.shortcuts import render
from .models import User, BudgetSubmission, Room
# Create your views here.
def index(request):
    return render(request, 'index.html')

def judge(request):
    return render(request, 'judge.html')

def room(request):
    return render(request, 'room.html')

def submit(request):

    return render(request, 'submit.html')