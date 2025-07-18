from django.urls import path, include
from . import views

urlpatterns = [
  path('', views.home, name="Home"),
  path('login/', views.login, name="Login"),
  path('signup/', views.signup, name="Signup"),
  path('product/<slug:slug>/', views.product_view, name="Product_view")
]