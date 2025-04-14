# 本文件的主要功能就是根据输入的信息进行下载操作了

import tool_file
import json
import requests
import os
from tqdm import tqdm


# 根据json文件中的内容下载，下载主函数
def main_download(ALL_IMG_ID_LIST,folder,username):
    # 创建个文件夹
    try:
        os.mkdir(os.path.join(folder,username))
    except:
        print("文件夹已存在")
    # 计算总有多少张图片
    all_img_count =  0
    for i in ALL_IMG_ID_LIST:
        for j in i:
            all_img_count += 1
   

    with tqdm(total=all_img_count) as pbar:
        pbar.set_description('正在下载，进度')
        # 解析字典列表，分别构造出url，调用下载
        for i in ALL_IMG_ID_LIST:
            index = 1
            # print(i['date']+'的图片开始下载')
            for img_id in i['img_id_list']:
                imgurl = 'https://wx2.sinaimg.cn/large/'+img_id["pid"]+'.jpg'

                with open (os.path.join(folder,username,i["date"]+"_"+str(index)+".jpg"),'wb') as fp:
                    fp.write(requests.get(imgurl).content)

               
                pbar.update(1)
                index += 1
           


# 被导入时不会默认运行
if __name__ == '__main__':

    print("当前JSONS文件夹中有如下文件，请输入编号进行选择：")
    json_list = os.listdir("JSONS")
    for i in range(len(json_list)):
        print(i+1,json_list[i])
        
    # 解析输入的数字
    num = int(input("请输入数字选择你要下载的选项："))
    json_path = os.path.join("JSONS",json_list[num-1])
    print(json_list)

    folder = input("请输入目标文件夹路径,置空则默认在本目录下output文件夹")
    if (folder==""):
        folder = "output"

    # 读取json文件
    ALL_IMG_ID_LIST = json.loads(tool_file.read(json_path,'r'))

    print(json_path)
    username = json_list[num-1].replace(".json","")
    main_download(ALL_IMG_ID_LIST,folder,username)


