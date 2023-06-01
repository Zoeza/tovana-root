from django.urls import path
from . import views


urlpatterns = [

    path('browser/', views.browser, name='browser'),
]

