from django.urls import path
from app2.views import *

urlpatterns = [
    path('yangi/', yangi),
    path('django/', django),
    path('new2/', new2),
]