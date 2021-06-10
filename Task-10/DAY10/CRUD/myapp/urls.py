from django.urls import path
from . import views

urlpatterns = [
    path('',views.homepageview, name="Home"),
    path('about',views.aboutpageview, name="About Us"),
    path('contact',views.contactpageview, name="Contact Us"),
    path('dlist',views.companylist.as_view(), name="Companies"),
    path('clist',views.productlist.as_view(), name="Products"),
]