import requests
from requests.auth import HTTPBasicAuth

from urllib3.exceptions import InsecureRequestWarning

# Suppress only the single warning from urllib3 needed.
requests.packages.urllib3.disable_warnings(category=InsecureRequestWarning)

device_portal_url = "http://172.16.10.251:50080"
API_shutdown = "/api/control/shutdown"
API_restart = "/api/control/restart"

def WDP_API_Call(url, _API):
    payload={}
    headers = {
      'Authorization': 'Basic aHBlYWRtaW46cGFzc3dvcmQ=',
      'Cookie': 'CSRF-Token=E3DZKrh8rXGIYc4uhM3BkUu1gQfk2NcS'
    }

    headers = {
      'User-Agent': 'python'
    }
    response = requests.request("POST", device_portal_url+API_shutdown, verify=False, \
                        auth=HTTPBasicAuth('hpeadmin', 'password'), headers=headers)

    
    return response.text
    
WDP_API_Call(device_portal_url, API_shutdown)
