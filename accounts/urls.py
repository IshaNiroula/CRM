from django.urls import path
from . import views

urlpatterns = [

    # this is the url for register page
    path('register/', views.register_page, name="register"),

    # this is the url for login page
    path('login/', views.login_page, name="login"),

    # this is the url for logout page
    path('logout/', views.logout_user, name="logout"),

    # this is the url for home page
    path('', views.home, name='home'),


    path('user/', views.user_page, name="user-page"),

    # dynamic products url
    path('products/', views.products, name='products'),

    # dynamic customer url
    path('customer/<str:pk>', views.customer, name='customer'),


    path('create_order/<str:pk>', views.create_order, name='create_order'),


    path('update_order/<str:pk>', views.update_order, name='update_order'),


    path('delete_order/<str:pk>', views.delete_order, name='delete_order')
]
