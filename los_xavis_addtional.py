import requests

password=''
URL='http://los.eagle-jump.org/xavis_fd4389515d6540477114ec3c79623afe.php?'
query={'pw': chr(184)+chr(249)+chr(197)+chr(176)+chr(198)+chr(208)+chr(196)+chr(161)+chr(164)+chr(187)}
headers = {'Content-Type': 'application/json; charset=utf-8'}
cookies = {'PHPSESSID': 'ean08as37ebof2v307j3kurer3'}
res=requests.get(URL, params=query, headers=headers, cookies=cookies)
if("Hello admin" in res.text):
    print("com")