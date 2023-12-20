from django.urls import path

from .views import feedback_view, success_view, error_view

urlpatterns = [
    # path('', index, name='index'),
    path('feedback/', feedback_view, name='feedback'),
    path('success/', success_view, name='success'),
    path('error/', error_view, name='error'),
]
