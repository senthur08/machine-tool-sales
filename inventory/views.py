from django.shortcuts import render, redirect
from .models import *
from django.contrib.auth.decorators import login_required
from django.contrib import messages

def home(request):
    if request.method == 'POST':
        query = request.POST.get('search')
        products = Product.objects.filter(name__icontains=query)
        if not products:
            messages.info(request, f'No matching product for {query}')
            return render(request,'inventory/home.html')
        else:
            id=products[0].id 
            return redirect(f'tool/{id}')

    return render(request,'inventory/home.html')

def productList(request):
    products= Product.objects.all()
    context={
        'products':products,
    }
    return render(request, 'inventory/inventory-user.html', context)

def tool(request, pk):
    product= Product.objects.get(id=pk)
    context ={'product':product}
    return render(request, 'inventory/tool.html', context)

@login_required
def order(request, pk):
    product= Product.objects.get(id=pk)
    if request.method == 'POST':
        customer= request.user.customer

        transaction_id = request.POST.get('transaction-id')

        quantity=int(request.POST.get('quantity'))
        total_amount=product.price*quantity

        product.stock_quantity-=quantity
        product.save()

        order=Order.objects.create(customer=customer, transaction_id=transaction_id, total_amount=total_amount)

        OrderItem.objects.create(order=order, product=product, quantity=quantity, price=product.price)
        return redirect( 'user-profile')

    context={'product':product}
    return render(request, 'inventory/place-order.html', context)

@login_required
def purchaseLog(request):
    customer=request.user.customer
    orders=customer.order_set.all()
    context={'orders':orders}
    return render(request, 'inventory/userlog.html', context)