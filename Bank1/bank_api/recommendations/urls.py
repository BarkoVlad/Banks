from django.urls import path
from .views import RecommendationView

urlpatterns = [
    path('recommendations/<int:client_id>/', RecommendationView.as_view(), name='recommendations'),
]