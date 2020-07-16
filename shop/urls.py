from django.urls import path
from . import views

urlpatterns = [
    path('', views.item_list, name="item_list"),
    path('login/', views.Login.as_view(), name='login'),
    path('logout/', views.Logout.as_view(), name='logout'),
    #     ユーザー新規追加
    path('registration', views.registration_user, name="registration"),
    path('cart_plus/<int:pk>/', views.cart_plus, name="cart_plus"),
    path('cart_list', views.cart_list, name="cart_list"),
    path('amount_edit/<int:pk>/', views.amount_edit, name="amount_edit"),
    path('cart_remove/<int:pk>/', views.cart_remove, name="cart_remove"),
    path('finish_list', views.finish_list, name="finish_list"),

]
