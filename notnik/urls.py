"""notnik URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path,include
from apps.products.views import ProductAPIView, ProductCreateAPIView, ProductUpdateAPIView, ProductDeleteAPIView
from apps.categories.views import CategoryAPIView,CategoryCreateAPIView, CategoryUpdateAPIView, CategoryDeleteAPIView
from apps.users.views import UserAPIView, UserCreateAPIView, UserUpdateAPIView,UserDeleteAPIView
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api-auth/', include('rest_framework.urls')),
    path('auth/', include('djoser.urls')),
    path('auth/', include('djoser.urls.authtoken')),
    path('api/auth/', include('djoser.urls.jwt')),

    #продукт api
    path('api/product', ProductAPIView.as_view(), name="product_api"),
    path('api/product/create', ProductCreateAPIView.as_view(), name = "product_create_api"),
    path('api/product/update/<int:pk>', ProductUpdateAPIView.as_view(), name = "product_api_update"),
    path('api/product/delete/<int:pk>',ProductDeleteAPIView.as_view(),name = "product_api_delete"),

    #категории api
    path('api/category',CategoryAPIView.as_view(),name = "category_api"),
    path('api/category/create',CategoryCreateAPIView.as_view(),name = "category_create_api"),
    path('api/category/update/<int:pk>',CategoryUpdateAPIView.as_view(),name = "category_api_update"),
    path('api/category/delete/<int:pk>',CategoryDeleteAPIView.as_view(),name = "category_api_delete"),

      #users api
    path('api/users', UserAPIView.as_view(), name = "users_api"),
    path('api/users/create', UserCreateAPIView.as_view(), name = "users_create_api"),
    path('api/users/update/<int:pk>', UserUpdateAPIView.as_view(), name = "users_update_api"),
    path('api/users/delete/<int:pk>', UserDeleteAPIView.as_view(), name = "users_delete_api"),
]
urlpatterns+=static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)