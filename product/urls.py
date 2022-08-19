from django.urls import path, include
from .views import *
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register('products', ProductViewSet)
router.register('subcategories', SubcategoryViewSet)
router.register('categories', CategoryViewSet)

urlpatterns = [
    path('', include(router.urls))
]