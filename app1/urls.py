
from django.urls import path
from app1.views import *
urlpatterns = [
    path('hello/', hello),
    path('salom/', salom),
    path('new/', new),
]
