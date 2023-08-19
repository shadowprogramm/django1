from django.urls import path, re_path
from . import views


app_name='app1'

urlpatterns = [
    path('', views.index, name='index'),
    path('getuser/<str:name>/<int:id>', views.pathview, name='path view'),
    path('operation', views.Operations.as_view()),
    re_path(r'^informations/(?P<year>[0-9]{4})$', views.informations),
]


"""
    include(path, namespace='')
    reverse(namespace:view_name) to get the path 
    {% url 'namespace:view_name' %}
    ?:name for non concern regex
"""