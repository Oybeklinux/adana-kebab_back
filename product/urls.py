from rest_framework.routers import DefaultRouter
from django.urls import path, include
from .views import *


router = DefaultRouter()
router.register("burgers", MenuViewSet)
router.register("categories", CategoryViewSet)
router.register("settings", SettingsViewSet)
router.register("video", VideoViewSet)
router.register("galary", GalaryViewSet)
router.register("party", PartyViewSet)

urlpatterns = [
    path('', include(router.urls)),
    path('orders/', OrderList.as_view()),
    path('orders/<int:pk>/', OrderDetail.as_view())
]
