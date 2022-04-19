from datetime import datetime

import requests
from django.utils import timezone

from users.models import UserProfile


def save_user_profile(backend, user, response, *args, **kwargs):
    if backend.name == 'vk-oauth2':
        fields = ','.join(('sex', 'about', 'bdate', 'city', 'mobile_phone', 'home_phone'))
        access_token = response['access_token']
        version = '5.131'
        api_url = f'http://api.vk.com/method/users.get?fields={fields}&access_token={access_token}&v={version}'


        resp = requests.get(api_url)
        if resp.status_code != 200:
            return
        data = resp.json()['response'][0]

        if data['sex'] == 1:
            user.userprofile.gender = UserProfile.FEMALE
        elif data['sex'] == 2:
            user.userprofile.gender = UserProfile.MALE
        if data['about']:
            user.userprofile.about = data['about']
        user.save()
    elif backend.name == "google-oauth2":
        access_token = response
        print(access_token)