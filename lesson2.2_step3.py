from selenium import webdriver
from selenium.webdriver.support.ui import Select
import time


browser = webdriver.Chrome()
link = "http://suninjuly.github.io/selects1.html"


try:
    browser.get(link)

    # находим значения которые нужно складывать
    num1 = browser.find_element_by_id("num1").text
    num2 = browser.find_element_by_id("num2").text
    # делаем ответ строкой чтобы можно было подставить в селект по части текста
    answer = str(int(num1) + int(num2))
    # ищем список по тегу и выбираем в нем ответ по части текста
    answers = Select(browser.find_element_by_tag_name("select"))
    answers.select_by_visible_text(answer)
    # находим кнопку и нажимаем
    browser.find_element_by_css_selector(".btn.btn-default").click()

finally:
    time.sleep(10)
    browser.quit()

# не забываем оставить пустую строку в конце файла
