from .cfg import *
import requests
from bs4 import BeautifulSoup
from bs4 import BeautifulSoup as bs
import html
from datetime import datetime, timedelta
from openpyxl import Workbook, load_workbook
import os 

def SESSION(LOGIN_POST_URL, LOGIN_PAYLOAD, LOGIN_HEADER):
    try:
        with requests.Session() as session:

            response_login = session.post(LOGIN_POST_URL, data=LOGIN_PAYLOAD, headers=LOGIN_HEADER)
            # with open('index.html', 'w', encoding='utf-8') as f:
            #     f.write(response_login.text)
            response_login.raise_for_status() # Check for login errors
            print(f"Login response status code: {response_login.status_code}")
            if response_login.status_code == 200:
                print("Login successful!")
            else:
                print("Login failed. Check credentials or website structure.")
            return session
        
    except requests.exceptions.RequestException as e:
        print(f"Error during request: {e}")
        return None
    except Exception as e:
        print(f"An unexpected error occurred: {e}")
        return None
    
def get_all_keys(session, all_issues_page_url):
    # == Step 1: Downloading the page ==
    all_issues_rq = session.get(all_issues_page_url)
    data = all_issues_rq.text
    # with open('index.html', 'w', encoding='utf-8') as f:
    #     f.write(data)
        
    # == Step 2: Parsing HTML ==
    pdata = bs(data, 'html.parser')
    script_all_data = pdata.find('body').find_all('script')
    
    # == Step 3: Finding the Target script ==
    rq_data = ''
    for d in script_all_data:
        if 'com.atlassian.jira.jira-issue-navigator-components:search-data' in d.text:
            rq_data = d
            break
    if rq_data == '':
        return None
    
    # == Step 4: Extracting the Right Line ==
    lines = rq_data.text.splitlines() 
    need_line = ''
    for l in lines:
        if 'com.atlassian.jira.jira-issue-navigator-components:search-data' in l:
            need_line = l
            break
        
    # == Step 5: Clean Excaped Quotes ==
    need_line = need_line.replace('\\u0022', '"')
    
    # == Step 6: Find the "issueKeys" Part ==
    start_index = need_line.find('\"issueKeys\":') + 13 # Find the opening quote before the curly brace
    end_index = need_line.rfind(',\"jiraHasIssues\"') - 1# Find the closing curly brace before the ending quote
    
    # == Step 7: Extract the Raw Keys ==
    if start_index != -1 and end_index != -1 and start_index < end_index:
        inner_string_value = need_line[start_index:end_index]
        inner_string_value = inner_string_value.replace('"','')
        issue_key_list = inner_string_value.split(',')
        print(issue_key_list)
        return issue_key_list
    
def export_xml_data(session, key):
    print(f"KEY: {key}")
    jira_request_url = f'https://jira.hmg-corp.io/si/jira.issueviews:issue-xml/{key}/{key}.xml' # jira request url
    print(f"jira_request_url: {jira_request_url}")
    jira_rq = session.get(jira_request_url)
    xml_data = jira_rq.text
    # Giải mã HTML entities (chuyển &lt thành <, &gt thành >, v.v.), .xml format có định dạng cũ như vậy để không phá vỡ cấu trúc khi nhúng vào html
    xml_data = html.unescape(xml_data)
    # with open('xml_data.html', 'w', encoding='utf-8') as f:
    #     f.write(xml_data)
    return xml_data

def tracking_xml_data(xml_data, key):
    obj_xml_data = bs(xml_data, 'html.parser')
    
    # == Get common ==
    obj_item = obj_xml_data.find("item")
    obj_description = obj_item.find("description")
    
    # == Get request_title ==
    request_title = obj_item.find("title").text
    try:
        request_title = obj_item.find("title").text
        signs = request_title.find("]") + 1
        request_title = request_title[signs:].lstrip()
        print(f"request_title: {request_title}")
    except Exception as e:
        request_title = None
        print(f"request_title error: {e}")

    # == Get priority ==
    try:
        priority = obj_item.find("priority").text 
        print(f"priority: {priority}")
    except Exception as e:
        priority = None
        print(f"priority error: {e}")
        
    # == Get reporter ==
    try:
        reporter = obj_item.find("reporter").text
        print(f"reporter: {reporter}")
    except Exception as e:
        reporter = None
        print(f"reporter error: {e}")

    # == Get assignee ==
    try:
        assignee = obj_item.find("assignee").text
        print(f"assignee: {assignee}")
    except Exception as e:
        assignee = None
        print(f"assignee error: {e}")    
        
    # == Get status ==
    try:
        status = obj_item.find("status").text
        print(f"status: {status}")
    except Exception as e:
        status = None
        print(f"status error: {e}")      
    
    two_hours_delta = timedelta(hours=2)
    # == Get created ==
    try:
        created = obj_item.find("created").text
        datetime_object = datetime.strptime(created, "%a, %d %b %Y %H:%M:%S %z") - two_hours_delta
        created = datetime_object.strftime('%Y-%m-%d %H:%M:%S')
        print(f"created: {created}")
    except Exception as e:
        created = None
        print(f"created error: {e}")  
        
    # == Get updated ==
    try:
        updated = obj_item.find("updated").text
        datetime_object = datetime.strptime(updated, "%a, %d %b %Y %H:%M:%S %z") - two_hours_delta
        updated = datetime_object.strftime('%Y-%m-%d %H:%M:%S')
        print(f"updated: {updated}")
    except Exception as e:
        created = None
        print(f"updated error: {e}")  
    
    issue_data = (
        key,
        request_title,
        priority,
        reporter,
        assignee,
        status,
        created,
        updated
    )   
    return issue_data  

def append_to_excel(ws, issue_data):
    key = issue_data[0]
    found = False
    
    for row in ws.iter_rows(min_row=2, values_only=False):   # Skip header
        if row[0].value == key:
            # Update the existing row
            for i in range(1, len(issue_data)):
                row[i].value = issue_data[i]
            found = True
            break
    if not found:
        # Append new row
        ws.append(issue_data)


def get_all_keys_KVHS(session, all_issues_page_url_kvhs):
    # == Step 1: Downloading the page ==
    all_issues_rq = session.get(all_issues_page_url_kvhs)
    data = all_issues_rq.text
    # with open('index.html', 'w', encoding='utf-8') as f:
    #     f.write(data)
        
    # == Step 2: Parsing HTML ==
    pdata = bs(data, 'html.parser')
    
    # == Step 3: Finding the table by ID ==
    table = pdata.find("table", id="ghx-issues-in-epic-table")
    
    # == Step 4: Finding all rows in the table ==
    rows = table.find_all("tr", class_="issuerow")
    
    # == Step 5: Extract issue keys from the second <td> with class "nav ghx-minimal" ==
    issue_key_list = []
    for row in rows:
        issue_key = row["data-issuekey"]
        issue_key_list.append(issue_key)
    print(issue_key_list)
    return issue_key_list




   
  