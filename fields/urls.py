from django.urls import path
from . import views

app_name = "fields"
urlpatterns = [
    path('', views.index, name="index"),
    path('<str:degree_slug>/', views.degree_detail, name="degree_detail"),
    path('<str:degree_slug>/<str:field_slug>/', views.field_detail, name="field_detail"),
]
