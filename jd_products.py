import requests
from lxml import etree
from pyecharts import WordCloud
from pyecharts import Bar

class JD_Spider():
    def __init__(self):
        self.headers = {
            "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/72.0.3626.109 Safari/537.36"}
        self.url = 'https://so.m.jd.com/ware/search.action?keyword=%E5%86%85%E8%A3%A4&area_ids=1,72,2819&sort_type=sort_totalsales15_desc&sf=12&as=1&qp_disable=no&fdesc=%E5%8C%97%E4%BA%AC&t1=1551798771686'

    def get_req(self):
        response = requests.get(url=self.url,headers=self.headers)
        txt = response.text
        html_content = etree.HTML(txt)
        return html_content

    def get_content(self):
        global brands
        brands = []
        global prices
        prices = []
        global sales_num
        sales_num = []
        global ratios
        ratios = []
        html_content = self.get_req()
        for i in range(10):
            products_info = html_content.xpath('//div[contains(@class,"search_prolist_item_inner")]/div[2]')[i]
            brand_names =products_info.xpath('./div[5]/div[@class="shop_area"]/span')[0]
            price_info = products_info.xpath('./div[@class="search_prolist_price"]/strong/em/@pri')[0]
            sales = products_info.xpath('./div[4]/span/span')[0]
            comment_ratios = products_info.xpath('.//div[4]/span/span')[1]
            brand_name = brand_names.text
            comment_ratio=comment_ratios.text
            sale_num = sales.text

            brands.append(brand_name)
            prices.append(price_info)
            sales_num.append(sale_num)
            ratios.append(comment_ratio)

            product = {
                "brand": brand_name,
                "price": price_info,
                "sales": sale_num,
                "good_comment_ratio": comment_ratio + '%'

            }
    def Geo(self):
        wordcloud = WordCloud(width=900, height=400)
        wordcloud.add("wordcloud",brands, sales_num, word_size_range=[20, 80],shape='circle')
        wordcloud.render("wordcloud.html")
        bar = Bar("销量与品牌")
        bar.add("sales", brands, sales_num,xaxis_interval=0, xaxis_rotate=30, yaxis_rotate=30,bar_category_gap='35%')
        bar.render("sales and brands1.html")

    def run(self):
        self.get_req()
        self.get_content()
        self.Geo()

if __name__ == '__main__':
    spider = JD_Spider()
    spider.run()