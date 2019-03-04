from django.urls import path
from . import views


urlpatterns = [
    path('', views.procedure_list, name='procedure_list'),
    path('proc1', views.proc1, name='proc1'),
    path('proc2', views.proc2, name='proc2'),
    # path('proc3', views.proc3, name='proc3'),
]