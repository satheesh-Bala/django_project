from django.urls import path
from . import views
from .views import ProductSearchView

urlpatterns = [
    path('', views.home, name='home'),
    path('upload', views.add_product, name='upload'),
    path('add_item', views.add_item, name='add_item'),
    path('fetch_sku/', ProductSearchView.as_view(), name='product_search'),
]
