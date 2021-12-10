from django.urls import path
from app.views import RegisterAPIView,LoginAPIView 

#Swagger settings
from drf_yasg.views import get_schema_view
from drf_yasg import openapi
schema_view = get_schema_view(
   openapi.Info( 
      title="API Doc",
      default_version='v1',
      description="API'S",

   ),
   public=True,
)

urlpatterns = [
	path('', schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'),
    path('redoc', schema_view.with_ui('redoc', cache_timeout=0), name='schema-redoc'),
    
   	path("register/", RegisterAPIView.as_view()),
   	path("login/",LoginAPIView.as_view()),

   
    
]

