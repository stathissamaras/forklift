
from django.urls import path, re_path
from forkapp.views import page_not_found
from forkapp import views as v
from .views import *

handler404 = page_not_found


urlpatterns = [
    path('', v.home, name='home'),
    path("contact_us/", v.contactview, name="contact_us"),
    path('about/', v.about, name='about'),
    path('dieseltrucks/', v.dieseltrucks, name='dieseltrucks'),
    path('shopsingle/<str:pk>/', v.shopsingle, name='shopsingle'),
    path('contact/', v.contactview, name='contact'),


    path("profile/", CustomerProfileView.as_view(), name="customerprofile"),
    path("profile/order/<int:pk>/", CustomerOrderDetailView.as_view(), name="customerorderdetail"),

    path("logout/", CustomerLogoutView.as_view(), name="customerlogout"),
    path("login/", CustomerLoginView.as_view(), name="customerlogin"),
    path("register/", CustomerRegistrationView.as_view(), name="customerregistration"),
    path("search/", SearchView.as_view(), name="search"),

    path("forgot-password/", PasswordForgotView.as_view(), name="passworforgot"),
    path("password-reset/<email>/<token>/",PasswordResetView.as_view(), name="passwordreset"),

    # Admin Side pages

    path("admin-login/", AdminLoginView.as_view(), name="adminlogin"),
    path("admin-home/", AdminHomeView.as_view(), name="adminhome"),
    path("admin-order/<int:pk>/", AdminOrderDetailView.as_view(), name="adminorderdetail"),

    path("admin-all-orders/", AdminOrderListView.as_view(), name="adminorderlist"),

    path("admin-order-<int:pk>-change/", AdminOrderStatusChangeView.as_view(), name="adminorderstatuschange"),

    path("admin-product/list/", AdminProductListView.as_view(), name="adminproductlist"),
]
