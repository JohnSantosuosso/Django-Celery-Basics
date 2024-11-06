from django.contrib import admin
from django.urls import path
from tasks import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('trigger-task/', views.trigger_task, name='trigger_task'),
    path('process-text/', views.process_text, name='process_text'),
]