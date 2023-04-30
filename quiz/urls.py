from django.urls import path
from .views import IndexView
from . import views

appname = 'quiz'
urlpatterns = [
    path('', IndexView.as_view(), name='index'),
    path('takequiz', views.take_quiz, name='takequiz'),
    path('result', views.result , name='result'),
]