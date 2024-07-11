from selenium import webdriver
from selenium.webdriver.common.by import By

browser = webdriver.Firefox()

browser.get("https://www.youtube.com")

browser.find_element(By.ID, "search-input").find_element(By.ID, "search").send_keys("devops")
browser.find_element(By.TAG_NAME, "ytd-searchbox").find_element(By.TAG_NAME, "button").click()