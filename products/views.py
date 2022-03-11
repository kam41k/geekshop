from django.shortcuts import render
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from products.models import Product, ProductCategory

# Create your views here.
def index(request):
    context = {'title': 'geekShop', 'hello_content': 'Новые образы и лучшие бренды на GeekShop Store.\
                        Бесплатная доставка по всему миру! Аутлет: до -70% Собственный бренд. -20% новым покупателям.'}
    return render(request, 'products/index.html', context)


def products(request, category_id=None, page=1):
    if category_id:
        products = Product.objects.filter(category_id=category_id)
    else:
        products = Product.objects.all()
    paginator = Paginator(products, 3)
    try:
        products_paginator = paginator.page(page)
    except PageNotAnInteger:
        products_paginator = paginator.page(1)
    except EmptyPage:
        products_paginator = paginator.page(paginator.num_pages)
    context = {'title': 'geekShop - Каталог',
               'categories': ProductCategory.objects.all(),
               'products': products_paginator
               }
    return render(request, 'products/products.html', context)
