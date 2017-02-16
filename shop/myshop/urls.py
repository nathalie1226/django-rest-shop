from django.conf.urls import url
from .views import ShopViewSet

from . import views

urlpatterns = [
    url(r'^$',ShopViewSet),

]