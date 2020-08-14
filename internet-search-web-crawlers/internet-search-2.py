# Python program to demonstrate Selenium
# https://www.geeksforgeeks.org/how-to-install-selenium-in-python/

from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time

def get_results(search_term):
    url = "https://www.startpage.com/sp/search"
    browser = webdriver.Firefox()
    browser.get(url)
    search_box = browser.find_element_by_id("q")
    search_box.clear()
    search_box.send_keys(search_term)
    search_box.send_keys(Keys.RETURN) #search_box.submit()
    time.sleep(5)
    
    links = browser.find_elements_by_class_name("w-gl__result-title")
        
    results = []

    for link in links:
        href = link.get_attribute("href")
        print(href)
        results.append(href)

    time.sleep(5)
    browser.close()
    return results

get_results("Spectre Attacks Exploiting Speculative Execution")
