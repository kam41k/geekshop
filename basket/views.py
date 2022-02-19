from django.shortcuts import HttpResponseRedirect
from products.models import Product
from basket.models import Basket
from django.contrib import messages

# Create your views here.
def basket_add(request, product_id):
    product = Product.objects.get(id=product_id)
    basket = Basket.objects.filter(user=request.user, product=product)
    if product.quantity > 0:
        if not basket:
            Basket.objects.create(user=request.user, product=product, quantity=1)
            return HttpResponseRedirect(request.META['HTTP_REFERER'])
        else:
            basket = basket.first()
            if (product.quantity - basket.quantity) > 0:
                basket.quantity += 1
                basket.save()
                return HttpResponseRedirect(request.META['HTTP_REFERER'])
            else:
                messages.warning(request, 'Товар закончился.')
                return HttpResponseRedirect(request.META['HTTP_REFERER'])


def basket_remove(request, id):
    basket = Basket.objects.get(id=id)
    basket.delete()
    return HttpResponseRedirect(request.META['HTTP_REFERER'])
