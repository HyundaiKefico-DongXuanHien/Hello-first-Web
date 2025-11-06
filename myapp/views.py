# ============================================================================
# FILE NAME     : myapp/views.py
# AUTHOR        : DONG XUAN HIEN
# DIVISION      : HYUNDAI KEFICO Co.,Ltd.
# DESCRIPTION   : Handle logic to display
# HISTORY       : 05/11/2025
# ============================================================================

from django.shortcuts import render
from .models import issue_data_table, issue_data_table_KVHS

def task_list(request):
    query = request.GET.get('search', '')  #get value from search bar, if not --> default is blank string
    if query:
        table1 = issue_data_table.objects.filter(assignee__icontains=query)
        table2 = issue_data_table_KVHS.objects.filter(assignee__icontains=query)
    else:
        table1 = issue_data_table.objects.all()
        table2 = issue_data_table_KVHS.objects.all()

    # Merge data from 2 table
    tasks = list(table1) + list(table2)
    return render(request, 'task_list.html', {'tasks': tasks, 'query': query})

