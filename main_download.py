import tool_file
import json
import requests

# 根据json文件中的内容下载，下载主函数
def main_download():
    json_str = input("请输入要载入的json文件路径：")
    folder = input("请输入目标文件夹路径")
    ALL_IMG_ID_LIST = json.loads(tool_file.read(json_str,'r'))
    # 解析字典列表，分别构造出url，调用下载
    for i in ALL_IMG_ID_LIST:
        index = 1
        print(i['date']+'的图片开始下载')
        for img_id in i['img_id_list']:
            imgurl = 'https://wx2.sinaimg.cn/large/'+img_id["pid"]+'.jpg'

            with open (folder+"/"+i["date"]+"第"+str(index)+"张.jpg",'wb') as fp:
                fp.write(requests.get(imgurl).content)

            print("当前文章第"+str(index)+"张图片下载完成")
            index += 1
        print(i['date']+'的图片下载完成')
        
main_download()
