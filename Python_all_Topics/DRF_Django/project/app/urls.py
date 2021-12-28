from django.urls import path
from .views import RegisterView,VerifyEmail,SetNewPasswordAPIView,LoginAPIView, PasswordTokenCheckAPI, RequestPasswordResetEmail
#from .views import RegisterView,SetNewPasswordAPIView, VerifyEmail, LoginAPIView, PasswordTokenCheckAPI,RequestPasswordResetEmail

from rest_framework_simplejwt.views import (
    TokenRefreshView,
)

from rest_framework import permissions
from drf_yasg.views import get_schema_view
from drf_yasg import openapi


schema_view = get_schema_view(
    openapi.Info(
        title="APP API",
        default_version='v1',
        description="API",
        # terms_of_service="https://www.ourapp.com/policies/terms/",
        # contact=openapi.Contact(email="contact@expenses.local"),
        # license=openapi.License(name="Test License"),
    ),
    public=True,
    permission_classes=(permissions.AllowAny,),
)


urlpatterns = [
    path('', schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'),
    path('redoc', schema_view.with_ui('redoc', cache_timeout=0), name='schema-redoc'),
    
    path('register/', RegisterView.as_view(), name="register"),
    path('login/', LoginAPIView.as_view(), name="login"),
    path('email-verify/', VerifyEmail.as_view(), name="email-verify"),
    path('token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('request-reset-email/', RequestPasswordResetEmail.as_view(),name="request-reset-email"),
    path('password-reset/<uidb64>/<token>/',PasswordTokenCheckAPI.as_view(), name='password-reset-confirm'),
    path('password-reset-complete', SetNewPasswordAPIView.as_view(),name='password-reset-complete')
]
