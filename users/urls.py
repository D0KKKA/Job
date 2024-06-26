from django.urls import path, include
from rest_framework import routers
from .views import *
app_name = 'users'

# Создание экземпляра маршрутизатора
router = routers.DefaultRouter()

# Регистрация представлений в маршрутизаторе
router.register(r'users', UserView)




urlpatterns = [
    # Включение маршрутов из маршрутизатора
    path('', include(router.urls)),
    path('registration/',RegistrationView.as_view(),name='user-registration'),
    path('login/',LoginView.as_view(),name='user-login'),
    path('logout/',LogoutView.as_view(),name='user-logout'),

]


