from django.urls import path, include
from rest_framework import routers

from .views import *
app_name = 'vacancies'

router = routers.DefaultRouter()

# Регистрация представлений в маршрутизаторе
router.register(r'job', JobViewSet)
router.register(r'usersjob', UsersJobViewSet)



urlpatterns = [
    # Включение маршрутов из маршрутизатора
    path('', include(router.urls)),

]