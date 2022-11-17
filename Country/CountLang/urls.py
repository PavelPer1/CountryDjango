from django.contrib import admin
from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.about, name='about'),
    path('country', views.country_add, name='country'),
    path('country/<url_country>', views.country_lang),
    path('language', views.language, name='language'),
    path('language/<url_language>', views.language_count_add)
]