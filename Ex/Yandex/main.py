from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class YandexAutomate:
    def __init__(self):
        self.browser = webdriver.Chrome(executable_path='./Yandex/chromedriver')
    def login(self, email, password):
        self.browser.get('https://passport.yandex.ru/auth?from=mail&origin=hostroot_homer_auth_ru&retpath=https%3A%2F%2Fmail.yandex.ru%2F&backpath=https%3A%2F%2Fmail.yandex.ru%3Fnoretpath%3D1')
        self.browser.find_element_by_xpath('//input[@data-t="field:input-login"]').send_keys(email)
        self.browser.find_element_by_xpath('//button[@data-t="button:action:passp:sign-in"]').click()
        WebDriverWait(self.browser, 10).until(
            EC.presence_of_all_elements_located(
                (By.XPATH, '//input[@data-t="field:input-passwd"]')
            )
        )
        self.browser.find_element_by_xpath('//input[@data-t="field:input-passwd"]').send_keys(password)
        self.browser.find_element_by_xpath('//button[@data-t="button:action:passp:sign-in"]').click()
        if(self.browser.find_element_by_xpath('//button[@data-t="button:pseudo"]')):
            self.browser.find_element_by_xpath('//button[@data-t="button:pseudo"]').click()
        
if __name__ == '__main__':
    yandex = YandexAutomate()
    yandex.login('PetrVasil1234@yandex.ru', 'Russia1234')