import requests

cookies = {
    'UOR': 'www.google.com,weibo.com,www.google.com',
    'SINAGLOBAL': '5855514105034.088.1719921168185',
    'SCF': 'ApaVGeHPezEAkTPWcMQ7OcTRb5D8YkUxRP9ad9nPAw6YysB7CHvxqxSTmfV3eTFXg1mqEkU0JGg4jAlxT8XO3Xw.',
    'SUB': '_2A25K_sTQDeRhGeBJ7loS9yrMwj-IHXVmclgYrDV8PUNbmtAbLROmkW9NRlR2Dp472Q7IHoxtp3Y74fooy6MmjY6V',
    'SUBP': '0033WrSXqPxfM725Ws9jqgMF55529P9D9WFji-ulwom.cApIyXB.RcPR5NHD95QcS0-Re0MXeh.0Ws4DqcjMi--NiK.Xi-2Ri--ciKnRi-zNSoMf1heNSh54e7tt',
    'XSRF-TOKEN': '-oaYltmtgzHLdS2EPpryNKQ-',
    '_s_tentry': 'weibo.com',
    'Apache': '1701665675411.883.1744639485978',
    'ULV': '1744639486006:9:3:3:1701665675411.883.1744639485978:1744537923822',
    'WBPSESS': '_Cyby0UYZv6huqkL7ifVbatVwoZhZA18axAJ5coXUk86UE1JT1nWVG3yjNShlo85w69LOtp9tyEYZ1JtB7AxhE2nO1e6eOwrBXR7CS8SWhdtJf29ip7Jg-XADCyy06B9FfMrBRpdqgtvQGavUtRQFg==',
}

headers = {
    'accept': 'application/json, text/plain, */*',
    'accept-language': 'zh-CN,zh;q=0.9',
    'cache-control': 'no-cache',
    'client-version': 'v2.47.52',
    'pragma': 'no-cache',
    'priority': 'u=1, i',
    'referer': 'https://weibo.com/u/7250241260?tabtype=album',
    'sec-ch-ua': '"Google Chrome";v="135", "Not-A.Brand";v="8", "Chromium";v="135"',
    'sec-ch-ua-mobile': '?0',
    'sec-ch-ua-platform': '"Windows"',
    'sec-fetch-dest': 'empty',
    'sec-fetch-mode': 'cors',
    'sec-fetch-site': 'same-origin',
    'server-version': 'v2025.04.14.3',
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/135.0.0.0 Safari/537.36',
    'x-requested-with': 'XMLHttpRequest',
    'x-xsrf-token': '-oaYltmtgzHLdS2EPpryNKQ-',
    # 'cookie': 'UOR=www.google.com,weibo.com,www.google.com; SINAGLOBAL=5855514105034.088.1719921168185; SCF=ApaVGeHPezEAkTPWcMQ7OcTRb5D8YkUxRP9ad9nPAw6YysB7CHvxqxSTmfV3eTFXg1mqEkU0JGg4jAlxT8XO3Xw.; SUB=_2A25K_sTQDeRhGeBJ7loS9yrMwj-IHXVmclgYrDV8PUNbmtAbLROmkW9NRlR2Dp472Q7IHoxtp3Y74fooy6MmjY6V; SUBP=0033WrSXqPxfM725Ws9jqgMF55529P9D9WFji-ulwom.cApIyXB.RcPR5NHD95QcS0-Re0MXeh.0Ws4DqcjMi--NiK.Xi-2Ri--ciKnRi-zNSoMf1heNSh54e7tt; XSRF-TOKEN=-oaYltmtgzHLdS2EPpryNKQ-; _s_tentry=weibo.com; Apache=1701665675411.883.1744639485978; ULV=1744639486006:9:3:3:1701665675411.883.1744639485978:1744537923822; WBPSESS=_Cyby0UYZv6huqkL7ifVbatVwoZhZA18axAJ5coXUk86UE1JT1nWVG3yjNShlo85w69LOtp9tyEYZ1JtB7AxhE2nO1e6eOwrBXR7CS8SWhdtJf29ip7Jg-XADCyy06B9FfMrBRpdqgtvQGavUtRQFg==',
}

params = {
    'uid': '7250241260',
    'sinceid': '0',
    'has_album': 'true',
}