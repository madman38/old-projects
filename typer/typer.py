from selenium import webdriver
from selenium.webdriver.common.by import By
import keyboard

browser = webdriver.Firefox() # istediğin webdriverı kullanabilirsin
browser.get("https://humanbenchmark.com/tests/typing")

the_text = []

try:
    for i in range(1000):
        value = browser.find_element(By.XPATH, f'/html/body/div/div/div[4]/div[1]/div/div[2]/div/span[{i+1}]')
        inner_html = value.get_attribute('innerHTML')
        the_text.append(inner_html)

except:
    print("bitti")

for word in the_text:
    keyboard.write(word)