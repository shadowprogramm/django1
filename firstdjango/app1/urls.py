from django.urls import path
from . import views


app_name='app1'
urlpatterns = [
    path('', views.index, name='index'),
    path('getuser/<name>/<int:id>', views.pathview, name='path view'),
]

"""
    include(path, namespace='')
    reverse(namespace:view_name) to get the path 
    {% url 'namespace:view_name' %}
"""