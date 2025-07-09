from django.urls import path,include
from rest_framework.routers import DefaultRouter
from profiles_api import views

router = DefaultRouter()
router.register('hello-viewset', views.HelloViewSet, basename='hello_world')
router.register('profiles', views.UserProfileViewSet)

urlpatterns = [
    path('hello-view/', views.HelloApiView().as_view(), name='hello_world'),
    path('login/', views.UserLoginApiView.as_view()),
    path('', include(router.urls)),
    ]