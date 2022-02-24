from settings import *
import pytest
import re
from selenium import webdriver


def test_show_my_pets():
   # Неявные ожидания элементов
   pytest.driver.implicitly_wait(10)

   # Вводим email "берем из файла settings"
   pytest.driver.find_element_by_id('email').send_keys(valid_email)
   # Вводим пароль "берем из файла settings"
   pytest.driver.find_element_by_id('pass').send_keys(valid_password)
   # Нажимаем на кнопку входа в аккаунт
   pytest.driver.find_element_by_css_selector('button[type="submit"]').click()
   # Проверяем, что мы оказались на главной странице пользователя
   assert pytest.driver.find_element_by_tag_name('h1').text == "PetFriends"

   btn_my_pets = pytest.driver.find_element_by_link_text("Мои питомцы")
   btn_my_pets.click()

   # Колличество питомцев
   my_pets_len = pytest.driver.find_element_by_css_selector('.\\.col-sm-4.left')
   str_my_pets = my_pets_len.text()

   # Получаем список num со значениями: количество питомцев[0],количество друзей[1],количество сообщений[2]
   num = re.findall(r'\d+', str_my_pets) # Использование библиотеки Regex
   print(num)
   #получаем количество питомцев
   quantity_my_pets = int(num[0])

   #селектор для поиска всех питомцев пользователя
   # находим все карточки питомцев
   # фото
   images = pytest.driver.find_elements_by_xpath('//*[@id="all_my_pets"]/table/tbody/tr/th/img')
   # имена
   names = pytest.driver.find_elements_by_xpath('//*[@id="all_my_pets"]/table/tbody/tr/td[1]')
   # тип
   type = pytest.driver.find_elements_by_xpath('//*[@id="all_my_pets"]/table/tbody/tr/td[2]')
   # возраст
   age = pytest.driver.find_elements_by_xpath('//*[@id="all_my_pets"]/table/tbody/tr/td[3]')

   print(names[0].text) #визуальный контроль имени первоо питомца

   list_names = [] #Список имен питомцев

   for i in range(len(names)): # Цикл для создания списка имен питомцев
      list_names.append(names[i].text)
   print(list_names)

   #Создаем список уникальных имен питомцев с помощью множества set
   list_of_unique_names = []
   unique_names = set(list_names)  # Множество с именами питомцев
   for number in unique_names:     # Цикл для создания списка с уникальными именами
      list_of_unique_names.append(number)
   print(list_of_unique_names)
   # Сравниваем длину списков имен, если списки равны значит все имена уникальны
   assert len(list_names) == len(list_of_unique_names)



   for i in range(quantity_my_pets):
   # Проверка количесвтва питомцев , сравнивание количества имен питомцев со статистикой пользователя
      assert quantity_my_pets == len(names)

   # Проверка на наличие имени, типа питомца и возраста
      assert (names[i].text) != ''
      assert (type[i].text) != ''
      assert (age[i].text) != ''

   count = 0  # Счетчик количества фотографий питомцев
   for i in range(len(names)): # Цикл для подсчета елементов с атрибутом src не равным пустой строке
      if images[i].get_attribute('src') != '':
         count += 1
      # Сравниваем количество питомцев с фотографиев,проверяем что у не менее половины питомцев есть фото
   assert count >= (len(names) / 2)
