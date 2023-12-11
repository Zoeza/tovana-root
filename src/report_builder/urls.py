from django.urls import path
from . import views

urlpatterns = [
    path('<str:action>/home/manager', views.home_manager, name='home-manager'),
    path('<str:action>/report/manager', views.report_manager, name='report-manager'),

]