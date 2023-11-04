# 本文件的主要功能就是根据输入的信息进行下载操作了

import tool_file
import json
import requests
from tqdm import tqdm
# 根据json文件中的内容下载，下载主函数
def main_download():
    # json_str = input("请输入要载入的json文件路径：")
    json_str = "./JSONS/走路摇.json"
    # folder = input("请输入目标文件夹路径")
    folder = r"C:\Users\25717\Desktop\tup"

    ALL_IMG_ID_LIST = json.loads(tool_file.read(json_str,'r'))
    

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

                with open (folder+"/"+i["date"]+"第"+str(index)+"张.jpg",'wb') as fp:
                    fp.write(requests.get(imgurl).content)

                # print("当前批次第"+str(index)+"张图片下载完成")
                # print("进度：")
                # print("%.0f%%" % ((index/len(i['img_id_list']) * 100)   ))    # 计算百分数
                pbar.update(1)
                index += 1
            # print(i['date']+'的图片下载完成')


# 被导入时不会默认运行
if __name__ == '__main__':
    main_download()


