from django.urls import path
from . import views

urlpatterns = [
    path('fessdj/',views.fess_django),
    path('fesspy/',views.fess_python),
    ]
