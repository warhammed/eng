from django.urls import path
from . import views

app_name = "groups"
urlpatterns = [
    path('', views.index, name="index"),
    path('<slug:slug>/', views.group_detail, name="detail"),
]
