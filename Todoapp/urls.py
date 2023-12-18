from django.urls import path
from . import views
from django.views.generic import TemplateView

app_name="Todoapp"
urlpatterns=[
        path('open', views.OpenView.as_view(), name='open'),
        path('', views.MainView.as_view(), name='all'),
        path('create/', views.TodoCreateView.as_view(), name='todo_create'),
        path('delete/<int:pk>/', views.TodoDeleteView.as_view(), name='todo_delete'),
        path('mark_completed/<int:pk>/', views.MarkCompletedView.as_view(), name='mark_completed'),
]