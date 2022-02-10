import json,geekshop.settings
from django.shortcuts import render

# Create your views here.
def index(request):
    context = {'title': 'geekShop', 'hello_content': 'Новые образы и лучшие бренды на GeekShop Store.\
                        Бесплатная доставка по всему миру! Аутлет: до -70% Собственный бренд. -20% новым покупателям.'}
    return render(request, 'products/index.html', context)

def products(request):
    context = {'title': 'geekShop - Каталог', 'products':[]}
    with open(geekshop.settings.BASE_DIR / 'products/fixtures/products.json', 'r') as read_file:
        context['products'] = json.load(read_file)
    return render(request, 'products/products.html', context)