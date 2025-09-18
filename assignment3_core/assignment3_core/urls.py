from django.contrib import admin
from django.urls import path
from math_operations.views import home

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', home, name='form'),
    path('results/', home, name='results')
]
