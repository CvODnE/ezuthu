from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('writings/', views.writings_list, name='writings'),
    path('writings/<int:id>/', views.writing_detail, name='writing_detail'),
    path('writers/', views.writers_list, name='writers'),
    path('submit/', views.submit_writing, name='submit'),
]
