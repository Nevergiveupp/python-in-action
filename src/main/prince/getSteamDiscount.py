import bs4
import requests
import codecs   # 解决文件编码问题

# Author: PrinceCheng
# Description: 爬取Steam所有打折游戏
# Date: 2021/06/08

def main():
    pageid = 1
    file = codecs.open("steamDiscountList.txt", "w+", "utf-8")   # a: 打开一个文件用于追加。如果该文件已存在，文件指针将会放在文件的结尾。也就是说，新的内容将会被写入到已有内容之后。如果该文件不存在，创建新文件进行写入。
                                                                 # w+: 打开一个文件用于读写。如果该文件已存在则打开文件，并从开头开始编辑，即原有内容会被删除。如果该文件不存在，创建新文件。
    print("文件名：" + file.name)
    while pageid < 362:
        url = "https://store.steampowered.com/search/?specials=1&page=" + str(pageid)
        res = requests.get(url)
        soup = bs4.BeautifulSoup(res.text, "lxml")
        contents = soup.select('div[class="responsive_search_name_combined"]')

        for content in contents:
            try:
                name = content.find("span", class_="title").string.strip()  # 游戏名
                discount = content.find("div", class_="col search_discount responsive_secondrow").find("span").string.strip()   # 折扣
                discountFloat = int("".join(list(filter(str.isdigit, discount)))) / 100
                originPrice = content.find("div", class_="col search_price discounted responsive_secondrow").find("strike").string.strip()  # 原价
                originPriceInt = int("".join(list(filter(str.isdigit, originPrice))))
                presentPrice = originPriceInt * (1 - discountFloat)
                presentPriceStr = str(round(presentPrice, 2))   # 现价
                print(name + "---" + discount + "---" + originPrice + "---" + presentPriceStr)
                file.write(name + "---" + discount + "---" + originPrice + "---" + presentPriceStr + "\n")


            except Exception as e:
                print(e) # 'gbk' codec can't encode character '\xa5' in position 39: illegal multibyte sequence
                print(name.encode('utf-8'))
                exceptname = name.encode('utf-8')
                file.write(str(exceptname) + "\n")     # 记录有问题的名称
        pageid = pageid + 1

    file.close() # 必须在这里关闭文件，提前关闭会导致 ValueError: IO operation on closed file


if __name__ == "__main__":
    main()
    print("完成！")
