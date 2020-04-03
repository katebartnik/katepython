from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('product-list', views.product_list, name='product_list'),
    path('about-us', views.about_us, name='about_us'),
    path('contact', views.contact, name='contact'),
]