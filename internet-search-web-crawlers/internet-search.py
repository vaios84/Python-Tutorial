# Python program to demonstrate Selenium
# https://www.geeksforgeeks.org/how-to-install-selenium-in-python/

from selenium import webdriver

driver = webdriver.Firefox()
driver.get("https://google.co.in")
