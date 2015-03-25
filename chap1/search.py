__author__ = 'Kaniska'

from selenium import webdriver
from selenium.webdriver.common.keys import Keys

driver = webdriver.Firefox()
driver.implicitly_wait(30)
driver.maximize_window()
driver.get('http://kaniska.in')

search_field = driver.find_element_by_id("search")
search_field.clear()
search_field.send_keys("Chess")
search_field.send_keys(Keys.ENTER)

#found = driver.find_element_by_xpath("/html/body/div[1]/div/div[2]/div[1]/ul/li[4]/a")
#found = driver.find_element_by_xpath("//*[@id='views']/ul/li[4]/a")
found = driver.find_element_by_xpath("//*[@href='?view=mosaic']")
found.click()

driver.close()