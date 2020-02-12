from selenium import webdriver
import time


link = "http://suninjuly.github.io/registration2.html"


try:
    browser = webdriver.Chrome()
    browser.get(link)


    first_name = browser.find_element_by_css_selector(".first_block .first")
    first_name.send_keys("Ann")
    last_name = browser.find_element_by_css_selector(".first_block .second")
    last_name.send_keys("Kinglet")
    email = browser.find_element_by_css_selector(".first_block .third")
    email.send_keys("123@mail.test")

    phone = browser.find_element_by_css_selector(".second_block .first")
    address = browser.find_element_by_css_selector(".second_block .second")
    button = browser.find_element_by_css_selector(".btn.btn-default")
    button.click()

    # Проверяем, что смогли зарегистрироваться
    # ждем загрузки страницы
    time.sleep(1)

    # находим элемент, содержащий текст
    welcome_text_elt = browser.find_element_by_tag_name("h1")

    # записываем в переменную welcome_text текст из элемента welcome_text_elt
    welcome_text = welcome_text_elt.text

    # с помощью assert проверяем, что ожидаемый текст совпадает с текстом на странице сайта
    assert "Congratulations! You have successfully registered!" == welcome_text

finally:
    # ожидание чтобы визуально оценить результаты прохождения скрипта
    time.sleep(10)
    # закрываем браузер после всех манипуляций
    browser.quit()

# не забываем оставить пустую строку в конце файла