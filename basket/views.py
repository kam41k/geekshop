from django.shortcuts import HttpResponseRedirect
from products.models import Product
from basket.models import Basket
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.http import JsonResponse
from django.template.loader import render_to_string


# Create your views here.
@login_required
def basket_add(request, product_id):
    product = Product.objects.get(id=product_id)
    basket = Basket.objects.filter(user=request.user, product=product)
    if product.quantity > 0:
        if not basket:
            Basket.objects.create(user=request.user, product=product, quantity=1)
            return HttpResponseRedirect(request.META['HTTP_REFERER'])
        else:
            basket = basket.first()
            if product.quantity > basket.quantity:
                basket.quantity += 1
                basket.save()
                return HttpResponseRedirect(request.META['HTTP_REFERER'])
            else:
                messages.warning(request, 'Товар закончился.')
                return HttpResponseRedirect(request.META['HTTP_REFERER'])


@login_required
def basket_remove(request, id):
    basket = Basket.objects.get(id=id)
    basket.delete()
    return HttpResponseRedirect(request.META['HTTP_REFERER'])

@login_required
def basket_edit(request, id, quantity):
    if request.is_ajax():
        item = Basket.objects.get(id=id)
        if quantity > 0:
            item.quantity = quantity
            item.save()
        else:
            item.delete()
        basket = Basket.objects.filter(user=request.user)
        context = {'basket': basket}
        result = render_to_string('basket/basket.html', context)
        return JsonResponse({'result': result})
