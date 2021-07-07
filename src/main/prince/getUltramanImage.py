import re
import requests

# 爬取所有奥特曼图片

# 声明 UA
headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/90.0.4430.85 Safari/537.36"
}
# 存储异常路径，防止出现爬取失败情况
errorList = []


# run方法
def run():
    url = "http://www.ultramanclub.com/allultraman/"
    try:
        res = requests.get(url=url, timeout=10)
        res.encoding = "gb2312"
        html = res.text
        return getLinks(html)
    except Exception as e:
        print("发生异常", e)


# 获取请求链接
def getLinks(html):
    startTag = '<ul class="lists">'
    start = html.find(startTag)
    html = html[start:]
    links = re.findall('<li class="item"><a href="(.*)">', html)
    print(
        links)  # ['./taiga/', './zett/', './trigger/', './tiga/', './zero/', './groob/', './ultraman/', './ultraseven/', './80/', './trigger/', './zett/', './reiga/', './taiga/', './titas/', './fuma/', './groob/', './grigio/', './tregear/', './ruebe/', './rosso/', './blu/', './geed/', './orb/', './x/', './ribut/', './ginga-victory/', './victory/', './ginga/', './saga/', './zero/', './belial/', './7x/', './hotto/', './motto/', './kitto/', './hikari/', './mebius/', './xenon/', './max/', './noa/', './nexus/', './thenext/', './boy/', './legend/', './pict/', './justice/', './cosmos/', './nice/', './agul/', './gaia/', './dyna/', './tiga', './zearth/', './ultraseven21/', './neos/', './powered/', './great/', './beth/', './chuck/', './scott/', './yullian/', './80/', './joneus/', './king/', './astra/', './leo/', './mother/', './taro/', './father/', './ace/', './jack/', './ultraseven/', './zoffy/', './ultraman/']
    # links = list(set(links)) # set去重
    links = [f"http://www.ultramanclub.com/allultraman/{i.split('/')[1]}/" for i in
             set(links)]  # 拼接url成 'http://www.ultramanclub.com/allultraman/xxx/' 的格式
    # print(links)
    return links


def getImg(url):
    try:
        # 网页访问速度慢，需要设置 timeout
        res = requests.get(url=url, headers=headers, timeout=15)
        res.encoding = "gb2312"
        html = res.text
        print(url)
        # 获取详情页标题，作为图片文件名
        title = re.search('<title>(.*?)\[', html).group(1)
        # 获取图片短连接地址
        image_short = re.search('<figure class="image tile">[.\s]*?<img src="(.*?)"', html).group(1)

        # 拼接完整图片地址
        img_url = "http://www.ultramanclub.com/allultraman/" + image_short[3:]
        # 获取图片数据
        img_data = requests.get(img_url).content
        print(f"正在爬取{title}")
        if title is not None and image_short is not None:
            with open(f"ultramanImg/{title}.png", "wb") as f:
                f.write(img_data)

    except Exception as e:
        print("*" * 100)
        print(url)
        print("请求异常", e)

        errorList.append(url)


if __name__ == '__main__':
    details = run()
    for detail in details:
        getImg(detail)

    while len(errorList) > 0:
        print("再次爬取")
        detail = errorList.pop()
        getImg(detail)
    print("数据全部爬取完毕")
