from django.shortcuts import render, redirect
from django.contrib import messages
from .forms import UserRegisterForm
from inventory.models import *
from django.contrib.auth.decorators import login_required

def register(request):
    if request.method == 'POST':
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            user = form.save()  # Save User instance
            address = form.cleaned_data.get('address')
            name = form.cleaned_data['username']
            email = form.cleaned_data['email']
            Customer.objects.create(user=user, address=address, name=name, email = email) 
            username = form.cleaned_data.get('username')
            messages.success(request,f'Welcome {username}')
            return redirect('user-login')

    else:
        form = UserRegisterForm()
    return render(request, 'user/register.html', {'form':form})

@login_required
def profile(request):
    customer = request.user.customer 
    
    # Prefetch orders and related order items and products 
    orders = Order.objects.filter(customer=customer).prefetch_related('orderitem_set__product')

    context={'orders':orders, 'customer':customer}
    return render(request, 'user/profile.html', context)



def aboutus(request):
    return render(request, 'user/aboutus.html')