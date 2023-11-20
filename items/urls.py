from django.urls import path, include
from . import views

urlpatterns = [
    path("", views.home, name="home"),
    path("item/<int:pk>/", views.item_detail, name="detail"),
]
