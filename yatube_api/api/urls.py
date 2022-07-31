from rest_framework.routers import DefaultRouter

from django.urls import include, path

from .views import PostViewSet

router = DefaultRouter()
router.register('posts', PostViewSet)

urlpatterns = [
    path('v1/', include(router.urls)),
]
