from django.urls import path
from ApiApplication import views

urlpatterns=[path('user/',views.userApiView.as_view()),]