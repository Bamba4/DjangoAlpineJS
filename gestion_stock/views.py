import json
import datetime
from django.http import JsonResponse
from django.shortcuts import render, get_object_or_404
from django.views.decorators.csrf import csrf_exempt
from gestion_stock.models import InitialStock

# Create your views here.
@csrf_exempt
def create_initial_stock(request):
    query = request.POST.get('stockInitial')
    stock_initial = InitialStock.objects.all().first()
    if not stock_initial:
        stock_initial = InitialStock.objects.create(stockInitial=query)
    else:
        stock_initial.stockInitial = query
        stock_initial.deleveredAt = datetime.datetime.now()    
        stock_initial.save()
    return JsonResponse(status=201, data={'stockInitial': stock_initial.stockInitial,
                                            'deleveredAt': stock_initial.deleveredAt,
                                            'id': stock_initial.id}, safe=False)

@csrf_exempt
def delete_stock(request, stock_id):
    stock_initial = get_object_or_404(InitialStock, pk=stock_id)
    stock_initial.delete()
    return JsonResponse(status=204, data={'message': 'Stock initial is successfully deleted'})

def get_stock_initial(request):
    stock_initial = InitialStock.objects.all().first()
    if stock_initial:
        return JsonResponse(status=200, data={'id': stock_initial.id, 'stockInitial': stock_initial.stockInitial, 'deleveredAt': stock_initial.deleveredAt}, safe=False)
    return JsonResponse(status=200, data={}, safe=False)

def index(request):
    return render(request, 'index.html')