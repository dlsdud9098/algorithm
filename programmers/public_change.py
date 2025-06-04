import requests
from bs4 import BeautifulSoup
import os
from glob import glob
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium import webdriver
import time
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.common.action_chains import ActionChains
import pyperclip
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from markdownify import MarkdownConverter
import shutil

def element(driver,type, tag, click_type=0):
    if type == 'xpath':
        if click_type:
            return WebDriverWait(driver, 10).until(
                EC.element_to_be_clickable((By.XPATH, tag))
            )
        else:

            return WebDriverWait(driver, 10).until(
                EC.presence_of_element_located((By.XPATH, tag))
            )
    elif type == 'css':
        if click_type:
            return WebDriverWait(driver, 10).until(
                EC.element_to_be_clickable((By.CSS_SELECTOR, tag))
            )
        else:
            return WebDriverWait(driver, 10).until(
                EC.presence_of_element_located((By.CSS_SELECTOR, tag))
            )

if __name__ == '__main__':
    # ChromeDriver 자동 설치 및 초기화
    options = webdriver.ChromeOptions()
    options.add_argument("--window-size=1280,720")  # 가로 1280px, 세로 720px
    driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=options)

    driver.get('https://velog.io/@dlsdud9098/series/%ED%94%84%EB%A1%9C%EA%B7%B8%EB%9E%98%EB%A8%B8%EC%8A%A4')
    driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")


    links = []
    for i in driver.find_elements(By.CSS_SELECTOR, '#root > div.sc-dPiLbb.sc-bBHHxi.kTIDXm > div > div > section > div > div > h2 > a'):
        links.append(i.get_attribute('href'))

    print(len(links))

    links = list(reversed(links))

    # 로그인 버튼
    driver.find_element(By.XPATH, '/html/body/div[1]/div[2]/div[1]/div/div[2]/button').click()
    time.sleep(.5)

    # 깃허브 선택
    driver.find_element(By.CSS_SELECTOR, '#root > div.sc-gsDKAQ.dWETBP > div > div.white-block > div.block-content > div > div.upper-wrapper > section:nth-child(3) > div > a:nth-child(1)').click()
    time.sleep(.5)
    # 아이디 비밀번호 입력, 로그인
    driver.find_element(By.CSS_SELECTOR, '#login_field').send_keys('dlsdud9098@naver.com')
    driver.find_element(By.CSS_SELECTOR, '#password').send_keys('dud7959098@')
    driver.find_element(By.CSS_SELECTOR, '#login > div.auth-form-body.mt-3 > form > div > input.btn.btn-primary.btn-block.js-sign-in-button').click()

    time.sleep(5)
    # for link in links[:30]:
    link = links[0]
    driver.get(link)
    for _ in range(30):
        bool_text = element(driver, 'xpath', '/html/body/div[1]/div[2]/div[3]/div/div[2]/div[1]').text
        print(bool_text)
        if '비공개' in bool_text:
            element(driver, 'xpath', '/html/body/div[1]/div[2]/div[3]/div/div[1]/button[2]', 1).click()
            element(driver, 'xpath', '/html/body/div[1]/div[2]/div/div[1]/div/div[2]/div/div/button[2]', 1).click()
            element(driver, 'xpath', '/html/body/div[1]/div[2]/div[2]/div/div[3]/div[1]/section[1]/div/button[1]', 1).click()
            element(driver, 'xpath', '/html/body/div[1]/div[2]/div[2]/div/div[3]/div[2]/button[2]', 1).click()
        element(driver, 'xpath', '/html/body/div[1]/div[2]/div[3]/div/div[6]/div/div[2]/div[2]/button[1]', 1).click()
        time.sleep(1)