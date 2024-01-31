from django.urls import path

from .views import BusinessAPIView, NearByView

urlpatterns = [
    path('', BusinessAPIView.as_view()),
    path('nearby', NearByView.as_view())
]
