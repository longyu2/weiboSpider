import json
from tokenize import cookie_re
import requests
import get_headers
import tool_file

# 把sinceid转化为方便识别的日期格式
def sinceid_To_datestr(since_id):
    if(since_id =='0'):
        return 'error'
    str_out = ''
    try:
        date_str = since_id.split("_")[2]
        str_list = list(date_str)    # 字符串转list
        str_list.insert(4, "_")  # 在指定位置插入字符串
        str_list.insert(7, "_")  # 在指定位置插入字符串
        str_out = ''.join(str_list)    # 空字符连接
    except:
        return 'error'
    finally:
        return str_out

# 获取所有图片，并存储到json
def get_url_to_json():
    # 根据输入的数量，循环从接口获取数据并保存
    num = 1
    while(True) :
        response = requests.get('https://weibo.com/ajax/profile/getImageWall', params=params, cookies=cookies, headers=header)        
        print(response.text)
        json_dict = json.loads(response.text)
        since_id = str(json_dict["data"]["since_id"])
        print("sinceid是：")
        print(since_id)
        date_str = sinceid_To_datestr(since_id)
        if (date_str == 'error'):
            # 这里是做一个异常处理，如果sinceid不能正常解析，说明已经全部完成
            print("全部完成")
            break
        print("第"+str(num)+"篇图片地址获取完成，日期是："+date_str)
        params['sinceid'] = since_id    # 设置下次请求的sinceid

        # 数据以字典列表存储
        ALL_IMG_ID_LIST.append({"date":date_str,"img_id_list":json_dict["data"]["list"]})
        print("本次共有"+str(len(json_dict["data"]["list"]))+"张")
        
        num+=1
    # 将字典转化为json，并且存储到json文件中
    with open (''.join(['./JSONS/',json_name,'.json']),'w') as fp:
        fp.write(json.dumps(ALL_IMG_ID_LIST,ensure_ascii=False))



ALL_IMG_ID_LIST = []

# 从header中取出requests 请求头
params = get_headers.params
cookies = get_headers.cookies
header = get_headers.headers

# 循环调用接口，每次调用都需要发送一个sinceid ，然后返回的数据能够拿到下次的sinceid ，最后把所有数据放到一起即可
# 使用了字典列表的形式存储数据，构造为列表里的每一项是一个如{"date":"具体日期"，"img_id_list":{"pid":"pid的值","mid":"mid的值"}}这样的字典，其中pid就是图片的url了
# 加上 https://wx2.sinaimg.cn/large/  的前缀，就能构造出完整url

# 程序开始
print("欢迎使用微博相册下载程序")
params['uid'] = input("请输入uid:")

# params['uid'] = '5391368312'


json_name = input("请输入保存为的json文件名(无需后缀名):")
# json_name = "月瑶兰蝶"




get_url_to_json()

