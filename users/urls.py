from django.urls import path
from .views import *

urlpatterns = [
    path('login/', LoginView.as_view(), name="login"),
    path('logout/', LogoutView.as_view(), name="logout"),
    path('signup/', SignupView.as_view(), name="signup"),
    path('profile/', ProfileUpdateView.as_view(), name="ProfileUpdateView"),
]
