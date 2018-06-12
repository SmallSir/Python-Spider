import requests
from urllib.parse import urlencode
import os
from hashlib import md5
from multiprocessing.pool import Pool

#实现单个ajax的请求
def get_page(offset):
    params = {
        'offset':offset,
        'format':'json',
        'keyword':'Python',
        'autoload':'true',
        'count':'20',
        'cur_tab':'1',
        'from':'search_tab',
    }#设置参数
    url = 'https://www.toutiao.com/search_content/?' + urlencode(params)
    try:
        response = requests.get(url)
        if response.status_code == 200:
            return response.json()
    except requests.ConnectionError:
            return None

#解析每个数据中包含的图片链接
def get_image(json):
    if json.get('data'):
        for item in json.get('data'):
            title = item.get('title')
            try:
                images = item.get('image_list')
                for image in images:
                    url = 'http:' + image.get('url')
                    yield{
                        'image':   url,
                        'title':title,
                    }
            except TypeError:
                   yield{
                       'image':None,
                       'title':None,
                   }
#将图片下载下来
def save_image(item):
    if item.get('image') == None:
        pass
    else:
        if not os.path.exists(item.get('title')):
            os.mkdir(item.get('title'))
        try:
            response = requests.get(item.get('image'))
            if response.status_code == 200:
                file_path = '{0}/{1}.{2}'.format(item.get('title'),md5(response.content).hexdigest(),'jpg')
                if not os.path.exists(file_path):
                    with open(file_path,'wb') as f:
                        f.write(response.content)
                else:
                    print('Already Downloaded',file_path)
        except:
            print('Failed to Save Image')


def main(offset):
    json = get_page(offset)
    for item in get_image(json):
        print(item)
        save_image(item)


GROUP_START = 0
GROUP_END = 0
if __name__ == '__main__':
    pool = Pool()
    group = ([x * 20 for x in range(GROUP_START, GROUP_END + 1)])
    pool.map(main, group)
    pool.close()
    pool.join()

