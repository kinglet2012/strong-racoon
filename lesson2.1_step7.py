from selenium import webdriver
import time
import math

browser = webdriver.Chrome()
link = "http://suninjuly.github.io/get_attribute.html"
# определяем функцию для расчета формулы


def calc(t):
    return str(math.log(abs(12*math.sin(int(t)))))


try:
    browser.get(link)

# search for value x
    treasure = browser.find_element_by_id("treasure")
    x = treasure.get_attribute("valuex")
    y = calc(x)

    answer = browser.find_element_by_css_selector("#answer")
    answer.send_keys(y)

    browser.find_element_by_id("robotCheckbox").click()
    browser.find_element_by_id("robotsRule").click()
    browser.find_element_by_css_selector(".btn.btn-default").click()

finally:
    # ожидание чтобы скопировать ключ
    time.sleep(5)
    # закрываем браузер после всех манипуляций
    browser.quit()

# не забываем оставить пустую строку в конце файла
