import pytest
from selenium import webdriver
from settings import *
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


def test_show_my_pets():
    # Явное ожидание елемента email
    email = WebDriverWait(pytest.driver, 10).until(
        EC.presence_of_element_located((By.ID, 'email'))
    )
    email.send_keys(valid_email)
    # Явное ожидание елемента Password
    password = WebDriverWait(pytest.driver, 10).until(
        EC.presence_of_element_located((By.ID, 'password'))
    )
    password.send_keys(valid_password)
    # Явное ожидание кнопки "Войти"
    button_enter = WebDriverWait(pytest.driver, 10).until(
        EC.visibility_of_element_located((By.CSS_SELECTOR, 'button[type="submit"]'))
    )
    button_enter.click()

    assert pytest.driver.find_element_by_tag_name('h1').text == "PetFriends"

    # Явное ожидание кнопки "Фото"
    images = WebDriverWait(pytest.driver, 10).until(
        EC.presence_of_all_elements_located((By.CSS_SELECTOR, '.card-deck .card-img-top'))
    )
    # Явное ожидание кнопки "Имен"
    names = WebDriverWait(pytest.driver, 10).until(
        EC.presence_of_all_elements_located((By.CSS_SELECTOR, '.card-deck .card-title'))
    )
    # Явное ожидание кнопки "Описания"
    descriptions = WebDriverWait(pytest.driver, 10).until(
        EC.presence_of_all_elements_located((By.CSS_SELECTOR, '.card-deck .card-text'))
    )

    print(names[0].text)
    print
    print(len(names))
    print
    print(descriptions[0].text)

    for i in range(len(names)):
       assert images[i].get_attribute('src') != ''
       assert names[i].text != ''
       assert descriptions[i].text != ''
       assert ',' in descriptions[i].text
       parts = descriptions[i].text.split(",")
       assert len(parts[0]) > 0
       assert len(parts[1]) > 0


    string = ""

    for i in range(1):
        assert (images[i].get_attribute('src')) != string
        assert (names[i].text) != string
        assert (descriptions[i].text) != string
        assert ',' in descriptions[i].text
        parts = descriptions[i].text.split(",")
        assert len(parts[0]) > 0
        assert len(parts[1]) > 0
