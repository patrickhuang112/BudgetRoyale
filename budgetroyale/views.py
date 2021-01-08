from django.shortcuts import render
from .models import User, BudgetSubmission, Room
# Create your views here.
def index(request):
    if request.method == "POST":
        return render(request, 'room.html')
    return render(request, 'index.html')

def judge(request):
    return render(request, 'judge.html')

def room(request):
    if(request.method == "get"):
        #arham got this part, set up urls already
        return render(request, 'room.html')

def submit(request):
    if(request.method == "post"):

        return render(request, 'submit.html')



