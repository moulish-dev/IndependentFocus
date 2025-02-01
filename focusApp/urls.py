from . import views
from django.urls import path

urlpatterns = [
    path('',views.focusApp,name='/'),
    path('login',views.loginPage,name='loginPage'),
    path('dashboard',views.dashboardPage,name='dashboardPage'),
    path('process-task/', views.process_task, name='process-task'),
]
    