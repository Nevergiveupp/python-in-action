import urllib.request
import urllib.parse
import jsonpath
import json
import os
import time


def main():
    print("开始工作……")
    timestart = time.time()
    cardClasses = ["druid", "hunter", "mage", "paladin", "priest", "rogue", "shaman", "warlock", "warrior", "neutral"]

    lushi_urls = 'https://hs.blizzard.cn/action/cards/query'
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/78.0.3904.108 Safari/537.36'
    }

    for cardClass in cardClasses:
        if not os.path.exists(cardClass):
            os.mkdir(cardClass)
        print("开始爬{}了".format(cardClass))
        for p in range(1, 60):
            print(p)
            try:
                lushi_urls = 'https://hs.blizzard.cn/action/cards/query'
                headers = {
                    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/90.0.4430.93 Safari/537.36'
                }
                data = {
                    'cost': '',
                    'cardClass': cardClass,
                    'keywords': '',
                    'standard': '1',
                    't': int(time.time()),
                    'cardSet': '',
                    'p': p
                }
                data = urllib.parse.urlencode(data).encode("utf-8")
                request = urllib.request.Request(url=lushi_urls, headers=headers, data=data)
                response = urllib.request.urlopen(request)
                content = response.read().decode('utf-8')
                jsondict = json.loads(content)
                card_names = jsonpath.jsonpath(jsondict, '$..cards..name')
                card_pics = jsonpath.jsonpath(jsondict, '$..cards..pic')
                for i in range(len(card_names)):
                    card_path = cardClass + "/" + card_names[i] + ".png"
                    urllib.request.urlretrieve(url=card_pics[i], filename=card_path)
            except:
                continue
    timeend = time.time()
    print("一共用时：{}秒".format(timeend - timestart))


if __name__ == "__main__":
    main()
    print("爬取完成！")
