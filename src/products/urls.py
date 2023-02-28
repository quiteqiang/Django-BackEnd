from django.urls import path

from .views import (
    product_detail_view,
    product_create_view,
    render_initial_view,
    dynamic_lookup_view,
    dynamic_delete_view,
    product_list_view,
)

urlpatterns = [
    path('', product_detail_view),
    path('create/', product_create_view),
    path('<int:id>/', dynamic_lookup_view, name='product-detail'),
    path('<int:id>/delete/', dynamic_delete_view, name='product-delete'),
    path('', product_list_view, name='product-list')
]

