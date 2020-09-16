from selenium import webdriver
import time
import math

link = "http://suninjuly.github.io/get_attribute.html"

def calc(x):
	return str(math.log(abs(12*math.sin(int(x)))))
	
try:
	browser = webdriver.Chrome()
	browser.get(link)
	
	x_element = browser.find_element_by_id("treasure")
	treasure_valuex = x_element.get_attribute("valuex")
	x = x_element.text
	y = calc(treasure_valuex)
	input1 = browser.find_element_by_xpath ("//*[@id='answer']")
	input1.send_keys(y) 
	option1 = browser.find_element_by_id ("robotCheckbox")
	option1.click()
	option2 = browser.find_element_by_id ("robotsRule")
	option2.click()
	button = browser.find_element_by_css_selector("button.btn")
	button.click()
finally:
    # успеваем скопировать код за 30 секунд
    time.sleep(20)
    # закрываем браузер после всех манипуляций
    browser.quit()

# не забываем оставить пустую строку в конце файла