import requests
from lxml import etree
import time

class JD_Spider():
    def __init__(self):
        self.headers = {
            "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/72.0.3626.109 Safari/537.36"}
        # 获取当前unix时间戳，并且保留和请求url中相同的位数（这里是5位）
        a = time.time()  # 这里获取的unix时间戳默认是小数点后七位
        self.b = '%.5f' % a
        # self.conn = connect(host='localhost',port=3306,user='wanli')
    def crawl_first_urls(self,n):
        self.url = 'https://search.jd.com/Search?keyword=内裤&enc=utf-8&qrst=1&rt=1&stop=1&psort=3&vt=2&stock=1&page='+str(2*n-1)+'&s='+str(1+(n-1)*30)+'&click=0&scrolling=y&log_id='+str(self.b)
        resp = requests.get(url=self.url, headers=self.headers)
        resp.encoding = 'utf-8'
        txt = resp.text
        html_content = etree.HTML(txt)
        shop_name = html_content.xpath(
            '//div[@id="J_goodsList"]/ul/li/div[contains(@class,"gl-i-wrap")]/div[7]/span/a/text()')
        # comment_count = html_content.xpath(
            # '//div[@id="J_goodsList"]/ul/li/div[contains(@class,"gl-i-wrap")]/div[5]/strong')

        prices = html_content.xpath(
            '//div[@id="J_goodsList"]/ul/li/div[contains(@class,"gl-i-wrap")]/div[3]/strong/i/text()')
    def crawl_next_urls(self,n):
        self.url = 'https://search.jd.com/Search?keyword=内裤&enc=utf-8&qrst=1&rt=1&stop=1&psort=3&vt=2&stock=1&page='+str(2*n)+'&s='+str(1+(n-1)*30)+'&click=0&scrolling=y&log_id='+str(self.b)
        resp = requests.get(url=self.url, headers=self.headers)
        resp.encoding = 'utf-8'
        txt = resp.text
        html_content = etree.HTML(txt)
        datas = html_content.xpath('//li[contains(@class,"gl-item")]')
        shop_name = html_content.xpath(
            '//div[@id="J_goodsList"]/ul/li/div[contains(@class,"gl-i-wrap")]/div[7]/span/a/text()')
        for data in datas:
            comment_count = data.xpath('div/div[5]/text()')
            print(comment_count)

        # comment = etree.tostring(comment_count)
        prices = html_content.xpath('//div[@id="J_goodsList"]/ul/li/div[contains(@class,"gl-i-wrap")]/div[3]/strong/i/text()')
        # print(type(shop_name))
    def run(self):
        for i in range(1,5):#这里要从1开始，如果从0开始的话前面的三四页都是第一页的内容
            # 看爬取到第几页：

            try:
                print('   First_Page:   ' + str(i))
                spider.crawl_first_urls(i)
                print('   Finish')
            except Exception as e:
                print(e)
            print('-'*30)
            try:
                print('   Last_Page:   ' + str(i))
                self.crawl_next_urls(i)
                print('   Finish')
            except Exception as e:
                print(e)
if __name__ == '__main__':
    spider = JD_Spider()

    spider.run()
