from greetingapp import views
from django.urls import path

urlpatterns=[
    path('',views.hello,name='helloworld'),
    path('morning',views.morning,name='morning'),
    path('afternoon',views.afternoon,name='afternoon'),
    path('evening',views.evening,name='evening')]