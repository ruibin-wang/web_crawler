import scrapy


class DemoSpider(scrapy.Spider):
    name = 'itcast'
    allowed_domains = ['itcast.com']
    start_urls = ['http://www.itcast.cn/']

    def parse(self, response):
        print(response)
        filename = "teacher.html"
        # open(filename, 'w').write(response.body.decode("utf-8"))
        open(filename, 'w', encoding="utf-8").write(response.body.decode("utf-8"))

        # 获取网站标题
        # context = response.xpath('/html/head/title/text()')
        context = response.xpath('/html/body/div[1]/div[4]/div/div[1]/h2')

        # 提取网站标题
        title = context.extract_first()
        print(title)
        pass


