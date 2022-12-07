from django.urls import path, include
from rest_framework import routers
from .views import *

router = routers.SimpleRouter()
router.register(r'user', UserView, basename="User")
router.register(r'page',PageView, basename="Page")
router.register(r'followers', FollowersView, basename="Follower")
router.register(r'post', PostsViews, basename="Post")

urlpatterns = [
        path('', include(router.urls))
    ]
