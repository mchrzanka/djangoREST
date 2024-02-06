from rest_framework.response import Response
from rest_framework.decorators import api_view
from base.models import Item
from .serializers import ItemSerializer

@api_view(['GET'])
def apiOverview(request):
    api_urls = {
        'List':'/item-list/',
        'Detail View':'/item-detail/',
        'Create':'/item-create/',
        'Update':'/item-update/<str:pk>/',
        'Delete':'/item-delete/<str:pk>/',
    }
    return Response(api_urls)

@api_view(['GET'])
def itemList(request):
    items = Item.objects.all()
    serializer = ItemSerializer(items, many=True)

    return Response(serializer.data)

@api_view(['GET'])
def itemDetail(request, pk):
    item = Item.objects.get(id=pk)
    serializer = ItemSerializer(item, many=False) #false means it will return just one object

    return Response(serializer.data)

@api_view(['POST'])
def itemCreate(request):
    serializer = ItemSerializer(data=request.data)

    if serializer.is_valid():
        serializer.save() #creates a new item in the db
    return Response(serializer.data)

@api_view(['POST'])
def itemUpdate(request, pk):
    item = Item.objects.get(id=pk)
    serializer = ItemSerializer(instance=item, data=request.data) #need to explicitly pass the instance of the item when you want to update

    if serializer.is_valid():
        serializer.save()

    return Response(serializer.data)

@api_view(['DELETE'])
def itemDelete(request,pk):
    item = Item.objects.get(id=pk)
    item.delete()
    return Response('Item successfully deleted!')