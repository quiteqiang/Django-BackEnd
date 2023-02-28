"""tryDjango URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include

from pages.views import homepage_view, contacts_view
# from products.views import product_detail_view, product_create_view,render_initial_view, dynamic_lookup_view, dynamic_delete_view, product_list_view

urlpatterns = [
    path('', homepage_view, name='home'),
    path('admin/', admin.site.urls),
    path('home/', homepage_view),
    path('contact/', contacts_view),
    path('products/', include('products.urls')),
    # path('initialView/', render_initial_view),
    # path('product/', product_detail_view),
    # path('create/', product_create_view),
    # path('products/<int:id>/', dynamic_lookup_view, name='product-detail'),
    # path('dynamicProduct/<int:id>/delete/', dynamic_delete_view, name='product-delete'),
    # path('products/', product_list_view, name='product-list')
]

