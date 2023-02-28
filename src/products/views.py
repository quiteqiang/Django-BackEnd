from django.shortcuts import render, get_object_or_404, redirect
from .models import Product
from django.http import Http404

from .forms import ProductForm, RawProductForm
def product_list_view(request):
    queryset = Product.objects.all()
    context = {
        'object_list': queryset
    }
    return render(request, "product/product_list.html", context)



# Create your views here.
def product_detail_view(request):
    my_form = RawProductForm()
    if request.method == "POST":
        my_form = RawProductForm(request.POST)
        if my_form.is_valid():
            print(my_form.cleaned_data)
            Product.objects.create(**my_form.cleaned_data)
        else:
            print(my_form.errors)
    context = {
        "form": my_form
    }
    return render(request, "product/product_creation.html", context)
    

def render_initial_view(request):
    initial_data = {
        'title': "my good title"
    }

    obj = Product.objects.get(id=1)
    form = ProductForm(request.POST or None, initial=initial_data, instance=obj)

    context = {
        "form": form
    }
    return render(request, "product/product_creation.html", context)
# def product_detail_view(request):
#     print(request.GET)
#     print(request.POST)
#     my_title = request.POST.get('title')
#     Product.objects.create(title=my_title)
#     context = {}
#     return render(request, "product/product_creation.html", context)


# def product_detail_view(request):
#     obj = Product.objects.get(id=1)
#     context = {
#         'title': obj.title,
#         'description': obj.description
#     }
#     return render(request, "product/detail.html", context)



def product_create_view(request):
    form = ProductForm(request.POST or None)
    if form.is_valid():
        form.save()
        form = ProductForm()
    context = {
        'form': form
    }
    return render(request, "product/product_creation.html", context)


def dynamic_lookup_view(request, id):
    # obj = Product.objects.get(id=id)
    obj = get_object_or_404(Product, id=id)
    # obj.delete()
    # Use Post Request to delete

    # try:
    #     obj = Product.objects.get(id=id)
    # except Product.DoesNotExist:
    #     raise Http404
    
    context = {
        'object': obj
    }
    return render(request, "products/product_detail.html", context)

def dynamic_delete_view(request, id):
    # obj = Product.objects.get(id=id)
    obj = get_object_or_404(Product, id=id)
    if request.method == "POST":
        obj.delete()
        return redirect('../../')
    context = {
        'object': obj
    }
    return render(request, "product/product_delete.html", context)