# todo_list/todo_app/urls.py
from django.urls import path
from ToDoApp_app1 import views

urlpatterns = [
    path("", views.ListListView.as_view(), name="index"),

]