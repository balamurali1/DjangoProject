from django.urls import path
from . import views    # . mean's current directory(floder)

urlpatterns = [
    path('django/',views.learn_django)

]    
