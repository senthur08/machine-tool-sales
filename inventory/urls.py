from django.urls import path
from . import views


urlpatterns=[
    path('', views.home, name="home"),
    path('tools/', views.productList, name="tools-user"),
    path('tool/<str:pk>', views.tool, name='single-tool'),
    path('order/<str:pk>', views.order, name='place-order'),
    path('userlog/' ,views.purchaseLog, name="user-log"),
]
