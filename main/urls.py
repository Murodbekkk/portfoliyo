from django.urls import path
from . import views

app_name = "main"

urlpatterns = [
    path("", views.index, name="index"),
    path("loyiha/<slug:slug>/", views.project_detail, name="project_detail"),
]
