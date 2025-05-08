from django.contrib import admin
from django.urls import path
from bot.views import register_user
from bot.views import get_user_info

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/register/', register_user),
    path('api/myinfo/', get_user_info),
]
