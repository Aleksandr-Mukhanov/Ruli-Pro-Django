from rest_framework.routers import DefaultRouter
from .views import *
from app.user.views import *
from app.teacher.views import *
from app.student.views import *
from app.school.views import *
from app.car.views import *
from django.urls import path

router = DefaultRouter()
router.register(r'subjects', SubjectViewSet, basename='subjects')
router.register(r'questions', QuestionViewSet, basename='questions')
router.register(r'answers', AnswerViewSet, basename='answers')
router.register(r'users', UserViewSet, basename='users')
router.register(r'teacher', TeacherViewSet, basename='teacher')
router.register(r'student', StudentViewSet, basename='student')
router.register(r'school', SchoolViewSet, basename='school')
router.register(r'school-member', MemberViewSet, basename='school-member')
router.register(r'car', CarViewSet, basename='car')
urlpatterns = router.urls

urlpatterns += [
    path('user/current/', CurrentUserView.as_view()),
]
