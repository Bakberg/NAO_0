from django.conf.urls import url

from .import views
from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from .forms import *

urlpatterns = [
    path('', views.glav),
    path('news', views.news),
    path('otziv', views.otziv),
    path('kategory', views.kategory),
    path('gilim', views.gilim),
    path('bilim', views.bilim),
    path('Innovacia', views.Innovacia),
    path('Adisteme', views.Adisteme),
    path('st_1', views.st_1),
    path('st_2', views.st_2),
    path('news_2', views.news_2),
    path('base', views.base),
    path('test/', views.Test.as_view)
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATICFILES_ROOT)
