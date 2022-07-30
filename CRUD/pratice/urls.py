from codecs import namereplace_errors
from collections import namedtuple
from django.urls import path
from . import views
urlpatterns = [path('Create',views.create),
               path('Read',views.read),
               path("update/<int:data>",views.update,name="update"),
               path("delete/<int:data>",views.delete)]