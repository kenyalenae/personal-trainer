from django.urls import path
from . import views

from .views import emailView, successView

# url patterns for trainer views
urlpatterns = [
    path('', views.home, name='trainer-home'),
    path('accountHome/', views.accountHome, name='account-home'),
    path('about/', views.about, name='trainer-about'),
    path('email/', emailView, name='email'),
    path('success/', successView, name='success'),
    path('workout_program/', views.workoutProgram, name='workout-program'),
    path('meal_plan/', views.mealPlan, name='meal-plan'),
]



