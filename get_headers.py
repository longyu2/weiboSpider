import requests

cookies = {
    'SINAGLOBAL': '5265262389763.914.1699073622419',
    'UOR': ',,www.google.com',
    'XSRF-TOKEN': 'o6KY2gupr6gn7Biod1HnFSie',
    '_s_tentry': 'weibo.com',
    'Apache': '7711192078043.168.1703233956781',
    'ULV': '1703233956821:5:2:1:7711192078043.168.1703233956781:1701618703564',
    'PC_TOKEN': '5c7abac3b5',
    'login_sid_t': '6977cf8eabc1b2828135821ba455acb8',
    'cross_origin_proto': 'SSL',
    'WBStorage': '267ec170|undefined',
    'wb_view_log': '1920*10801',
    'WBtopGlobal_register_version': '2023122216',
    'crossidccode': 'CODE-yf-1RgAXP-0-GOJdRK5UoaRMkXsaf5ca8',
    'SSOLoginState': '1703233984',
    'SUB': '_2A25IgTmQDeRhGeBM71QT9CnOyjSIHXVr_zNYrDV8PUJbkNANLUjwkW1NRP0Jy1fIECbQ5KUacqQn-SvRpLEcFUtn',
    'SUBP': '0033WrSXqPxfM725Ws9jqgMF55529P9D9WWlnb7dMd7-Z-ESJYDqm9hX5NHD95QceoBceoBNeo2RWs4DqcjYi--Ri-2Ei-8Fi--4i-20iKy8i--fiK.7i-z4i--ciK.fi-20i--NiKLWiKnXi--Xi-iWi-iWdsvV9NLf',
    'WBPSESS': 'Prog0-43KpazQQeV_6sfCxrJhNgAsT1eRpZkcaUdFgQpyXGyKQwKcDHKBB68DrhOFk28LDGo9Pkv8G7tPoHMLhum9Vv8XKG5Rj_n4GNIIdHKeGy4cd40uCFzQjxBweO329WNVhFUWN7WWjy4WZzhdg==',
}

headers = {
    'authority': 'weibo.com',
    'accept': 'application/json, text/plain, */*',
    'accept-language': 'zh-CN,zh;q=0.9',
    'client-version': 'v2.44.42',
    # 'cookie': 'SINAGLOBAL=5265262389763.914.1699073622419; UOR=,,www.google.com; XSRF-TOKEN=o6KY2gupr6gn7Biod1HnFSie; _s_tentry=weibo.com; Apache=7711192078043.168.1703233956781; ULV=1703233956821:5:2:1:7711192078043.168.1703233956781:1701618703564; PC_TOKEN=5c7abac3b5; login_sid_t=6977cf8eabc1b2828135821ba455acb8; cross_origin_proto=SSL; WBStorage=267ec170|undefined; wb_view_log=1920*10801; WBtopGlobal_register_version=2023122216; crossidccode=CODE-yf-1RgAXP-0-GOJdRK5UoaRMkXsaf5ca8; SSOLoginState=1703233984; SUB=_2A25IgTmQDeRhGeBM71QT9CnOyjSIHXVr_zNYrDV8PUJbkNANLUjwkW1NRP0Jy1fIECbQ5KUacqQn-SvRpLEcFUtn; SUBP=0033WrSXqPxfM725Ws9jqgMF55529P9D9WWlnb7dMd7-Z-ESJYDqm9hX5NHD95QceoBceoBNeo2RWs4DqcjYi--Ri-2Ei-8Fi--4i-20iKy8i--fiK.7i-z4i--ciK.fi-20i--NiKLWiKnXi--Xi-iWi-iWdsvV9NLf; WBPSESS=Prog0-43KpazQQeV_6sfCxrJhNgAsT1eRpZkcaUdFgQpyXGyKQwKcDHKBB68DrhOFk28LDGo9Pkv8G7tPoHMLhum9Vv8XKG5Rj_n4GNIIdHKeGy4cd40uCFzQjxBweO329WNVhFUWN7WWjy4WZzhdg==',
    'referer': 'https://weibo.com/u/1705586121?tabtype=album',
    'sec-ch-ua': '"Not_A Brand";v="8", "Chromium";v="120", "Google Chrome";v="120"',
    'sec-ch-ua-mobile': '?0',
    'sec-ch-ua-platform': '"Windows"',
    'sec-fetch-dest': 'empty',
    'sec-fetch-mode': 'cors',
    'sec-fetch-site': 'same-origin',
    'server-version': 'v2023.12.21.3',
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36',
    'x-requested-with': 'XMLHttpRequest',
    'x-xsrf-token': 'o6KY2gupr6gn7Biod1HnFSie',
}

params = {
    'uid': '1705586121',
    'sinceid': '0',
    'has_album': 'true',
}
