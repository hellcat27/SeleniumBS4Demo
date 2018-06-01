from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from bs4 import BeautifulSoup
import urllib.request

#######

#with open(r"C:\Users\egellerman\Desktop\Python\webdriveroutput\output.html") as fp:
#    soup = BeautifulSoup(fp)

#htmlFile = open(r"C:\Users\egellerman\Desktop\Python\webdriveroutput\output.html", 'r', encoding='utf-8')
#source = htmlFile.read()
#htmlFile.close()

#soup = BeautifulSoup(source, 'html.parser')

#######

driver = webdriver.Chrome()
driver.implicitly_wait(5)
driver.get("https://www.google.com")
r = driver.find_element_by_xpath("//*[@id='lst-ib']")
r.send_keys("europe")
r.send_keys(Keys.ENTER)
#r = driver.find_element_by_xpath("//*[@id='sbtc']/div[2]/div[2]/div[1]/div/ul/li[11]/div/span[1]/span/input")
#r.click()
r = driver.find_element_by_xpath("//*[@id='hdtb-msb-vis']/div[4]/a")
r.click()
source = driver.page_source

soup = BeautifulSoup(source, 'html.parser')
#for link in soup.find_all('a'):
#    print(link.get_text())
for link in soup.find_all('a'):
    print(link.get_text()," : ",link.get('href'))

"""
site = 'http://www.google.com'
page = urllib.request.urlopen(site)

soup = BeautifulSoup(page, 'html.parser')
print(soup.prettify())
"""