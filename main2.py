import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class GoogleAutomate:
    def __init__(self):
        self.browser = webdriver.Chrome(executable_path='./Yandex/chromedriver')
    def find(self, request):
        self.browser.get('https://www.google.ru/')
        self.browser.find_element_by_xpath('//input[@class="gLFyf gsfi"]').send_keys(request)
        url = self.browser.current_url
        print(url)
        self.browser.get(url + "&num=20")
        
if __name__ == '__main__':
    google = GoogleAutomate()
    google.find('купить кофемашину bork c804 site:https://www.mvideo.ru/\n')
