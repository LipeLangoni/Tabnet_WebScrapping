from bs4 import BeautifulSoup as bs
import pandas as pd
import selenium as sln
from selenium.webdriver.support.ui import Select
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium import webdriver
chrome_options = webdriver.ChromeOptions()
chrome_options.add_argument('--headless')
chrome_options.add_argument('--no-sandbox')
chrome_options.add_argument('--disable-dev-shm-usage')
wd = webdriver.Chrome('chromedriver',options=chrome_options)
wd.get("http://tabnet.datasus.gov.br/cgi/deftohtm.exe?sih/cnv/qrbr.def")

select_box = wd.find_element("name", "Incremento")
box_object = Select(select_box)
for opt in box_object.options:
  ActionChains(wd) \
    .key_down(Keys.SHIFT) \
    .click(opt) \
    .key_up(Keys.SHIFT) \
    .perform()
select_box2 = wd.find_element("name", "Arquivos")
box_object = Select(select_box2)
for opt in box_object.options:
  ActionChains(wd) \
    .key_down(Keys.SHIFT) \
    .click(opt) \
    .key_up(Keys.SHIFT) \
    .perform()
 
bitton = wd.find_element("name", "mostre")
bitton.click()

nivel2 = wd.find_element("xpath", "/html/body/div/div/div[3]/table[1]/tbody/tr/td[1]/a")
href = nivel2.get_attribute('href')
df = pd.read_csv(href,sep=';', encoding='latin-1',skiprows=3)
