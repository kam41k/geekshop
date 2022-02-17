from django.shortcuts import render
from products.models import Product, ProductCategory

# Create your views here.
def index(request):
    context = {'title': 'geekShop', 'hello_content': 'Новые образы и лучшие бренды на GeekShop Store.\
                        Бесплатная доставка по всему миру! Аутлет: до -70% Собственный бренд. -20% новым покупателям.'}
    return render(request, 'products/index.html', context)

def products(request):
    context = {'title': 'geekShop - Каталог', 'categories': ProductCategory.objects.all(), 'products': Product.objects.all()}
    return render(request, 'products/products.html', context)
