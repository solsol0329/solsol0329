from django.urls import path
from . import views

app_name = "finlife"
urlpatterns = [
    path("", views.list),
    path("save-deposit-products/", views.save_prdt),
    path("deposit-products/", views.product_list),
    path("deposit-products-options/<fin_prdt_cd>/", views.option_list),
    path("deposit-products/top_rate/", views.top_rate),
]
