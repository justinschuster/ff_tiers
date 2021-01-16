import scrapy


# TODO
class RankingsSpider(scrapy.Spider):
    name = "rankings"

    def start_requests(self):
        url = 'https://www.fantasypros.com/nfl/rankings/'
        format_prefixes = [
            '',
            'ppr-',
            'half-point-ppr-'
        ]
        positions = [
            'qb',
            'rb',
            'wr',
            'te'
        ]

        for pre in format_prefixes:
            for pos in positions:
                curr_url = url+pre+pos+'.php'
                #print(curr_url)
                yield scrapy.Request(url=curr_url, callback=self.parse)
            
    def parse(self, response):
        page = response.url.split("/")[-1]
        print(page)
        file_name = 'rankings-' + page + '.html'
        with open(file_name, 'wb') as f:
            f.write(response.body)
        self.log('Saved file ' + file_name)
