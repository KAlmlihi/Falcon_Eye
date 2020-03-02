import os
import time
from selenium import webdriver
from twilio.rest import Client


id_ = os.environ.get('twilioID') 
pass_ = os.environ.get('twilioPass') 

client = Client(id_, pass_)

from_Whatsapp = 'whatsapp:+14155238886'
to_Whatsapp = 'whatsapp:+966559397753'

driver = webdriver.PhantomJS('phantomjs.exe')
url = "https://www.amazon.com/Cooler-Master-MasterLiquid-Chamber-MLA-D24M-A18PC-R1/dp/B07CRGC899/ref=sr_1_5?keywords=liquid%2Bcooler&qid=1582918172&sr=8-5&th=1"
itemName = 'Cooler Master MasterLiquid LC240E RGB'

while True:
    driver.get(url)
    try:
        price = driver.find_element_by_id('priceblock_ourprice').get_attribute('innerHTML')
    except:
        price = driver.find_element_by_id('priceblock_dealprice').get_attribute('innerHTML')
    var = str()
    for i in price:
        if i != '$':
            var = var + i
    print(var)
    if float(var) <= 66:
        client.messages.create(body='Hey!\n\'' + itemName + '\' is less than 65 USD.\nCome Check it out! \nhttps://www.amazon.com/Cooler-Master-MasterLiquid-Chamber-MLA-D24M-A18PC-R1/dp/B07CRGC899/ref=sr_1_5?keywords=liquid%2Bcooler&qid=1582918172&sr=8-5&th=1',
                                from_= from_Whatsapp,
                                to=to_Whatsapp)
    time.sleep(43200)