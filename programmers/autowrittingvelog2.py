from glob import glob
from bs4 import BeautifulSoup
import requests
import os
import shutil
from seleniumbase import Driver
import time
import pyperclip
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import Keys

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

        title = soup.select_one('#tab > div.challenge-nav-left-menu > div.nav-item.algorithm-nav-link.algorithm-title > span').text.lstrip().rstrip()

        result = []
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

        # print(result)

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

def create_driver():
    driver = Driver(
        uc=True,           # undetected 모드
        headless=False,    # 브라우저 창 표시 (디버깅용)
        incognito=True,    # 시크릿 모드
        # guest_mode=True, # 게스트 모드 (필요시)
    )

    return driver

def google_login(driver):
    driver.open('https://v3.velog.io/api/auth/v3/social/redirect/google?next=&isIntegrate=0')

    # 아이디 입력
    driver.wait_for_element("input[type='email']", timeout=10)
    driver.type("input[type='email']", "remember33330")
    # 다음 버튼
    driver.wait_for_element("/html/body/div[1]/div[1]/div[2]/c-wiz/div/div[3]/div/div[1]/div/div/button", timeout=10)
    driver.click("/html/body/div[1]/div[1]/div[2]/c-wiz/div/div[3]/div/div[1]/div/div/button")
    # 비밀번호 입력
    driver.wait_for_element("input[type='password']", timeout=10)
    driver.type("input[type='password']", "tmddlf795")
    # 다음 버튼
    driver.wait_for_element('//*[@id="passwordNext"]/div/button', timeout=10)
    driver.click('//*[@id="passwordNext"]/div/button')

def write_content(driver, variables):
    for i in range(len(variables)):
        title, velog_content_all = variables[f'page_{i}']
        pass

    # 새 글 작성
    driver.wait_for_element('//*[@id="html"]/body/div/div[2]/div[2]/div/header/div/div[2]/a[3]/button', timeout=10)
    driver.click('//*[@id="html"]/body/div/div[2]/div[2]/div/header/div/div[2]/a[3]/button')

    # 제목 작성
    driver.wait_for_element('//*[@id="root"]/div[2]/div/div[1]/div/div[1]/div[1]/div/textarea')
    driver.type('//*[@id="root"]/div[2]/div/div[1]/div/div[1]/div[1]/div/textarea', '프로그래머스 ' + title)

    #  태그 입력
    driver.wait_for_element('//*[@id="root"]/div[2]/div/div[1]/div/div[1]/div[1]/div/div[2]/div/input')
    driver.type('//*[@id="root"]/div[2]/div/div[1]/div/div[1]/div[1]/div/div[2]/div/input', '프로그래머스, 파이썬,')
    # time.sleep(100)

    # 내용 쓰기
    driver.wait_for_element('//*[@id="root"]/div[2]/div/div[1]/div/div[1]/div[3]/div/div[6]/div[1]/div/div/div/div[5]')
    # elemlent = driver.find_element('//*[@id="root"]/div[2]/div/div[1]/div/div[1]/div[3]/div/div[6]/div[1]/div/div/div/div[5]')
    driver.click('//*[@id="root"]/div[2]/div/div[1]/div/div[1]/div[3]/div/div[6]/div[1]/div/div/div/div[5]')
    act = ActionChains(driver)

    pyperclip.copy(velog_content_all)
    act.key_down(Keys.CONTROL).send_keys("v").perform()
    # 출간하기 버튼 클릭
    driver.wait_for_element('//*[@id="root"]/div[2]/div/div[1]/div/div[2]/div/div/button[2]', timeout=10)
    driver.click('//*[@id="root"]/div[2]/div/div[1]/div/div[2]/div/div/button[2]')

    # 시리즈 버튼 클릭
    driver.wait_for_element('//*[@id="root"]/div[2]/div[2]/div/div[3]/div[1]/section[3]/div/button', timeout=10)
    driver.click('//*[@id="root"]/div[2]/div[2]/div/div[3]/div[1]/section[3]/div/button')

    # 프로그래머스 선택
    driver.wait_for_element('//*[@id="root"]/div[2]/div[2]/div/div[3]/section/div/div[1]/ul//li[contains(text(), "프로그래머스")]')
    driver.click('//*[@id="root"]/div[2]/div[2]/div/div[3]/section/div/div[1]/ul//li[contains(text(), "프로그래머스")]')

    # 선택하기
    driver.wait_for_element('//*[@id="root"]/div[2]/div[2]/div/div[3]/section/div/div[2]/button[2]', timeout=10)
    driver.click('//*[@id="root"]/div[2]/div[2]/div/div[3]/section/div/div[2]/button[2]')

    time.sleep(5)

    # 출간하기 버튼 클릭
    driver.wait_for_element('//*[@id="root"]/div[2]/div[2]/div/div[3]/div[2]/button[2]', timeout=10)
    driver.click('//*[@id="root"]/div[2]/div[2]/div/div[3]/div[2]/button[2]')
    


    time.sleep(5)
if __name__ =='__main__':
    variables = crawl_data()
    driver = create_driver()
    google_login(driver)
    write_content(driver, variables)