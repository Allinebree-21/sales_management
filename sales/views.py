# Create your views here.

from django.shortcuts import render
from datetime import datetime
from .models import Sale
from .forecast import predict_sales


# 🏠 Homepage view
def home(request):
    return render(request, 'sales/index.html', {
        'year': datetime.now().year
    })


# 📊 Dashboard view
def dashboard(request):
    sales = Sale.objects.all()

    # total sales and profit
    total_sales = sum(s.quantity * s.price for s in sales)
    profit = total_sales * 0.3  # 30% profit margin

    # optional forecast logic
    forecast = predict_sales(sales, periods=30)

    return render(request, 'sales/dashboard.html', {
        'sales': sales,
        'forecast': forecast,
        'total_sales': total_sales,
        'profit': profit,
    })

