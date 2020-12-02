from django.contrib import admin
from django.urls import include, path
from todo import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('todo', include('todo.urls')),
]
