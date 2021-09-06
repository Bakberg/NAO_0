from .import views
from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from .models import *

urlpatterns = [
    path('', views.news, name='news'),
    path('test/', views.Test.as_view)
]

