from django.urls import path
from .import views

urlpatterns = [
    path('feesdj/',views.fess_django),
    path('feespy/',views.fess_python),
    
]
