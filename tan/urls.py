from django.urls import path
from . import views
urlpatterns = [

    path('', views.index, name='tan'),
    path('zhou/',views.index,name='zhou')
]