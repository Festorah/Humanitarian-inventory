from django.urls import path
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView

from users.views.confirm_password_reset import ConfirmPasswordResetView
from users.views.login_user import LoginView
from users.views.logout import LogoutView
from users.views.register_user import RegisterView
from users.views.request_password import RequestPasswordView
from users.views.verify_email import VerifyEmailView

app_name = "users"

urlpatterns = [
    path("login/", LoginView.as_view(), name="login"),
    path("logout/", LogoutView.as_view(), name="logout"),
    path("register/", RegisterView.as_view(), name="register"),
    path(
        "verify-email/<str:token>/",
        VerifyEmailView.as_view(),
        name="verify-email",
    ),
    path(
        "password-reset/",
        RequestPasswordView.as_view(),
        name="password-reset",
    ),
    path(
        "password-reset/confirm/",
        ConfirmPasswordResetView.as_view(),
        name="password-reset-confirm",
    ),
    path("token/", TokenObtainPairView.as_view(), name="token_obtain_pair"),
    path("token/refresh/", TokenRefreshView.as_view(), name="token_refresh"),
]
