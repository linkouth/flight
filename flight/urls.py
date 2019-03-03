from django.urls import path
from . import views


urlpatterns = [
    path('', views.procedure_list, name='procedure_list'),
    path('proc1', views.proc1, name='proc1'),
]