from django.urls import path
from django.contrib.auth.views import LogoutView

from .views import registerView, CustomLoginView

urlpatterns = [
    path('login/', CustomLoginView.as_view(), name="login_url"),
    path('register/', registerView, name="register_url"),
    path('logout/', LogoutView.as_view(), name="logout"),
]