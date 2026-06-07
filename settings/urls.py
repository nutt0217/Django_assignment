from django.urls import path
from . import views


urlpatterns = [
    path('category/', views.category),
    path('brand/', views.brand),
    path('product/', views.product)

]
