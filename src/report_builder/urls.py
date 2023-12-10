from django.urls import path
from . import views

urlpatterns = [
    path('<str:action>/report/manager', views.report_manager, name='report-manager'),

]