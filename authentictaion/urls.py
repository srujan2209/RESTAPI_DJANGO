from django.urls import path
from . import views
urlpatterns = [
    path('', views.HellpAuthView.as_view(),name='hello_auth'))
]
