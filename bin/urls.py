from django.urls import path,include
from . import views
app_name = 'bin'
urlpatterns = [

    path('',views.index, name='index'),
    path('log_in',views.log_in,name='log_in'),
]