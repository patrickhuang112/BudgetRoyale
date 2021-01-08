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


from rest_framework import viewsets
from .models import Room, User, BudgetSubmission
from .serializers import BudgetSubmissionSerializer, RoomSerializer, UserSerializer

class RoomViewSet(viewsets.ModelViewSet):
    queryset = Room.objects.all()
    serializer_class = RoomSerializer

class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer

class BudgetSubmissionViewSet(viewsets.ModelViewSet):
    queryset = BudgetSubmission.objects.all()
    serializer_class = BudgetSubmissionSerializer