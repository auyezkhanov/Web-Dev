from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import CompanyViewSet, VacancyViewSet

# Настроим роутер для ViewSet-ов
router = DefaultRouter()
router.register(r'companies', CompanyViewSet)
router.register(r'vacancies', VacancyViewSet)

# Подключаем маршруты из роутера
urlpatterns = [
    path('api/', include(router.urls)),
]
