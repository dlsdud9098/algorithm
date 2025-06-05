import undetected_chromedriver as uc
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import Keys
import requests
from bs4 import BeautifulSoup
import os
from glob import glob
import time
import pyperclip
import shutil
import random
from seleniumbase import SB
from selenium_stealth import stealth
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service

def crawl_data():
    variables = {}
    
    file_paths = glob('programmers/files/*.py')
    for id, file in enumerate(file_paths):
        file_name = os.path.basename(file)[:-3]
        folder, idx = file.split('-')
        
        url = f'https://school.programmers.co.kr/learn/courses/30/lessons/{idx}'
        rq = requests.get(url)
        
        with open(file, 'r', encoding='UTF8') as file_content:
            code = file_content.read()

        soup = BeautifulSoup(rq.content, 'html.parser')

        result = []
        title = soup.select_one('#tab > div.challenge-nav-left-menu > div.nav-item.algorithm-nav-link.algorithm-title > span').text.lstrip().rstrip()
        content = str(soup.select_one('body > div.main.theme-dark > div > div.challenge-content.lesson-algorithm-main-section > div.main-section.tab-content > div.guide-section'))
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
                con  =con.replace('</code>', '```')
            
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
            if '테스트 케이스 구성 안내' in con:
                con = con.replace('## 테스트 케이스 구성 안내', '## 테스트 케이스 구성 안내\n\n')

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

        # result
        velog_content_all = ''.join(result)
        variables[f'page_{id}'] = (title, velog_content_all)
        
        new_path = './uploads'
        if not os.path.exists(new_path):
            os.makedirs(new_path)
        file_name = os.path.basename(file)
        new_file_path = os.path.join(new_path, file_name)
        shutil.move(file, new_file_path)

    return variables

def create_undetected_driver():
    """Undetected Chrome 드라이버 생성"""
    print("Undetected Chrome 드라이버를 생성하는 중...")
    
    # 옵션 설정
    options = webdriver.ChromeOptions()
    options.add_argument("--window-size=1280,720")
    options.add_experimental_option("debuggerAddress", "127.0.0.1:9222")
    options.add_experimental_option("excludeSwitches", ["enable-automation"])
    options.add_experimental_option('useAutomationExtension', False)
    
    # Undetected Chrome 드라이버 생성
    driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=options)
    driver.implicitly_wait(10)

    with SB(test=True, uc=True) as sb:
        sb.open("https://google.com/ncr")
        sb.type('[title="Search"]', "SeleniumBase GitHub page\n")
        sb.click('[href*="github.com/seleniumbase/"]')
        sb.save_screenshot_to_logs()  # ./latest_logs/
        print(sb.get_page_title())
    
    print("드라이버 생성 완료!")
    return driver

def google_login(driver):

    driver.get('https://v3.velog.io/api/auth/v3/social/redirect/google?next=&isIntegrate=0')


    # 로그인 버튼
    # WebDriverWait(driver, 10).until(
    #     EC.element_to_be_clickable((By.XPATH, '//*[@id="html"]/body/div/div[2]/div[2]/div/header/div/div[2]/button'))
    # ).click()

    # 구글 선택
    # WebDriverWait(driver, 10).until(
    #     EC.element_to_be_clickable((By.XPATH, '//*[@id="html"]/body/div/div[3]/div/div[2]/div[2]/div/div[1]/section[2]/div/a[2]'))
    # ).click()

    WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.XPATH, '/html/body/div[1]/div[1]/div[2]/c-wiz/div/div[2]/div/div/div[1]/form/span/section/div/div/div[1]/div/div[1]/div/div[1]/input'))
    ).send_keys('remember33330')

    WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.XPATH, '/html/body/div[1]/div[1]/div[2]/c-wiz/div/div[3]/div/div[1]/div/div/button'))
    ).click()

    WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.XPATH, '//*[@id="password"]/div[1]/div/div[1]/input'))
    ).send_keys('tmddlf795')
    time.sleep(.5)

    WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.XPATH, '//*[@id="passwordNext"]/div/button'))
    ).click()

    WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.XPATH, '//*[@id="html"]/body/div/div[2]/div[2]/div/header/div/div[2]/a[3]'))
    )

    driver.get('https://velog.io/')
def write_content(driver, variables):
    for i in range(len(variables)):
        title, velog_content_all = variables[f'page_{i}']
        print(title)
        
        WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, '//*[@id="html"]/body/div/div[2]/div[2]/div/header/div/div[2]/a[3]/button'))
        ).click()

        # 제목 쓰기                          
        ele = driver.find_element(By.XPATH,'/html/body/div[1]/div[2]/div/div[1]/div/div[1]/div[1]/div/textarea').click()
        act = ActionChains(driver)
        
        pyperclip.copy('프로그래머스 '+title)
        act.key_down(Keys.CONTROL).send_keys('v').perform()

        # 태그
        driver.find_element(By.XPATH, '/html/body/div[1]/div[2]/div/div[1]/div/div[1]/div[1]/div/div[2]/div/input').send_keys('프로그래머스, 파이썬,')

        # 내용 쓰기
        ele = driver.find_element(By.XPATH, '/html/body/div[1]/div[2]/div/div[1]/div/div[1]/div[3]/div/div[6]').click()
        act = ActionChains(driver)

        pyperclip.copy(velog_content_all)
        act.key_down(Keys.CONTROL).send_keys("v").perform()

        time.sleep(1)
        # 출간하기 버튼
        try:
            WebDriverWait(driver, 10).until(
                EC.element_to_be_clickable((By.XPATH, '/html/body/div[1]/div[2]/div/div[1]/div/div[2]/div/div/button[2]'))
            ).click()
        except:
            WebDriverWait(driver, 10).until(
                EC.element_to_be_clickable((By.XPATH, '/html/body/div[1]/div[2]/div/div[1]/div/div[2]/div/div/button[2]'))
            ).click()
        # 전체 공개

        # WebDriverWait(driver, 10).until(
        #     EC.element_to_be_clickable((By.XPATH, '/html/body/div[1]/div[2]/div[2]/div/div[3]/div[1]/section[1]/div/button[2]'))
        # ).click()
        # WebDriverWait(driver, 10).until(
        #     EC.element_to_be_clickable((By.XPATH, '/html/body/div[1]/div[2]/div[2]/div/div[3]/div[1]/section[1]/div/button[1]'))
        # ).click()

        time.sleep(1)

        # 시리즈 선택
        WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, '//*[@id="root"]/div[2]/div[2]/div/div[3]/div[1]/section[3]/div/button'))
        ).click()
        time.sleep(1)

        # 프로그래머스 선택
        WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, "//li[text()='프로그래머스']"))
        ).click()
        time.sleep(1)

        # 선택하기
        WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, '/html/body/div[1]/div[2]/div[2]/div/div[3]/section/div/div[2]/button[2]'))
        ).click()

        # 출간하기
        WebDriverWait(driver, 30).until(
            EC.element_to_be_clickable((By.XPATH, '/html/body/div[1]/div[2]/div[2]/div/div[3]/div[2]/button[2]'))
        ).click()
        # element = driver.find_element(By.XPATH, '/html/body/div[1]/div[2]/div[2]/div/div[3]/div[2]/button[2]')
        # driver.execute_script('arguments[0].click();', element)
    

if __name__ == '__main__':
    variables = crawl_data()
    driver = create_undetected_driver()

    google_login(driver)
    # time.sleep(10)
    write_content(driver, variables)