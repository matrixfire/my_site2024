from django.contrib import admin
from django.urls import path
from django.contrib.sitemaps.views import sitemap
from .views import RobotsTxtView
from . import views



app_name = 'service'

urlpatterns = [
    path('', views.service, name='service'),
    # path('products/', views.product_list, name='product_list'),
    # path('<slug:category_slug>/', views.product_list, name='product_list_by_category'),
    # path('<int:id>/<slug:slug>/', views.product_detail, name='product_detail'),
    # path('robots.txt', RobotsTxtView.as_view(), name='robots_txt'),
]
