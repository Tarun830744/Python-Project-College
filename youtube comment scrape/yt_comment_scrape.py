from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from bs4 import BeautifulSoup
import time
import pandas as pd

def ScrapComment(url):
    option = webdriver.ChromeOptions()
    option.add_argument("--headless")
    driver = webdriver.Chrome(executable_path = ChromeDriverManager().install(), options=option)
    driver.get(url)
    prev_h = 0
    while True:
        height = driver.execute_script("""
                function getActualHeight() {
                    return Math.max(
                        Math.max(document.body.scrollHeight, document.documentElement.scrollHeight),
                        Math.max(document.body.offsetHeight, document.documentElement.offsetHeight),
                        Math.max(document.body.clientHeight, document.documentElement.clientHeight)
                    );
                }
                return getActualHeight();
            """)
        driver.execute_script(f"window.scrollTo({prev_h},{prev_h + 200})")
        time.sleep(1)
        prev_h +=200  
        if prev_h >= height:
            break
    soup = BeautifulSoup(driver.page_source, 'html.parser')
    driver.quit()
    user_text_div = soup.select('#author-text')
    user = [x.text.replace("\n","") for x in user_text_div]
    u = []
    for i in user:
        j = i.replace(' ' ,'')
        u.append(j)
    comment_div = soup.select("#content #content-text")
    comment_list = [x.text.replace("\n", "") for x in comment_div]
    df = pd.DataFrame({'User Name' : u,'Comment':comment_list},index=None)
    print(df)
    df.to_csv(saved + '.csv')

if __name__ == '__main__':
    link = input("Enter Youtube link : ")
    saved = input("Enter Name for file saving : ")
    ScrapComment(link)