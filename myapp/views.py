# ============================================================================
# FILE NAME     : myapp/views.py
# AUTHOR        : DONG XUAN HIEN
# DIVISION      : HYUNDAI KEFICO Co.,Ltd.
# DESCRIPTION   : Handle logic to display
# HISTORY       : 11/11/2025
# ============================================================================

from django.shortcuts import render
from .models import issue_data_table, issue_data_table_KVHS
from django.db.models import Q
from django.core.paginator import Paginator

import importlib
from django.http import JsonResponse
from django.shortcuts import render, redirect
from django.contrib import messages



def home(request):
    return render(request, 'home.html', {'show_background': True})

def task_list(request):
    # Get value from search box
    query = request.GET.get('search', '')  #get value from search bar, if not --> default is blank string
    
    # Get value from dropdown
    key_filter = request.GET.get('key', '')
    priority_filter = request.GET.get('priority', '')
    reporter_filter = request.GET.get('reporter', '')
    assignee_filter = request.GET.get('assignee', '')
    status_filter = request.GET.get('status', '')
    
    # Create filter condition
    filter_condition = Q()
    if query:
        filter_condition &= (
            Q(key__icontains=query) |
            Q(request_title__icontains=query) |
            Q(priority__icontains=query) |
            Q(reporter__icontains=query) |
            Q(assignee__icontains=query) |
            Q(status__icontains=query) |
            Q(created__icontains=query) |
            Q(updated__icontains=query)
        )
    if key_filter: filter_condition &= Q(key=key_filter)
    if priority_filter: filter_condition &= Q(priority=priority_filter)
    if status_filter: filter_condition &= Q(status=status_filter)
    if assignee_filter: filter_condition &= Q(assignee=assignee_filter)
    if reporter_filter: filter_condition &= Q(reporter=reporter_filter)
        
    # Get value from 2 table in DB               
    table1 = issue_data_table.objects.filter(filter_condition)
    table2 = issue_data_table_KVHS.objects.filter(filter_condition)
    tasks = list(table1) + list(table2)

    # Pagination
    page_number = request.GET.get('page', 1)
    paginator = Paginator(tasks, 20)  # 20 task each page, object devide tasks to many page
    page_obj = paginator.get_page(page_number)

    # Get unique value list for dropdown
    keys = sorted(set(issue_data_table.objects.values_list('key', flat=True)) |
                set(issue_data_table_KVHS.objects.values_list('key', flat=True)))
    priorities = sorted(set(issue_data_table.objects.values_list('priority', flat=True)) |
                        set(issue_data_table_KVHS.objects.values_list('priority', flat=True)))
    statuses = sorted(set(issue_data_table.objects.values_list('status', flat=True)) |
                    set(issue_data_table_KVHS.objects.values_list('status', flat=True)))
    assignees = sorted(set(issue_data_table.objects.values_list('assignee', flat=True)) |
                    set(issue_data_table_KVHS.objects.values_list('assignee', flat=True)))
    reporters = sorted(set(issue_data_table.objects.values_list('reporter', flat=True)) |
                    set(issue_data_table_KVHS.objects.values_list('reporter', flat=True)))

    return render(request, 'task_list.html', {
        'page_obj': page_obj,
        'query': query,
        'keys': keys,
        'priorities': priorities,
        'statuses': statuses,
        'assignees': assignees,
        'reporters': reporters,
        'filters': {
            'key': key_filter,
            'priority': priority_filter,
            'status': status_filter,
            'assignee': assignee_filter,
            'reporter': reporter_filter
        },
        'show_background': False
    }) 

def document(request):
    return render(request, 'document.html', {'show_background': False})

def report(request):
    return render(request, 'report.html', {'show_background': False})

# ---------- Tool ----------
def tool(request):
    tools = [
        {"name": "Tool 1", "id": "tool1"},
        {"name": "Tool 2", "id": "tool2"},
    ]
    return render(request, 'tool.html', {
        'show_background': False,
        "tools": tools
    })
    

def run_tool(request, tool_id):
    try:
        # Import module main.py của tool tương ứng
        module = importlib.import_module(f"myapp.tools.{tool_id}.main")   # Import file main.py of tool
        result = module.run()  # Gọi hàm run() trong main.py
        messages.success(request, f"✅ {tool_id} executed successfully!")
    except Exception as e:
        messages.error(request, f"❌ Error running {tool_id}: {str(e)}")
        
    # Redirect về trang Tool
    return redirect('tool')   #The Django messages framework is designed to keep "messages" across redirects without passing them through the URL.
    




