import time
from .jira_scan import *
from .interact_dtb import *

def run():
    '''========== TRACKING KGP =========='''
    session = SESSION(LOGIN_POST_URL, LOGIN_PAYLOAD, LOGIN_HEADER)
    issue_key_list = get_all_keys(session, ALL_ISSUES_PAGE_URL)
    issue_key_list.reverse()
    
    # Save into database
    for key in issue_key_list:
        xml_data = export_xml_data(session, key)
        issue_data = tracking_xml_data(xml_data, key)   
        save_issue_to_database(issue_data)
          
    
    '''========== TRACKING KVHS =========='''
    issue_key_list = get_all_keys_KVHS(session, ALL_ISSUES_PAGE_URL_KVHS)
    
    # Save into database
    for key in issue_key_list:
        xml_data = export_xml_data(session, key)
        issue_data = tracking_xml_data(xml_data, key)   
        save_issue_to_database_KVHS(issue_data)   
    
    
    
    
    
    
    
    
    
    
    
