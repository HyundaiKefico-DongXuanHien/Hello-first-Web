# ============================================================================
# FILE NAME     : myapp/models.py
# AUTHOR        : DONG XUAN HIEN
# DIVISION      : HYUNDAI KEFICO Co.,Ltd.
# DESCRIPTION   : Mapping data from database to Model
# HISTORY       : 05/11/2025, 13/02/2026, 09/03/2026
# ============================================================================

from django.db import models

class issue_data_table(models.Model):
    key = models.CharField(max_length=50, primary_key=True)
    request_title = models.TextField()
    priority = models.CharField(max_length=20)
    reporter = models.TextField()
    assignee = models.TextField()
    status = models.CharField(max_length=20)
    created = models.TextField()
    updated = models.TextField()
    due = models.TextField()

    class Meta:
        db_table = 'issue_data_table'  # mapping to available table

class issue_data_table_KVHS(models.Model):
    key = models.CharField(max_length=50, primary_key=True)
    request_title = models.TextField()
    priority = models.CharField(max_length=20)
    reporter = models.TextField()
    assignee = models.TextField()
    status = models.CharField(max_length=20)
    created = models.TextField()
    updated = models.TextField()
    due = models.TextField()

    class Meta:
        db_table = 'issue_data_table_KVHS'

class ticket_log_table(models.Model):
    time = models.TextField(primary_key=True)
    name = models.TextField()
    note = models.TextField()
    project_name = models.TextField()
    requester = models.TextField()

    class Meta:
        db_table = 'ticket_log_table'  # exact table name in ticket_log.dtb

