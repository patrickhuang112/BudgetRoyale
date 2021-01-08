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



from django.shortcuts import render

from django.http.response import JsonResponse
from rest_framework.parsers import JSONParser 
from rest_framework import status
 
from .models import Room
from .serializers import RoomSerializer
from rest_framework.decorators import api_view


@api_view(['GET', 'POST', 'DELETE'])
def room_list(request):
    if request.method == 'GET':
        rooms = Room.objects.all()
        
        title = request.query_params.get('title', None)
        if title is not None:
            rooms = rooms.filter(title__icontains=title)
        
        rooms_serializer = RoomSerializer(rooms, many=True)
        return JsonResponse(rooms_serializer.data, safe=False)
        # 'safe=False' for objects serialization
 
    elif request.method == 'POST':
        room_data = JSONParser().parse(request)
        room_serializer = RoomSerializer(data=room_data)
        if room_serializer.is_valid():
            room_serializer.save()
            return JsonResponse(room_serializer.data, status=status.HTTP_201_CREATED) 
        return JsonResponse(room_serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    elif request.method == 'DELETE':
        count = Room.objects.all().delete()
        return JsonResponse({'message': '{} Rooms were deleted successfully!'.format(count[0])}, status=status.HTTP_204_NO_CONTENT)
 
 
@api_view(['GET', 'PUT', 'DELETE'])
def room_detail(request, pk):
    try: 
        room = Room.objects.get(pk=pk) 
    except Room.DoesNotExist: 
        return JsonResponse({'message': 'The room does not exist'}, status=status.HTTP_404_NOT_FOUND) 
 
    if request.method == 'GET': 
        room_serializer = RoomSerializer(room) 
        return JsonResponse(room_serializer.data) 
 
    elif request.method == 'PUT': 
        room_data = JSONParser().parse(request) 
        room_serializer = RoomSerializer(room, data=room_data) 
        if room_serializer.is_valid(): 
            room_serializer.save() 
            return JsonResponse(room_serializer.data) 
        return JsonResponse(room_serializer.errors, status=status.HTTP_400_BAD_REQUEST) 
 
    elif request.method == 'DELETE': 
        room.delete() 
        return JsonResponse({'message': 'Room was deleted successfully!'}, status=status.HTTP_204_NO_CONTENT)
    
        
@api_view(['GET'])
def room_list_published(request):
    rooms = Room.objects.filter(published=True)
        
    if request.method == 'GET': 
        rooms_serializer = RoomSerializer(rooms, many=True)
        return JsonResponse(rooms_serializer.data, safe=False)

@api_view(['GET', 'POST', 'DELETE'])
def room_list(request):
    if request.method == 'GET':
        rooms = Room.objects.all()
        
        title = request.query_params.get('title', None)
        if title is not None:
            rooms = rooms.filter(title__icontains=title)
        
        rooms_serializer = RoomSerializer(rooms, many=True)
        return JsonResponse(rooms_serializer.data, safe=False)
        # 'safe=False' for objects serialization
 
    elif request.method == 'POST':
        room_data = JSONParser().parse(request)
        room_serializer = RoomSerializer(data=room_data)
        if room_serializer.is_valid():
            room_serializer.save()
            return JsonResponse(room_serializer.data, status=status.HTTP_201_CREATED) 
        return JsonResponse(room_serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    elif request.method == 'DELETE':
        count = Room.objects.all().delete()
        return JsonResponse({'message': '{} Rooms were deleted successfully!'.format(count[0])}, status=status.HTTP_204_NO_CONTENT)
 
 
@api_view(['GET', 'PUT', 'DELETE'])
def room_detail(request, pk):
    try: 
        room = Room.objects.get(pk=pk) 
    except Room.DoesNotExist: 
        return JsonResponse({'message': 'The room does not exist'}, status=status.HTTP_404_NOT_FOUND) 
 
    if request.method == 'GET': 
        room_serializer = RoomSerializer(room) 
        return JsonResponse(room_serializer.data) 
 
    elif request.method == 'PUT': 
        room_data = JSONParser().parse(request) 
        room_serializer = RoomSerializer(room, data=room_data) 
        if room_serializer.is_valid(): 
            room_serializer.save() 
            return JsonResponse(room_serializer.data) 
        return JsonResponse(room_serializer.errors, status=status.HTTP_400_BAD_REQUEST) 
 
    elif request.method == 'DELETE': 
        room.delete() 
        return JsonResponse({'message': 'Room was deleted successfully!'}, status=status.HTTP_204_NO_CONTENT)
    
        
@api_view(['GET'])
def room_list_published(request):
    rooms = Room.objects.filter(published=True)
        
    if request.method == 'GET': 
        rooms_serializer = RoomSerializer(rooms, many=True)
        return JsonResponse(rooms_serializer.data, safe=False)