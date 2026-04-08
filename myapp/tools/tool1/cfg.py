USERNAME = "xuanhien.dong@hyundai-kefico.com"
PASSWORD = "Thutrang2001!"

LOGIN_PAYLOAD = {"username":"xuanhien.dong@hyundai-kefico.com","password":"Thutrang2001!","rememberMe":False,"targetUrl":"","captchaId":""}
LOGIN_HEADER = {
    'Accept': '*/*',
    'Accept-Encoding': 'gzip, deflate, br, zstd',
    'Accept-Language': 'en-US,en;q=0.9',
    'Cache-Control': 'max-age=0',
    'Connection': 'keep-alive',
    'Content-Length': '121',
    'Content-Type': 'application/json',
    'Host': 'jira.hmg-corp.io',
    'Origin': 'https://jira.hmg-corp.io',
    'Referer': 'https://jira.hmg-corp.io/login.jsp',
    'Sec-Fetch-Dest': 'empty',
    'Sec-Fetch-Mode': 'cors',
    'Sec-Fetch-Site': 'same-origin',
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/140.0.0.0 Safari/537.36 Edg/140.0.0.0',
    'sec-ch-ua': '"Chromium";v="140", "Not=A?Brand";v="24", "Microsoft Edge";v="140"',
    'sec-ch-ua-mobile': '?0',
    'sec-ch-ua-platform': "Windows",
 
}

LOGIN_POST_URL = r'https://jira.hmg-corp.io/rest/tsv/1.0/authenticate?os_authType=none' # The URL the login form submits to
ALL_ISSUES_PAGE_URL = 'https://jira.hmg-corp.io/projects/KVHS?filter=allissues' # Page after successful login

EXCEL_FILE = "jira_issues.xlsx"

ALL_ISSUES_PAGE_URL_KVHS = 'https://jira.hmg-corp.io/browse/KVHSSDT-31'