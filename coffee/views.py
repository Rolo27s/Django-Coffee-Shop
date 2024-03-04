from django.shortcuts import render, redirect
from django.http import HttpResponse, JsonResponse
from coffee.models import Coffee, CartList

def home (request):
    search_string = request.GET.get('search_string', '')
    filtered_coffees = Coffee.objects.filter(name__icontains = search_string) # Similar a LIKE. 'i' es para no case sensitive. 'contains' es como %LIKE%

    return render(request, 'home.html', {'coffee': filtered_coffees})

def add_to_cart(request, coffee_id):
    coffee = Coffee.objects.get(id=coffee_id)
    try:
        cartListItem = CartList.objects.get(coffee = coffee)
    except CartList.DoesNotExist:
        cartListItem = CartList(coffee = coffee, quantity = 0)
        cartListItem.save()

    cartListItem.quantity = cartListItem.quantity + 1
    cartListItem.save()

    return redirect('home')

def cart_list(request):
    cart_list = CartList.objects.all()
    cart_coffees = []
    for item in cart_list:
        cart_coffees.append(item)

    return render(request, 'cartList.html', {'cart_coffees': cart_coffees})

def remove_from_cart(request, cartlist_id):
    cart_list_item = CartList.objects.get(id=cartlist_id)

    if (cart_list_item.quantity > 1):
        cart_list_item.quantity -= 1
        cart_list_item.save()
    else:
        print ("Entras en el else?")
        cart_list_item.delete()

    return redirect('cart_list')