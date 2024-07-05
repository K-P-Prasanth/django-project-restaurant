
import json
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.db import IntegrityError
from django.http import JsonResponse
from django.shortcuts import HttpResponse, HttpResponseRedirect, render
from django.urls import reverse
from django.views.decorators.csrf import csrf_exempt

from .models import User,Item,Order,Sale,Category
# Create your views here.

def index(request):
    return render(request, "restaurant/index.html",{
    })

def login_view(request):
    if request.method == "POST":

        # Attempt to sign user in
        username = request.POST["username"]
        password = request.POST["password"]
        user = authenticate(request, username=username, password=password)

        # Check if authentication successful
        if user is not None:
            login(request, user)
            return HttpResponseRedirect(reverse("index"))
        else:
            return render(request, "restaurant/login.html", {
                "message": "Invalid username and/or password."
            })
    else:
        return render(request, "restaurant/login.html")


def logout_view(request):
    logout(request)
    return HttpResponseRedirect(reverse("index"))


def register(request):
    if request.method == "POST":
        username = request.POST["username"]
        email = request.POST["email"]

        # Ensure password matches confirmation
        password = request.POST["password"]
        confirmation = request.POST["confirmation"]
        if password != confirmation:
            return render(request, "restaurant/register.html", {
                "message": "Passwords must match."
            })

        # Attempt to create new user
        try:
            user = User.objects.create_user(username, email, password)
            user.save()
        except IntegrityError:
            return render(request, "restaurant/register.html", {
                "message": "Username already taken."
            })
        login(request, user)
        Order.objects.create(user=request.user)
        return HttpResponseRedirect(reverse("index"))
    else:
        return render(request, "restaurant/register.html")


def menu(request):
    return render(request,"restaurant/menu.html",{
        "categories":Category.objects.all()
    })   

def allorders(request):
    orders = Order.objects.all()
    return render(request, "restaurant/allorders.html", {
        "orders": orders
        })

def myorders(request):
    order = Order.objects.filter(user=request.user)
    return render(request,"restaurant/myorder.html",{
        "orders":order
    })

def add(request):
    if request.method == "POST":
        name = request.POST["name"]
        price = request.POST["price"]
        imageURL = request.POST["imageURL"]
        vegBool = request.POST["vegBool"]
        rating = request.POST["rating"]
        category = request.POST["category"]
        category = Category.objects.get(pk=category)
        item = Item(name=name, price=price, imageURL=imageURL, vegBool=vegBool,rating=rating,category=category)
        item.save()
        return HttpResponseRedirect(reverse("index"))
    else:
        return render(request, "restaurant/add.html",{
            "categories":Category.objects.all()
        })



# API's 
@login_required
def menu_categories(request,category_name):
    category = Category.objects.filter(name = category_name)
    all_items = Item.objects.filter(category=category[0])
    all_items = all_items.order_by("name").all()
    return JsonResponse([item.serialize() for item in all_items], safe=False)


@login_required
def orders(request):
    all_orders = Order.objects.all()
    all_orders = all_orders.order_by("timestamp").all()
    return JsonResponse([order.serialize() for order in all_orders], safe=False)


@csrf_exempt
def a_order(request,order_id):
    all_orders = Order.objects.filter(pk=order_id)
    all_orders = all_orders.order_by("timestamp").all()
    if request.method == "GET":
        return JsonResponse([order.serialize() for order in all_orders], safe=False)
    
    elif request.method == "POST":
        order_id = request.POST["order_id"]
        order = Order.objects.get(pk=order_id)
        Order.objects.filter(pk=order_id).update(total=0)
        items = order.items.all()
        for item in items:
            Sale.objects.filter(user=item.user,item=item.item).update(quantity=0)
        
        return HttpResponseRedirect(reverse("allorders")) 
    

@csrf_exempt
def cancleorder(request):
    if request.method == "POST":
        order_id = request.POST["order_id"]
        order = Order.objects.get(pk=order_id)
        Order.objects.filter(pk=order_id).update(total=0)
        items = order.items.all()
        for item in items:
            Sale.objects.filter(user=item.user,item=item.item).update(quantity=0)
        
        return HttpResponseRedirect(reverse("index")) 

    


@login_required
def allitems(request):
    all_items = Item.objects.all()
    all_items = all_items.order_by("name").all()
    return JsonResponse([item.serialize() for item in all_items], safe=False)

@login_required
def a_item(request,item_id):
    all_items = Item.objects.filter(pk=item_id)
    all_items = all_items.order_by("name").all()
    return JsonResponse([item.serialize() for item in all_items], safe=False)




@csrf_exempt
def add_item(request):
    if request.method == "POST":
        quantity = int(request.POST["quantity"])
        item_id = request.POST["item_id"]
        value = int(request.POST["amt"])
        item = Item.objects.get(pk=item_id)
        ord = Order.objects.filter(user=request.user)
        tot = int(ord[0].total)
        
        Sale.objects.get_or_create(user=request.user,item=item)
        sale = Sale.objects.filter(user=request.user,item=item)
        q = sale[0].quantity+quantity
        Sale.objects.filter(user=request.user,item=item).update(quantity=q)
        
        
        order = Order.objects.get(user=request.user)
        order.items.add(Sale.objects.get(item=item,user=request.user))
        order.save()
        Order.objects.filter(user=request.user).update(total=value+tot)
        
        return HttpResponseRedirect(reverse("index"))
    

