from selenium import webdriver
from selenium.webdriver.common import action_chains
from selenium.webdriver.support.ui import Select
from selenium.webdriver.common import touch_actions
import time

driver = webdriver.Firefox()

url = open("url").readlines()[0].replace('\n','')

driver.get(url)

time.sleep(3)

#touch_actions.TouchActions(driver).scroll(0,100).perform()

selectsort = driver.find_elements_by_id("proposal-sorting")[0]
#action_chains.ActionChains(driver).click(b1).perform()
action_chains.ActionChains(driver).move_to_element(selectsort).perform()
Select(selectsort).select_by_index(2)

time.sleep(2)

println(driver.find_element_by_tag_name("td").html())

#for i in range(5):
#    morebutton=driver.find_elements_by_id("Citation network")[0]
