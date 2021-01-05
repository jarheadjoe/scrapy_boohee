import urllib.request
import pandas as pd
import time,os
import math
path  = './img_'




def download(id,url,type):
    url = str(url)
    if url !='nan':
        filename=id+'_'+type+'.'+url.split('.')[-1]  #[-1]表示倒数第一个。[-2]表示倒数第二个。这里是为了处理链接的格式,因为要把链接的一部分当做图片名字的
        if not os.path.exists(path+type+'/' + filename):
            urllib.request.urlretrieve(url,path+type+'/' + filename)



data  = pd.read_csv('all.csv',encoding='gbk')
for index, row in data.iterrows():
    id = row['id']
    b_url = row['大图片地址']
    s_url = row['小图片地址']
    t_url = row['红绿灯地址']
    download(id,b_url,'big')
    # time.sleep(0.01)
    download(id,s_url,'small')
    # time.sleep(0.01)
    download(id,t_url,'traffic')
    # time.sleep(0.01)

