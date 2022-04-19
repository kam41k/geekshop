from django.shortcuts import render, HttpResponseRedirect
from django.contrib import auth, messages
from django.core.mail import send_mail
from django.conf import settings
from users.models import User
from django.urls import reverse
from users.forms import UserLoginForm, UserRegistrationForm, UserProfileForm, UserProfileEditForm
from basket.models import Basket
from django.contrib.auth.decorators import login_required


# Create your views here.
def login(request):
    if request.method == 'POST':
        form = UserLoginForm(data=request.POST)
        if form.is_valid():
            username = request.POST['username']
            password = request.POST['password']
            user = auth.authenticate(username=username, password=password)
            if user and user.is_active:
                auth.login(request, user)
                return HttpResponseRedirect(reverse('index'))
    else:
        form = UserLoginForm()
    context = {'title': 'GeekShop - Авторизация', 'form': form}
    return render(request, 'users/login.html', context)


def registration(request):
    if request.method == 'POST':
        form = UserRegistrationForm(data=request.POST)
        if form.is_valid():
            user = form.save()
            if send_verify_mail(user):
                messages.success(request, 'Поздравляем! Регистрация прошла успешно.\
сообщение подтверждения отправлено на почту.')
                return HttpResponseRedirect(reverse('users:login'))
            else:
                messages.error(request, 'Ошибка отправки сообщения.')
                return HttpResponseRedirect(reverse('users:login'))
    else:
        form = UserRegistrationForm()
    context = {'title': 'GeekShop - Регистрация', 'form': form}
    return render(request, 'users/register.html', context)


def logout(request):
    auth.logout(request)
    return HttpResponseRedirect(reverse('index'))


@login_required
def profile(request):
    user = request.user
    if request.method == 'POST':
        form = UserProfileForm(instance=user, files=request.FILES, data=request.POST)
        profile_form = UserProfileEditForm(instance=user.userprofile)
        if form.is_valid() and profile_form.is_valid():
            form.save()
            profile_form.save()
            messages.success(request, 'Поздравляем! Изменения прошли успешно.')
            return HttpResponseRedirect(reverse('users:profile'))
    else:
        form = UserProfileForm(instance=user)
        profile_form = UserProfileEditForm(instance=user.userprofile)
    context = {
        'title': 'GeekShop - Профиль',
        'form': form,
        'profile_form': profile_form,
        'basket': Basket.objects.filter(user=user),
    }
    return render(request, 'users/profile.html', context)


def send_verify_mail(user):
    verify_link = reverse('users:verify', args=[user.email, user.activation_key])
    title = f'Подтверждение учетной записи {user.username}'
    message = f'Для подтверждения учетной записи {user.username} на портале \
{settings.DOMAIN_NAME} перейдите по ссылке: \n {settings.DOMAIN_NAME}{verify_link}'
    return send_mail(title, message, settings.EMAIL_HOST_USER, [user.email],
                     fail_silently=False)


def verify(request, email, activation_key):
    try:
        user = User.objects.get(email=email)
        if user.activation_key == activation_key and not user.is_activation_key_expired():
            user.is_active = True
            user.activation_key = None
            user.activation_key_expires = None
            user.save()
            auth.login(request, user, backend='django.contrib.auth.backends.ModelBackend')
            messages.success(request, f'Поздравляем! Пользователь {user.username} подтвержден.')
            return HttpResponseRedirect(reverse('index'))
        else:
            messages.error(request, f'Ошибка! Пользователь {user.username} не подтвержден.')
            return HttpResponseRedirect(reverse('index'))
    except Exception as e:
        print(f'error activation user : {e.args}')
        return HttpResponseRedirect(reverse('index'))
