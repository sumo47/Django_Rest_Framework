from django.urls import path, include
from api.views import CompanyViewSets
from rest_framework import routers

router = routers.DefaultRouter()
router.register(r'companies', CompanyViewSets)

urlpatterns = [
    path('', include(router.urls))
]
