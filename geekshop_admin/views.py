from django.shortcuts import render, HttpResponseRedirect
from django.urls import reverse
from django.contrib import messages
from users.models import User
from geekshop_admin.forms import GeekshopAdminCreationForm, GeekshopAdminProfileForm


# Create your views here.
def admin(request):
    context = {'title': 'GeekShop - Admin'}
    return render(request, 'geekshop_admin/admin.html', context)


def admin_users_create(request):
    if request.method == 'POST':
        form = GeekshopAdminCreationForm(data=request.POST, files=request.FILES)
        if form.is_valid():
            form.save()
            messages.success(request, 'Пользователь успешно создан.')
            return HttpResponseRedirect(reverse('geekshop_admin:admin-users-read'))
    else:
        form = GeekshopAdminCreationForm()
    context = {'title': 'GeekShop - Admin', 'form': form}
    return render(request, 'geekshop_admin/admin-users-create.html', context)


def admin_users_read(request):
    context = {'title': 'GeekShop - Admin', 'Users': User.objects.all()}
    return render(request, 'geekshop_admin/admin-users-read.html', context)


def admin_users_update(request, user_id):
    user = User.objects.get(id=user_id)
    if request.method == 'POST':
        form = GeekshopAdminProfileForm(instance=user, files=request.FILES, data=request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse('geekshop_admin:admin-users-read'))
    else:
        form = GeekshopAdminProfileForm(instance=user)
    context = {'title': 'GeekShop - Admin', 'User': user, 'form': form}
    return render(request, 'geekshop_admin/admin-users-update-delete.html', context)


def admin_users_delete(request, user_id):
    user = User.objects.get(id=user_id)
    user.self_delete()
    return HttpResponseRedirect(reverse('geekshop_admin:admin-users-read'))
