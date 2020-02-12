from selenium import webdriver
import time
import math

browser = webdriver.Chrome()
link = "http://suninjuly.github.io/math.html"
# определяем функцию для расчета формулы


def calc(t):
    return str(math.log(abs(12*math.sin(int(t)))))


try:
    browser.get(link)

# search for value x
    x_el = browser.find_element_by_css_selector("label #input_value")
    x = x_el.text
    y = calc(x)

    answer = browser.find_element_by_css_selector("#answer")
    answer.send_keys(y)
    checkbox = browser.find_element_by_css_selector(".form-check-input")
    robots = browser.find_element_by_css_selector("[for='robotsRule']")
    checkbox.click()
    robots.click()

    button = browser.find_element_by_css_selector(".btn.btn-default")
    button.click()

finally:
    # ожидание чтобы скопировать ключ
    time.sleep(30)
    # закрываем браузер после всех манипуляций
    browser.quit()

# не забываем оставить пустую строку в конце файла
