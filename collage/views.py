from django.shortcuts import render
from .models import GetCarImage
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .serializers import CarImageSerializer
# Create your views here.


    


def Home(request):
    car_images = GetCarImage.objects.all()
    return render(request, 'home.html', {'car_images': car_images})


@api_view(['POST'])
def addItem(request):
    serializer = CarImageSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status=201)
    return Response(serializer.errors, status=400)

