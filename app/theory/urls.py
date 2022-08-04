from rest_framework.routers import DefaultRouter
from .views import *
from app.user.views import *
from django.urls import path

router = DefaultRouter()
router.register(r'subjects', SubjectViewSet, basename='subjects')
router.register(r'questions', QuestionViewSet, basename='questions')
router.register(r'answers', AnswerViewSet, basename='answers')
router.register(r'users', UserViewSet, basename='users')
urlpatterns = router.urls

urlpatterns += [
    path('user/current/', CurrentUserView.as_view()),
]
