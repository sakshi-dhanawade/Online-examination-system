from django.urls import path
from . import views

urlpatterns = [
    path('', views.exam_list, name='exam_list'),
    path('<int:pk>/', views.exam_detail, name='exam_detail'), 
    path('<int:pk>/take/', views.take_exam, name='take_exam'),
    
]

