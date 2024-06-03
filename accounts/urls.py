from django.urls import path

from .views import SearchUserView, SignupView, LoginView, MyTokenRefreshView

urlpatterns = [
    path('signup/', SignupView.as_view(), name='signup'),
    path('login/', LoginView.as_view(), name='login'),
    path('token/refresh/', MyTokenRefreshView.as_view(), name='token_refresh'),
    path('search/', SearchUserView.as_view(), name='search'),
]
