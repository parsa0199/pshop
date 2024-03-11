from django.urls import path
from .views import BookView

urlpatterns = [
    path('/home', BookView.as_view()),
]