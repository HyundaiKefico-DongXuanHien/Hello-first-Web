# ============================================================================
# FILE NAME     : myapp/urls.py
# AUTHOR        : DONG XUAN HIEN
# DIVISION      : HYUNDAI KEFICO Co.,Ltd.
# DESCRIPTION   : Define url for myapp
# HISTORY       : 05/11/2025
# ============================================================================

from django.urls import path
from . import views

urlpatterns = [
    path('', views.task_list, name='task_list'),
]