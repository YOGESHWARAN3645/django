from django.urls import path
from testApp import views
urlpatterns=[path('',views.wish),
                path('results',views.result)]