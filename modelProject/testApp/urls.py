from django.urls import path
from testApp import views

urlpatterns = [
    path('user/', views.userApiView.as_view()),
    path('user/<int:id>/', views.userApiView.as_view()),  # This is correct for user detail
]
