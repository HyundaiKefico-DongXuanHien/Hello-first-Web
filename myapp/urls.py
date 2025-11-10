# ============================================================================
# FILE NAME     : myapp/urls.py
# AUTHOR        : DONG XUAN HIEN
# DIVISION      : HYUNDAI KEFICO Co.,Ltd.
# DESCRIPTION   : Define url for myapp
# HISTORY       : 11/11/2025
# ============================================================================

from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('task_list/', views.task_list, name='task_list'),
    path('document/', views.document, name='document'),
    path('report/', views.report, name='report'),
    path('tool/', views.tool, name='tool'),
    path('run_tool/<str:tool_id>/', views.run_tool, name='run_tool')  #Get agrument tool_id from html and add it into route
]