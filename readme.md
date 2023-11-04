## 本代码用来将微博的相册批量下载/知乎作为附加
### 1.各个模块
#### 一共提供了3个模块，其中，
file作为工具模块，封装了with open，
headers封装了requests 需要的请求头，
#### JSONS文件夹存储了输出的json文件，其中pid 即是图片地址，

### 2.使用方法
tojson.py,根据提示操作,用户的uid在浏览器地址栏中可以查看
tojson.py默认只导出json,文件的下载须手动调用main_download()方法，

