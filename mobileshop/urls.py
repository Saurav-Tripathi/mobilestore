"""mobileshop URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
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
from django.urls import path
from myapp import views
from django.conf import settings
from django.conf.urls.static import static
urlpatterns = [
    path('admin/', admin.site.urls),
    path("",views.index,name="index"),
    path("about/",views.about,name="about"),
    path("blog_default/",views.blog_default,name="blog_default"),
    path("blog_single/",views.blog_single, name="blog_single"),
    path("cart/",views.cart,name="cart"),
    path("checkout/",views.checkout,name="checkout"),
    path("contact_us/",views.contact_us,name="contact_us"),
    path("login_form/",views.login_form,name="login_form"),
    path("product_list/",views.product_list,name="product_list"),
    path("product_single/<int:id>",views.product_single,name="product_single"),
    path("signup_form/",views.signup_form,name="signup_form"),
    path("styleguide/",views.styleguide,name="styleguide"),
    path("logout/",views.logout,name="logout"),
    path("add_to_cart/<int:id>",views.add_to_cart,name="add_to_cart"),

]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)