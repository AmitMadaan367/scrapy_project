# -*- coding: utf-8 -*-
import scrapy


class ShopSpider(scrapy.Spider):
    name = 'shop'
    # allowed_domains = ['www.shop.com']
    # start_urls = ['http://www.shop.com/']
    def start_requests(self):
        url = 'https://www.tfrrs.org/results_search.html'

        yield scrapy.Request(url=url, callback=self.parse)

    def parse(self, response):
        meet_url=response.xpath('//td/a/@href').extract()
        meet_name=response.xpath('//td/a/text()').extract()

        # for i in men1:
        #     # print(i)
        #     url2="https:"+str(i)
        #     print(url2)
        #     self.gen="MAN"
            
        #     yield scrapy.Request(url=url2, callback=self.parse1)
            # men.append(i.strip())
        for i in meet_url:
            url2="https:"+str(i)
            # print(url2)
            yield scrapy.Request(url=url2, callback=self.parse1)
            

    def parse1(self, response):
        m_n_event=response.xpath('//td/a/@href').extract()
        for i in m_n_event:
            url3="https:"+str(i)
            # print(url3)
            yield scrapy.Request(url=url3, callback=self.parse2)



    def parse2(self, response):
        url41=response.xpath('//td/a/@href').extract()
        for i in url41:
            url4="https:"+str(i)
            # print(url4)
            yield scrapy.Request(url=url4, callback=self.parse4)


    def parse4(self, response):
        team_name=response.xpath('//th/a/text()').extract()
        date_name=response.xpath('//th/span/text()').extract()
        time_aagya=response.xpath('//td/a/text()').extract()
        sum_time=[]
        for i in time_aagya:
        #     print(i)
            if "." in i:
        #         print(i)
                sum_time.append(i)
        end_date=[]
        for i in date_name:
            i=i.strip()
            if "," in i:
                end_date.append(i)
        #         print(i)
        meet_pos=response.xpath('//td[@class="panel-heading-text"]/text()').extract()
        check=[]
        for i in meet_pos:
        #     print(i.strip())
            check.append(i.strip())
        meters=[]
        pos=[]
        for i in check:
        #     print(i.strip())
            if len(i)<=4 and len(i)!=0:
        #         print(i)
                meters.append(i)
            if len(i)>4:
                pos.append(i)
        print("done")
        for i,j,k,l,m in zip(team_name,end_date,sum_time,meters,pos):
            yield {
            'teem_name': i,
            'date': j,
            'meet_time': k,
            'meaters': l,
            'position': m,
        }
        

    	
    	# print("reeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeee",response.text)
    	
        
# class TestSpider(scrapy.Spider):
#     name = 'test'
#     # allowed_domains = ['https://www.flipkart.com/']
#     # start_urls = ['https://www.flipkart.com/']


#     def start_requests(self):
#         url = 'https://www.flipkart.com/watches/pr?sid=r18&otracker=product_breadCrumbs_Watches&page=1'

#         yield scrapy.Request(url=url, callback=self.parse)

#     def parse(self, response):
#         # print("response",response)
#         price=response.xpath('//div[@class="_1vC4OE"]/text()').extract()
#         name=response.xpath('//a[@class="_2mylT6"]/text()').extract()
#         # print(price)
#         # print(name)
#         # print(response.text)
#         jobs = response.xpath("//div/video[@class='jsx-3382097194 video-player']/src").extract()
       
#         # new=response.xpath('//div/nav[@class="_1ypTlJ"]').extract()
#         next=response.xpath("//nav[@class='_1ypTlJ']/a/@href").extract()
#         print("------------------------------------------------------------------------")
#         print("next",next)
#         print("------------------------------------------------------------------------")
#         # print("new",new)
#         # print("new",new[0])

#         for i in next:
#             url1="https://www.flipkart.com"+i
#             print("this is new url",url1)
#             for i,j in zip(price,name):
#                 print(i,j)
#                 price1.append(i)
#                 yield {
#             'price': i,
#             'name': j,
           
#         }
           

#             for j in  name:
#                 print(j)
#                 name1.append(j)
           
#             yield scrapy.Request(url=url1, callback=self.parse)
       


        # yield scrapy.Request(url="www.flipkart.com"+new[0], callback=self.parse)
   

        #     print('http://www.playbill.com'+job.replace('\\"',''))
        #     yield scrapy.Request(url='http://www.playbill.com'+job.replace('\\"',''), callback=self.parse_details)

    # def parse_details(self, response):
    #     title = response.xpath("//h2[@class='bsp-component-title jobs-page-title']/text()").extract_first()
    #     mails = response.xpath("//a[contains(@href,'mailto:')]/@href").extract()
    #     if (len(mails) > 0):
    #         email = mails[-1].replace('#a#','@').replace('#d#','.').replace('mailto:','')
    #     else:
    #         email = None
    #     company_name = response.xpath("//section[@class='jobs-section ']/p/text()").extract_first()
    #     job_description = response.xpath("//section[@class='jobs-section '][2]/p[2]//text()").extract_first()
    #     salary = response.xpath("//p[contains(text(), '$')]/text()").extract_first()

    #     yield {
    #         'title': title,
    #         'email': email,
    #         'company': company_name,
    #         'job_description': job_description,
    #         'salary': salary
    #     }
