
from django.contrib import admin
from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from ordersystem.views import startpage
from ordersystem.views import menumanage
from ordersystem.views import managepage
from ordersystem.views import categorymanage
from ordersystem.views import usermanage
from ordersystem.views import ordermanage
from ordersystem.views import order_edit
from ordersystem.views import order_delete
urlpatterns = [
    path('admin/', admin.site.urls),
    path('',startpage),
    path('managepage/',managepage),
    path('managepage/menumanage/',menumanage),
    path('managepage/categorymanage/',categorymanage),
    path('managepage/usermanage/',usermanage),
    path('managepage/ordermanage/',ordermanage),
    path('order/<int:pk>/edit/',order_edit,name='order_edit'),
    path('order/<int:pk>/delete/',order_delete,name='order_delete'),

]+static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)
