from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from time import sleep

driver = webdriver.Firefox()

driver.get('about:preferences#privacy')

sleep(5)

clear_now_button = driver.find_element(By.XPATH, '//button[contains(@class, "button-clear-private-data-now")]')
ActionChains(driver).move_to_element(clear_now_button).click().perform()

sleep(5)

cache_checkbox = driver.find_element(By.XPATH, '//input[@value="cache"]')
cache_checkbox.send_keys(Keys.SPACE)

sleep(5)

clear_selected_button = driver.find_element(By.XPATH, '//button[contains(@class, "button-clear-selected")]')
ActionChains(driver).move_to_element(clear_selected_button).click().perform()

sleep(5)

driver.quit()
