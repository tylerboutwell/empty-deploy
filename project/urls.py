from django.contrib import admin
from django.urls import path
from main import views # <-- new

urlpatterns = [
    path('', views.main_page), # <-- new
    path('admin/', admin.site.urls),
]