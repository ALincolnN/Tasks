from django.urls import path
from . import views

urlpatterns = [
    path('', views.list, name='list'),
    
    
    #path('task-list/', views.tasklist, name = 'tasks-list'),
    #path('task-detail/<str:pk>/', views.taskDetail, name = 'tasks-detail'),
    #path('task-create/', views.taskCreate, name = 'tasks-create'),
    #path('task-update/<str:pk>/', API.views.taskUpdate, name = 'tasks-update'),
    #path('task-delete/<str:pk>/', views.taskDelete, name = 'tasks-delete'),
    
]