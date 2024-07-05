from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path("login", views.login_view, name="login"),
    path("logout", views.logout_view, name="logout"),
    path("register", views.register, name="register"),

    #routes
    path("menu", views.menu, name="menu"),
    path("add", views.add, name="add"),
    path("allorders", views.allorders, name="allorders"),
    path("myorders", views.myorders, name="myorders"),
    path("myorders/cancle", views.cancleorder, name="cancleorder"),


    # API's
    path("orders", views.orders, name="orders"),
    path("orders/<int:order_id>", views.a_order, name="a_order"),

    path("additem", views.add_item, name="additem"),
    
    path("allitems", views.allitems, name="allitems"),
    path("allitems/<int:item_id>", views.a_item, name="a_item"),
    path("allitems/<str:category_name>", views.menu_categories, name="menu_categories")
]