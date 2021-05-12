from django.urls import path, include
from rest_framework import routers
from UsersApp import views

router = routers.DefaultRouter()
router.register(r'users', views.UserViewSet, basename='User')

urlpatterns = [
    path('', include(router.urls))
]