from django.shortcuts import render
from rest_framework import status
from rest_framework.response import Response
from .models import *
from rest_framework.decorators import api_view
from .serializers import *
# Create your views here.

def purchase_list(request):
    purchases = Purchase.objects.all()
    context = {'purchases':purchases}
    return render(request,'purchase.html',context)

@api_view(['GET'])
def purchaseList(request):
    purchases = Purchase.objects.all()
    serializer = PurchaseSerializer(purchases,many=True)
    return Response(serializer.data)

# @api_view(['POST'])
# def purchaseCreate(request):
#     serializer = PurchaseSerializer(data=request.data)
#     if serializer.is_valid():
#         serializer.save()
#     return Response(serializer.data)

#
# @api_view(['GET'])
# def purchaseDetailList(request,pk):
#     purchase = Purchase.objects.get(id=pk)
#     serializer = PurchaseSerializer(purchase,many=False)
#     return Response(serializer.data)
#
# @api_view(['POST'])
# def purchaseUpdate(request,pk):
#     purchase = Purchase.objects.get(id=pk)
#     serializer = PurchaseSerializer(instance=purchase,data=request.data,many=False)
#     if serializer.is_valid():
#         serializer.save()
#     return Response(serializer.data)
#
# @api_view(['POST'])
# def purchaseDelete(request,pk):
#     purchase = Purchase.objects.get(id=pk)
#     serializer = PurchaseSerializer(instance=purchase,data=request.data,many=False)
#     if serializer.is_valid():
#         purchase.delete()
#     return Response(serializer.data)

@api_view(['GET'])
def purchaseFilterList(request):
    purchases = Purchase.objects.filter(status=True)
    serializer = PurchaseSerializer(purchases, many=True)
    return Response(serializer.data)

@api_view(['PUT'])
def purchaseUpdate(request,pk):
    try:
        purchase = Purchase.objects.get(id=pk)
    except Purchase.DoesNotExist:
        return Response({'data': 'not found page'}, status=status.HTTP_404_NOT_FOUND)

    if request.method == 'PUT':
        serializer = PurchaseSerializer(purchase, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({'SERVER RESPONSE':'PURCHASE successfuly updated'},status=status.HTTP_200_OK)

@api_view(['DELETE'])
def purhaseDelete(request,pk):
    try:
        purchase = Purchase.objects.get(id=pk)
    except Purchase.DoesNotExist:
        return Response({'SERVER RESPONSE':'page not found'},status=status.HTTP_404_NOT_FOUND)

    if request.method == 'DELETE':
        purchase.delete()
        return Response({'SERVER RESPONSE': 'PURCHASE successfuly deleted'},status=status.HTTP_200_OK)

@api_view(['POST'])
def purchaseCreate(request,pk):
    account = Account.objects.get(id=pk)
    purchase = Purchase(customer=account)
    if request.method == 'POST':
        serializer = PurchaseSerializer(purchase,data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data,status=status.HTTP_201_CREATED)
        else:
            return Response(serializer.errors)


@api_view(['POST'])
def accounRegister(request):
    if request.method == 'POST':
        serializer = AccountSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data,status.HTTP_201_CREATED)
        else:
            return Response(serializer.errors,status.HTTP_400_BAD_REQUEST)