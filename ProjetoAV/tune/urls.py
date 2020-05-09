from django.urls import path
from .views import index, contact, store, order

urlpatterns = [
    path('', index),
    path('contact',contact),
    path('store', store),
    path('order', order),

]