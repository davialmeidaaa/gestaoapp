from django.urls import path
from .views import UserLoginView, UserLogoutView, SignUpView

app_name = 'accounts'

urlpatterns = [
    path('login/', UserLoginView.as_view(), name='login'),
    path('logout/', UserLogoutView.as_view(), name='logout'),
    path('signup/', SignUpView.as_view(), name='signup'),
]
