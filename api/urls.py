from django.urls import path, include
from rest_framework import routers
from .views import CreateUserView, ListUserView, LoginUserView, CategoryViewSet, SkillsViewSet

router = routers.DefaultRouter()
router.register('category', CategoryViewSet)
router.register('skills', SkillsViewSet)

urlpatterns = [
    path('create/', CreateUserView.as_view(), name='create'),
    path('users/', ListUserView.as_view(), name='users'),
    path('loginuser/', LoginUserView.as_view(), name='loginuser'),
    path('', include(router.urls)),
]