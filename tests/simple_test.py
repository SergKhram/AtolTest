# -*- encoding: utf-8 -*-

from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from requests import get
import pytest
import os

class TestOpenSite():

    @pytest.fixture()
    def test_setup(self):
        global driver
        google_driver_path = os.path.join(os.path.abspath(os.path.dirname(__file__)), "../resources/drivers/chromedriver.exe")
        driver = webdriver.Chrome(executable_path=google_driver_path)
        driver.implicitly_wait(10)
        driver.maximize_window()
        yield
        driver.close()
        driver.quit()

    def test_open_site(self, test_setup):
        search_text = 'Атол-Онлайн'
        driver.get('https://www.google.ru')
        driver.find_element_by_name('q').send_keys(search_text.decode('utf-8'))
        driver.find_element_by_name('q').send_keys(Keys.RETURN)
        first_site = driver.find_element_by_xpath('//*[@id="rso"]/div[1]/div/div/div/div/div[1]/a').get_attribute('href')
        response = get(first_site)
        code = response.status_code
        assert code == 200
