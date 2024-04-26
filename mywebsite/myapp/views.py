from django.shortcuts import render, redirect
from .models import Product

def home(request):
    products = Product.objects.filter(is_available=True)
    return render(request, 'myapp/home.html', {'products': products})

def buy_product(request, product_id):
    product = Product.objects.get(pk=product_id)
    if request.method == 'POST':
        # Process the purchase
        product.is_available = False
        product.save()
        return redirect('home')
    return render(request, 'myapp/buy_product.html', {'product': product})

def sell_product(request):
    if request.method == 'POST':
        # Process the sale
        name = request.POST['name']
        description = request.POST['description']
        price = request.POST['price']
        Product.objects.create(name=name, description=description, price=price)
        return redirect('home')
    return render(request, 'myapp/sell_product.html')
