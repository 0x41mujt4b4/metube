from django.conf.urls import url
from . import views

urlpatterns = [
    url('download/', views.download, name="download"),
    url('', views.index, name="index"),
]
