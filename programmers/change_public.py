from multiprocessing import Process, freeze_support
from multiprocessing import Pool, Manager
from itertools import repeat
import requests
from bs4 import BeautifulSoup
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select
from selenium import webdriver
import time
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait as wait

def take_links(link, private_list):
    try:
        rq = requests.get(link.get_attribute('href'))
        soup = BeautifulSoup(rq.content, 'html.parser')
        soup.find('div', 'head-wrapper').text
        soup.find('div', 'information').text
    except:
        # private_links.append(link.get_attribute('href'))
        private_list.append(link.get_attribute('href'))

if __name__ == '__main__':
    driver = webdriver.Chrome('./chromedriver')
    driver.implicitly_wait(10)

    driver.get('https://velog.io/@dlsdud9098/series/%ED%94%84%EB%A1%9C%EA%B7%B8%EB%9E%98%EB%A8%B8%EC%8A%A4')

    # 로그인 버튼
    driver.find_element(By.XPATH, '//*[@id="root"]/div[2]/div[1]/div/div[2]/button[2]').click()
    time.sleep(.5)

    # 깃허브 선택
    driver.find_element(By.CSS_SELECTOR, '#root > div.sc-gsDKAQ.dWETBP > div > div.white-block > div.block-content > div > div.upper-wrapper > section:nth-child(3) > div > a:nth-child(1)').click()
    time.sleep(.5)
    # 아이디 비밀번호 입력, 로그인
    driver.find_element(By.CSS_SELECTOR, '#login_field').send_keys('dlsdud9098@naver.com')
    driver.find_element(By.CSS_SELECTOR, '#password').send_keys('dud7959098@')
    driver.find_element(By.CSS_SELECTOR, '#login > div.auth-form-body.mt-3 > form > div > input.btn.btn-primary.btn-block.js-sign-in-button').click()

    time.sleep(.5)
    driver.find_element(By.XPATH, '//*[@id="root"]/div[2]/div[3]/div/section/div[2]/button').click()
    links = driver.find_elements(By.XPATH, '//*[@id="root"]/div[2]/div[3]/div/section/div[3]/div/h2/a')
    # print(links)
    private_links = []

    freeze_support()

    m = Manager()
    private_links = m.list()

    pool = Pool(processes=4)
    pool.starmap(take_links, zip(links, repeat(private_links)))

    pool.close()
    pool.join()

    print(private_links)

    for link in private_links:
        driver.get(link)
        # 수정 버튼
        try:
            wait(driver, 10).until(EC.visibility_of_element_located((By.XPATH, '//*[@id="root"]/div[2]/div[3]/div/div[1]/button[2]'))).click()
        except:
            driver.get(link)
            wait(driver, 10).until(EC.visibility_of_element_located((By.XPATH, '//*[@id="root"]/div[2]/div[3]/div/div[1]/button[2]'))).click()

        # 수정하기 버튼
        wait(driver, 10).until(EC.visibility_of_element_located((By.XPATH, '//*[@id="root"]/div[2]/div/div[1]/div/div[2]/div/div/button[2]'))).click()
        # 전채 공개 버튼
        wait(driver, 10).until(EC.visibility_of_element_located((By.XPATH, '//*[@id="root"]/div[2]/div[2]/div/div[3]/div[1]/section[1]/div/button[1]'))).click()
        # 출간하기 버튼
        wait(driver, 10).until(EC.visibility_of_element_located((By.XPATH, '//*[@id="root"]/div[2]/div[2]/div/div[3]/div[2]/button[2]'))).click()
    driver.close()