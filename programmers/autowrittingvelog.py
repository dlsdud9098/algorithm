import requests
from bs4 import BeautifulSoup
# from pathlib import Path
import os
from datetime import datetime
from glob import glob
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select
from selenium import webdriver
import time
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.common.action_chains import ActionChains
import pyperclip
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait as wait
import schedule

def auto_write():
    file_list = glob(r'C:\Users\inyoung\Desktop\git_programmers\*')
    file_create_date = {}
    now_date_upload_llist = []
    folders_file = []
    # 폴더 안의 파일 모두 보기
    for file in file_list:
        if os.path.isdir(file):
            folders_file = glob(file+'\*')
            # print(file)

    # 파일 생성 날짜 딕셔너리 만들기
    for folder in folders_file:
        # print(folder)
        # file_create_date[folder[folder.index('0\\')+2:]] = datetime.fromtimestamp(os.path.getctime(folder)).strftime('%Y-%m-%d')
        file_create_date[folder[folder.index('0\\')+2:]] = [datetime.fromtimestamp(os.path.getctime(folder)).strftime('%Y-%m-%d'), folder]

    now = datetime.now().strftime('%Y-%m-%d')
    now_date_upload_file = []
    now_date_upload_list = []
    # print(now)
    for name, date in file_create_date.items():
        if date[0] == now:
            now_date_upload_list.append(name)
            now_date_upload_file.append(date[1])
        # now_date_upload_list.append(name)
        # now_date_upload_file.append(date[1])

    # now_date_upload_file
    # 셀레니움
    driver = webdriver.Chrome('./chromedriver')
    driver.implicitly_wait(10)

    driver.get('https://velog.io/')
    time.sleep(1)
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

    for idx, file in zip(now_date_upload_list, now_date_upload_file):
        print(idx)
        url = f'https://school.programmers.co.kr/learn/courses/30/lessons/{idx}'
        rq = requests.get(url)
        # rq = requests.get('https://school.programmers.co.kr/learn/courses/30/lessons/120862')

        with open(file, 'r', encoding='UTF8') as file:
            code = file.read()

        soup = BeautifulSoup(rq.content, 'html.parser')

        result = []
        title = soup.select_one('#tab > li').text.lstrip().rstrip()
        content = str(soup.select_one('#tour2 > div'))
        content = content.split('\n')
        for con in content:
            if ' class' in con:
                con = con[:con.index(' class')] + con[con.index('">')+1:]

            if '<h6>' or '<h5>' in con:
                con = con.replace('<h6>', '\n## ')
                con = con.replace('<h5>', '\n## ')
            
            if '</h6>' or '</h5>' in con:
                con = con.replace('</h6>', '')
                con = con.replace('</h5>', '')
            
            if '<div>' in con:
                con = con.replace('<div>', '')
            if '</div>' in con:
                con = con.replace('</div>', '')
            
            if '<hr/>' or '</hr>' in con:
                con = con.replace('</hr>', '\n---\n\n')
                con = con.replace('<hr/>', '\n---\n\n')

            if '<ul>' or '</ul>' in con:
                con = con.replace('<ul>', '')
                con = con.replace('</ul>', '')
            
            if '<li>' in con:
                con = con.replace('<li>', '\n* ')
            
            if '</li>' in con:
                con = con.replace('</li>','\n\n')

            if '<p>' or '</p>' in con:
                con = con.replace('<p>', '')
                con = con.replace('</p>', '\n')

            if 'code>' in con:
                con  =con.replace('<code>', '```')
                con  =con.replace('</code>', '```\n')
            
            if '<table>' in con:
                con = con.replace('<table>', '\n<table>')
            
            if '</table>' in con:
                con = con.replace('</table>', '\n</table>\n')


            if '문제 설명' in con:
                con = con.replace('## 문제 설명', '## 💡문제 설명\n')
            if '제한사항' in con:
                con = con.replace('## 제한사항', '## 🚫제한사항\n')
            if '입출력 예 설명' in con:
                con = con.replace('## 입출력 예 설명', '## 🔍입출력 예 설명\n')
            if '입출력 예' in con:
                con = con.replace('## 입출력 예', '## 🔢입출력 예\n\n')
            

            result.append(con)

        result.append('---\n\n')
        result.append('## 💻코드')
        result.append('\n')
        result.append(f'''
```python
{code}
```
        ''')
        result.append('\n\n')


        # 맨 처음에 사진 추가하기
        result.insert(0, '![](https://velog.velcdn.com/images/dlsdud9098/post/e1464da6-734f-4172-a5d3-8df73b71a328/image.png)')

        # 해당 문제 링크 추가
        result.append(url.replace('.py', '?language=python3'))

        # print(result)

        # result
        velog_content = []
        velog_content_all = ''.join(result)

        # velog

        try:
            # 글쓰기 버튼
            driver.find_element(By.XPATH, '//*[@id="root"]/div[2]/div[1]/div/div[2]/button[2]').click()
        except:
            driver.find_element(By.XPATH, '//*[@id="root"]/div[2]/div[1]/div/div[2]/button[2]').click()

        # 제목 쓰기                          
        ele = driver.find_element(By.XPATH,'//*[@id="root"]/div[2]/div/div[1]/div/div[1]/div[1]/div/textarea')
        ele.send_keys('프로그래머스 '+title)

        # 태그
        driver.find_element(By.XPATH, '//*[@id="root"]/div[2]/div/div[1]/div/div[1]/div[1]/div/div[2]/input').send_keys('프로그래머스, 파이썬,')

        # 내용 쓰기
        ele = driver.find_element(By.XPATH, '//*[@id="root"]/div[2]/div/div[1]/div/div[1]/div[3]/div/div[6]/div[1]/div/div/div/div[5]').click()
        act = ActionChains(driver)

        pyperclip.copy(velog_content_all)
        act.key_down(Keys.CONTROL).send_keys("v").perform()

        time.sleep(1)
        # 출간하기 버튼
        try:
            driver.find_element(By.XPATH, '//*[@id="root"]/div[2]/div/div[1]/div/div[2]/div/div/button[2]').click()
        except NoSuchElementException:
            time.sleep(1)
            driver.find_element(By.CSS_SELECTOR, '#root > div.sc-gLDmcm.giPzuI > div > div.sc-ehCJOs.auvDf > div > div.sc-eLwHnm.BNgcW > div > div > button.sc-jrQzAO.jYsOEX.sc-fvxzrP.hiArGR').click()
        time.sleep(1)

        # 전체 공개
        driver.find_element(By.XPATH, '//*[@id="root"]/div[2]/div[2]/div/div[3]/div[1]/section[1]/div/button[1]').click()

        # 시리즈 선택
        try:
            driver.find_element(By.XPATH, '//*[@id="root"]/div[2]/div[2]/div/div[3]/div[1]/section[3]/div/button').click()
        except NoSuchElementException:
            driver.find_element(By.XPATH, '//*[@id="root"]/div[2]/div[2]/div/div[3]/div[1]/section[3]/div/button').click()
        time.sleep(1)
        # 시리즈 선택
        driver.find_element(By.XPATH, '//*[@id="root"]/div[2]/div[2]/div/div[3]/section/div/div[1]/ul/li[5]').click()
        time.sleep(1)
        # 선택하기
        driver.find_element(By.XPATH, '//*[@id="root"]/div[2]/div[2]/div/div[3]/section/div/div[2]/button[2]').click()
        time.sleep(.5)
        # 출간하기
        driver.find_element(By.XPATH, '//*[@id="root"]/div[2]/div[2]/div/div[3]/div[2]/button[2]').click()

        # time.sleep(100)
    time.sleep(1)
    driver.close()


def change_public():
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

    page = driver.page_source
    soup = BeautifulSoup(page, 'html.parser')
    links = soup.find_all('a','sc-hGnimi')

    for link in links:
        driver.get('https://velog.io'+link['href'])
        # 수정 버튼
        try:
            wait(driver, 10).until(EC.visibility_of_element_located((By.XPATH, '//*[@id="root"]/div[2]/div[3]/div/div[1]/button[2]'))).click()
        except:
            driver.get('https://velog.io'+link['href'])
            wait(driver, 10).until(EC.visibility_of_element_located((By.XPATH, '//*[@id="root"]/div[2]/div[3]/div/div[1]/button[2]'))).click()

        # 수정하기 버튼
        wait(driver, 10).until(EC.visibility_of_element_located((By.XPATH, '//*[@id="root"]/div[2]/div/div[1]/div/div[2]/div/div/button[2]'))).click()
        # 전채 공개 버튼
        wait(driver, 10).until(EC.visibility_of_element_located((By.XPATH, '//*[@id="root"]/div[2]/div[2]/div/div[3]/div[1]/section[1]/div/button[1]'))).click()
        # 출간하기 버튼
        wait(driver, 10).until(EC.visibility_of_element_located((By.XPATH, '//*[@id="root"]/div[2]/div[2]/div/div[3]/div[2]/button[2]'))).click()
    driver.close()

schedule.every().day.at('23:59').do(auto_write)
schedule.every().day.at('09:00').do(change_public)

while True:
    schedule.run_pending()
    time.sleep(1)