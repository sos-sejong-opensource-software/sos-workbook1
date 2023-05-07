# users/urls.py

from django.urls import path
from .views import (ListUserView, DetailUserView)

app_name = 'users'

urlpatterns = [
    path('', ListUserView.as_view(), name="user_api"),
    path('<int:pk>/', DetailUserView.as_view(), name="user_detail_api"),
]