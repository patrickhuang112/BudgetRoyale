from django.shortcuts import render

# Create your views here.
def index(request):
    return render(request, 'index.html')

def room(request, *args, **kwargs):
    if request.GET.get('create'):
        print('user clicked create')

    return render(request, 'room.html');