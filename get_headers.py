import requests


cookies = {
    'SINAGLOBAL': '1845421966748.706.1681844419370',
    'PC_TOKEN': '2c1afcba29',
    'wb_view_log': '1280*7201.5',
    'SUB': '_2A25IEdNXDeRhGeBM71QT9CnOyjSIHXVr_f0frDV8PUJbkNANLRnNkW1NRP0JyzBH0w2BHaPAQY_YgAX-2NfISBMx',
    'SUBP': '0033WrSXqPxfM725Ws9jqgMF55529P9D9WWlnb7dMd7-Z-ESJYDqm9hX5NHD95QceoBceoBNeo2RWs4DqcjYi--Ri-2Ei-8Fi--4i-20iKy8i--fiK.7i-z4i--ciK.fi-20i--NiKLWiKnXi--Xi-iWi-iWdsvV9NLf',
    'XSRF-TOKEN': 'S5V1eUx8C3WKdRrIcmeaqGIS',
    '_s_tentry': 'weibo.com',
    'Apache': '4283993956910.004.1695917688111',
    'ULV': '1695917688179:6:3:3:4283993956910.004.1695917688111:1695916654220',
    'WBPSESS': 'Prog0-43KpazQQeV_6sfCxrJhNgAsT1eRpZkcaUdFgQpyXGyKQwKcDHKBB68DrhOFk28LDGo9Pkv8G7tPoHMLj9zjx90SlhTSuFWwVTQqOstWyWZsMWOYk3OnIxIygVFjj710E8J_6PJ7xsGVcduFw==',
}

headers = {
    'authority': 'weibo.com',
    'accept': 'application/json, text/plain, */*',
    'accept-language': 'zh-CN,zh;q=0.9',
    'client-version': 'v2.43.43',
    # 'cookie': 'SINAGLOBAL=1845421966748.706.1681844419370; PC_TOKEN=2c1afcba29; wb_view_log=1280*7201.5; SUB=_2A25IEdNXDeRhGeBM71QT9CnOyjSIHXVr_f0frDV8PUJbkNANLRnNkW1NRP0JyzBH0w2BHaPAQY_YgAX-2NfISBMx; SUBP=0033WrSXqPxfM725Ws9jqgMF55529P9D9WWlnb7dMd7-Z-ESJYDqm9hX5NHD95QceoBceoBNeo2RWs4DqcjYi--Ri-2Ei-8Fi--4i-20iKy8i--fiK.7i-z4i--ciK.fi-20i--NiKLWiKnXi--Xi-iWi-iWdsvV9NLf; XSRF-TOKEN=S5V1eUx8C3WKdRrIcmeaqGIS; _s_tentry=weibo.com; Apache=4283993956910.004.1695917688111; ULV=1695917688179:6:3:3:4283993956910.004.1695917688111:1695916654220; WBPSESS=Prog0-43KpazQQeV_6sfCxrJhNgAsT1eRpZkcaUdFgQpyXGyKQwKcDHKBB68DrhOFk28LDGo9Pkv8G7tPoHMLj9zjx90SlhTSuFWwVTQqOstWyWZsMWOYk3OnIxIygVFjj710E8J_6PJ7xsGVcduFw==',
    'referer': 'https://weibo.com/u/1850920525?tabtype=album',
    'sec-ch-ua': '"Google Chrome";v="117", "Not;A=Brand";v="8", "Chromium";v="117"',
    'sec-ch-ua-mobile': '?0',
    'sec-ch-ua-platform': '"Windows"',
    'sec-fetch-dest': 'empty',
    'sec-fetch-mode': 'cors',
    'sec-fetch-site': 'same-origin',
    'server-version': 'v2023.09.23.1',
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/117.0.0.0 Safari/537.36',
    'x-requested-with': 'XMLHttpRequest',
    'x-xsrf-token': 'S5V1eUx8C3WKdRrIcmeaqGIS',
}

params = {
    'uid': '1850920525',
    'sinceid': '0',
    'has_album': 'true',
}
