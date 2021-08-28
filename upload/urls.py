from rest_framework import routers

from .views import UserViewSet, ContentViewSet

router = routers.DefaultRouter()

router.register('users', UserViewSet)
router.register('contents', ContentViewSet)
