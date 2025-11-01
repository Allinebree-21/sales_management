# Create your views here.

from django.shortcuts import render
from .models import Sale
from .forecast import predict_sales

def dashboard(request):
    sales = Sale.objects.all()

    total_sales = sum(s.quantity * s.price for s in sales)
    profit = total_sales * 0.3  # assuming 30% profit margin

    forecast = predict_sales(sales, periods=30)

    return render(request, 'sales/dashboard.html', {
        'sales': sales,
        'forecast': forecast,
        'total_sales': total_sales,
        'profit': profit,
    })
