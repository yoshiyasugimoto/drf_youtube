from rest_framework import routers
from django.urls import path, include
from .views import VideoViewSet, CreateUserView  # ModelViewSetはrouterでurlの繋ぎ込み

router = routers.DefaultRouter()
router.register("videos", VideoViewSet)

urlpatterns = [
    path('create/', CreateUserView.as_view(), name='create'),
    path('', include(router.urls)),
]
