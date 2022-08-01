from rest_framework.routers import DefaultRouter

from django.urls import include, path

from .views import PostViewSet, GroupViewSet, CommentViewSet

router = DefaultRouter()
router.register('posts', PostViewSet, basename='posts')
router.register('groups', GroupViewSet, basename='groups')
router.register('posts/(?P<post_id>\\d+)/comments', CommentViewSet, basename='comments')

urlpatterns = [
    path('v1/', include(router.urls))
]
