from django.urls import path
from . import views

urlpatterns = [

    path('tool_list/', views.tool_list, name="tool_list"),
    path('user_list/', views.user_list, name="user_list"),
    # この時点でurlはhttp://127.0.0.1:8000/tool/tool_create
    path('tool_create/', views.tool_create, name="tool_create"),
    path('stock_edit/<int:pk>/', views.stock_edit, name="stock_edit"),
    path('status_edit/<int:pk>/', views.status_edit, name="status_edit"),
    path('item_remove/<int:pk>/', views.item_remove, name="item_remove"),

]
