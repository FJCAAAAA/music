"""
File name : download_music.py.py
Create file time: 2023/8/28 21:07
File Create By Author : fengjicheng
"""
import random
import re
import requests
import urllib3
import json
from . import user_agent
# import user_agent
from datetime import datetime


class DownMusic(object):
    def __init__(self, music_name):
        self.header = {
            'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
            'Accept-Language': 'zh-CN,zh;q=0.8,zh-TW;q=0.7,zh-HK;q=0.5,en-US;q=0.3,en;q=0.2',
            'Connection': 'close',
            'User-Agent': random.choice(user_agent.pcUserAgent)
        }
        if ' ' in music_name:
            self.music_name = re.sub(' ', '+', music_name)
        else:
            self.music_name = music_name

    def get_music(self):
        url = "" # 第三方平台音乐下载接口，这里隐藏了，有需求可以联系作者。
        # data = json.dumps({"q":  self.music_name, "page": 0})
        data = {"q": self.music_name, "page": 0}
        try:
            urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)
            get_url = requests.post(url=url, data=data, headers=self.header, timeout=(20, 20), verify=False)
            content = get_url.content.decode('utf-8')
            pattern = r'\(|\);'
            result = re.sub(pattern, '', content)
        except:
            result = ""
        # print(result)
        return json.loads(result)

    def get_pic(self):
        pic_search_url = "https://bd.kuwo.cn/search/searchMusicBykeyWord?vipver=1&client=kt&ft=music&cluster=0&strategy=2012&encoding=utf8&rformat=json&mobi=1&issubtitle=1&show_copyright_off=1&pn=0&rn=20&all="
        music_name = self.music_name
        if "+" in music_name:
            music_name = re.sub('\+', ' ', music_name)
        pic_search_url = pic_search_url + music_name
        try:
            urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)
            get_url = requests.get(pic_search_url, headers=self.header, timeout=(20, 20), verify=False)
            resp_dict = json.loads(get_url.content.decode('utf-8'))
            uri_list = resp_dict.get("abslist")
            uri = ""
            for i in uri_list:
                uri_1 = i.get("web_albumpic_short")
                # uri_1 = i.get("web_artistpic_short")
                if uri_1:
                    uri = uri_1
                    break
            url = "https://img2.kuwo.cn/star/albumcover/" + uri
            # url = "https://img4.kuwo.cn/star/starheads/" + uri

        except:
            url = ""
        return url


    def run(self):
        data = self.get_music()
        pic = self.get_pic()
        music_list = []
        if data['response'] and len(data['response']) > 1:
            for i in data['response'][1:]:
                date = datetime.fromtimestamp(i['date']).strftime('%Y-%m-%d %H:%M:%S')
                music_list.append({'id': i['id'], 'name': i['title'], 'artist': i['artist'], 'album': i['title'], 'duration': i['duration'], 'released_data': date, 'pic': pic, 'url': i['url']})
        return music_list


if __name__ == '__main__':
    o = DownMusic("empty love")
    data = o.run()
    print(data)