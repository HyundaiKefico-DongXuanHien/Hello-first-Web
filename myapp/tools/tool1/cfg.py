USERNAME = "xuanhien.dong@hyundai-kefico.com"
PASSWORD = "Kimhan2001!"

LOGIN_PAYLOAD = {
    'os_username': f'{USERNAME}', # Replace with the actual name of the username field
    'os_password': f'{PASSWORD}', # Replace with the actual name of the password field
    'os_destination': None,
    'user_role': None,
    'alt_token': None,
    'login': 'Log In'
}
LOGIN_HEADER = {
    'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7',
    'accept-encoding': 'gzip, deflate, br, zstd',
    'host': 'jira.hmg-corp.io',
    'origin': 'https://jira.hmg-corp.io',
    'referer': 'https://jira.hmg-corp.io/login.jsp',
    'connection': 'keep-alive',
    'sec-ch-ua': '"Microsoft Edge";v="131", "Chromium";v="131", "Not_A Brand";v="24"',
    'sec-ch-ua-mobile': '?0',
    'sec-ch-ua-platform': "Windows",
    'sec-fetch-dest': 'document',
    'sec-fetch-mode': 'navigate',
    'sec-fetch-site': 'same-origin',
    'sec-fetch-user': '?1',
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/131.0.0.0 Safari/537.36 Edg/131.0.0.0',
    "Content-Type": "application/x-www-form-urlencoded"
}

LOGIN_POST_URL = 'https://jira.hmg-corp.io/login.jsp' # The URL the login form submits to
ALL_ISSUES_PAGE_URL = 'https://jira.hmg-corp.io/projects/KVHS?filter=allissues' # Page after successful login

EXCEL_FILE = "jira_issues.xlsx"

ALL_ISSUES_PAGE_URL_KVHS = 'https://jira.hmg-corp.io/browse/KVHSSDT-31'