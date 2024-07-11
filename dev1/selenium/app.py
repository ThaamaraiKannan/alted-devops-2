from selenium import webdriver
from selenium.webdriver.common import by

browser = webdriver.Firefox()

browser.get("https://accounts.google.com")
By = by.By

email = browser.find_element(By.ID, "identifierId")
email.send_keys("kannnan@gmail.com")

browser.find_element(By.ID, "identifierNext").find_element(By.TAG_NAME, "button").click()

# browser.find_element(By.CLASS_NAME,"button_class=VfPpkd-LgbsSe VfPpkd-LgbsSe-OWXEXe-k8QpJ VfPpkd-LgbsSe-OWXEXe-dgl2Hf nCP5yc AjY5Oe DuMIQc LQeN7 BqKGqe Jskylb TrZEUc lw1w4b").click()