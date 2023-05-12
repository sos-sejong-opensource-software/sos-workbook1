from django.urls import path
from .views import (ListPostView, DetailPostView)

urlpatterns = [
   path('', ListPostView.as_view(), name="post_api"),
   path('<int:pk>/', DetailPostView.as_view(), name="post_detail_api"),
]