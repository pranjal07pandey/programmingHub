from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('courses/', views.courses, name='courses'),
    path('course/<int:pk>/', views.course_details, name='course_details'),
    path('course/<int:pk>/<int:pk1>/', views.lesson_details, name='lesson_details'),
    path('blogs/', views.blogs, name='blogs'),
    path('newsletter/', views.newsletter, name='newsletter'),
    path('pricing/', views.pricing, name='pricing'),

    path('register/', views.register, name='register'),
    path('logout/', views.logoutUser, name='logout'),
    path('dashboard/<int:pk>/', views.dashboard, name='dashboard'),

    # path('login/', views.loginUser, name='login'),
   
]