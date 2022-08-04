from rest_framework.routers import DefaultRouter
from .views import *
from django.urls import path


router = DefaultRouter()
router.register(r'users', UserViewSet, basename='users')
urlpatterns = router.urls
urlpatterns += [
    path('user/current/', CurrentUserView.as_view()),
]
