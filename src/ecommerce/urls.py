"""ecommerce URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.1/topics/http/urls/
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
from django.conf import settings
from django.conf.urls.static import static

from django.contrib import admin
from django.urls import re_path
from .views import home_page, about_page, contact_page, login_page, register_page
from products.views import product_list_view

# Using re_path() instead of path() for
# handelling dynamic URLs.
urlpatterns = [
    re_path(r'^$', home_page),
    re_path(r'^about/$', about_page),
    re_path(r'^contact/$', contact_page),
    re_path(r'^login/$', login_page),
    re_path(r'^register/$', register_page),
    re_path(r'^products/$', product_list_view),
    re_path(r'^admin/', admin.site.urls),
]

if settings.DEBUG:
    urlpatterns = urlpatterns + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
    urlpatterns = urlpatterns + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
