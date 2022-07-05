from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework.serializers import Serializer
from .models import Property
from .models import User
from .serializers import PropertySerializer

# Create your views here.


@api_view(['GET'])
def getRoutes(request):
    routes = [
        {
            'Endpoint': '/properties/',
            'method': 'GET',
            'body': None,
            'description': 'Returns an array of properties'
        },
        {
            'Endpoint': '/properties/id',
            'method': 'GET',
            'body': None,
            'description': 'Returns a single property object'
        },
        {
            'Endpoint': '/properties/category/',
            'method': 'GET',
            'body': {'body': ""},
            'description': 'Returns an array of properties based on category'
        },
        {
            'Endpoint': '/properties/id/update/',
            'method': 'PUT',
            'body': {'body': ""},
            'description': 'Creates an existing property with data sent in post request'
        },
        {
            'Endpoint': '/properties/id/delete/',
            'method': 'DELETE',
            'body': None,
            'description': 'Deletes and exiting property'
        }
    ]
    return Response(routes)


@api_view(['GET'])
def getProperties(request):
    properties = Property.objects.all()
    serializer = PropertySerializer(properties, many=True)
    return Response(serializer.data)


@api_view(['GET'])
def getProperty(request, pk):
    property = Property.objects.get(id=pk)
    serializer = PropertySerializer(property, many=False)
    return Response(serializer.data)


@api_view(['GET'])
def searchProperty(request):
    purpose = request.GET.get('purpose')
    priceMin = request.GET.get('priceMin')
    priceMax = request.GET.get('priceMax')
    rooms = request.GET.get('rooms')
    baths = request.GET.get('baths')
    areaMax = request.GET.get('areaMax')
    properties = Property.objects.all().filter(
        purpose=purpose,
        minPrice__gte=priceMin,
        maxPrice__lte=priceMax,
        rooms__gte=rooms,
        baths__gte=baths,
        area__lte=areaMax,
    )
    serializer = PropertySerializer(properties, many=True)
    return Response(serializer.data)


@api_view(['POST'])
def createProperty(request):
    data = request.data
    property = Property.objects.create(
        title=data['title'],
        purpose=data['purpose'],
        minPrice=data['minPrice'],
        maxPrice=data['maxPrice'],
        area=data['area'],
        baths=data['baths'],
        rooms=data['rooms'],
        body=data['body'],
        images=data['images'],
    )
    serializer = PropertySerializer(property, many=False)
    return Response(serializer.data)
