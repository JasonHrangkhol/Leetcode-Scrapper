from matplotlib.pyplot import get
from selenium import webdriver
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.options import Options
from setuptools import PEP420PackageFinder
from fpdf import FPDF
import yaml
import sys
import random


options = webdriver.ChromeOptions()
options.add_argument("--headless")

# options = webdriver.ChromeOptions()
# options.add_experimental_option('excludeSwitches', ['enable-logging'])
# driver = webdriver.Chrome(options=options)


capa = DesiredCapabilities.CHROME
capa["pageLoadStrategy"] = "none"

url = "https://leetcode.com/"

cfg = yaml.full_load(open(sys.argv[1], 'r'))

driver_path = cfg['driver_path']
number_of_problems =int(cfg['number_of_problems'])
difficulty = cfg['difficulty']
status = cfg['status']
tags = cfg['tags']
email = cfg['email'] 
password = cfg['password']

tags = list(tags.strip().split(','))

driver = webdriver.Chrome(options=options, executable_path = driver_path)
driver.maximize_window()
driver.get(url)

signIn = driver.find_element_by_css_selector('a[href="/accounts/login/"]')
signIn.click()
    
login = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.ID, "id_login"))
    )
password_field = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.ID, "id_password"))
    )

login.send_keys(email)
password_field.send_keys(password)
password_field.send_keys(Keys.RETURN)

WebDriverWait(driver, 10).until(
        EC.invisibility_of_element((By.ID, 'initial-loading'))
    )

problems = WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.CSS_SELECTOR, 'a[href="/problemset/all/"]'))
    )

problems.click()

driver.execute_script("window.scrollTo(0,600)")

if difficulty != "None":

    WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.XPATH, '/html/body/div/div/div/div[1]/div[1]/div[6]/div[1]/div/div[1]/div[2]/div/button'))
    )

    difficulty_button = driver.find_element_by_xpath('/html/body/div/div/div/div[1]/div[1]/div[6]/div[1]/div/div[1]/div[2]/div/button')
    difficulty_button.click()

    if difficulty == 'Easy':
        easy = WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.CSS_SELECTOR, 'span[class="text-olive dark:text-dark-olive"]'))
        )
        easy.click()
    
    elif difficulty == 'Medium':
        Medium = WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.CSS_SELECTOR, 'span[class="text-yellow dark:text-dark-yellow"]'))
        )
        Medium.click()
    
    else:
        Hard = WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.CSS_SELECTOR, 'span[class="text-pink dark:text-dark-pink"]'))
        )
        Hard.click()

if status != "None":

    WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.XPATH, '/html/body/div[1]/div/div/div[1]/div[1]/div[6]/div[1]/div/div[1]/div[3]/div/button'))
    )

    status_button = driver.find_element_by_xpath('/html/body/div[1]/div/div/div[1]/div[1]/div[6]/div[1]/div/div[1]/div[3]/div/button')
    status_button.click()

    if status == 'Todo':
        Todo = WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.XPATH, '/html/body/div[1]/div/div/div[1]/div[1]/div[6]/div[1]/div[1]/div[1]/div[3]/div[2]/div[1]/div/div/span'))
        )
        Todo.click()

    elif status == 'Solved':
        Solved = WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.XPATH, '/html/body/div[1]/div/div/div[1]/div[1]/div[6]/div[1]/div[1]/div[1]/div[3]/div[2]/div[2]/div/div/span'))
        )
        Solved.click()

    else:
        Attempted = WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.XPATH,'/html/body/div[1]/div/div/div[1]/div[1]/div[6]/div[1]/div[1]/div[1]/div[3]/div[2]/div[3]/div/div/span'))
        )
        Attempted.click()

if len(tags)!=0:
        
    WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.XPATH, '/html/body/div[1]/div/div/div[1]/div[1]/div[6]/div[1]/div/div[1]/div[4]/button'))
    )

    tags_button = driver.find_element_by_xpath('/html/body/div[1]/div/div/div[1]/div[1]/div[6]/div[1]/div/div[1]/div[4]/button')
    tags_button.click()

    WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.XPATH, '/html/body/div[1]/div/div/div[1]/div[1]/div[6]/div[1]/div[1]/div[1]/div[4]/div/div/div[2]/div[1]/div/div'))
    )

    expand = driver.find_element_by_xpath('/html/body/div[1]/div/div/div[1]/div[1]/div[6]/div[1]/div[1]/div[1]/div[4]/div/div/div[2]/div[1]/div/div')
    expand.click()

    
    for tag in tags:
        tag = tag.strip()
        try:
            option =driver.find_element_by_css_selector(f'span[data-name="{tag}"]')
        except:
            
            WebDriverWait(driver, 10).until(
                EC.presence_of_element_located((By.XPATH, '/html/body/div[1]/div/div/div[1]/div[1]/div[6]/div[1]/div[1]/div[1]/div[4]/div/div/div[2]/div[1]/div'))
            )
            sroll_bar = driver.find_element_by_xpath('/html/body/div[1]/div/div/div[1]/div[1]/div[6]/div[1]/div[1]/div[1]/div[4]/div/div/div[2]/div[1]/div')
            driver.execute_script("scroll_bar.scrollTo(0,600)")
            option =driver.find_element_by_css_selector(f'span[data-name="{tag}"]')
        
        option.click()
       
    WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.XPATH, '/html/body/div[1]/div/div/div[1]/div[1]/div[6]/div[1]/div/div[1]/div[4]/button'))
    )

    tags_button = driver.find_element_by_xpath('/html/body/div[1]/div/div/div[1]/div[1]/div[6]/div[1]/div/div[1]/div[4]/button')
    tags_button.click()

url = driver.current_url

def get_problem(url):

    driver.get(url)

    problem_info = {}
    cnt=0
    indx = 1
    while cnt<60:
         
        try:
            WebDriverWait(driver, 10).until(
                    EC.presence_of_element_located((By.XPATH,f'//*[@id="__next"]/div/div/div[1]/div[1]/div[6]/div[2]/div/div/div[2]/div[{indx}]/div[2]'))
                )
            problem_name = driver.find_element_by_xpath(f'//*[@id="__next"]/div/div/div[1]/div[1]/div[6]/div[2]/div/div/div[2]/div[{indx}]/div[2]').text
            problem_url = driver.find_element_by_xpath(f'//*[@id="__next"]/div/div/div[1]/div[1]/div[6]/div[2]/div/div/div[2]/div[{indx}]/div[2]/div/div/div/div/a').get_attribute('href')
            problem_info[problem_name] = problem_url
            print(indx," ",problem_name," ",problem_url)
            cnt = cnt+1
            indx = indx+1
        except:
            print(indx)
            #try:
               
            driver.execute_script("window.scrollTo(0,document.body.scrollHeight)")
            WebDriverWait(driver, 10).until(
                EC.element_to_be_clickable((By.XPATH,'/html/body/div/div/div/div[1]/div[1]/div[6]/div[3]/nav/button[5]'))
            )
                
            next_page = driver.find_element_by_xpath('/html/body/div/div/div/div[1]/div[1]/div[6]/div[3]/nav/button[5]')
            next_page.click()
            indx=1
            
            url = driver.current_url
            print(driver.current_url)
            driver.get(url)
            print("Successs")
            #except:
            #    return problem_info

    return problem_info

     
def to_pdf(problem_name, problem_url):
    
    pdf = FPDF()
    pdf.add_page()
    pdf.set_font("Arial", size = 15)
    #set name
    name=problem_name.encode('latin-1', 'replace').decode('latin-1')
    #set url
    url=problem_url
    pdf.cell(200, 10, txt =name, ln = 1, align = 'C')
    pdf.write(5, 'Problem_Link: ')
    pdf.write(5,url,url)
    name = name.rstrip()
    pdf.output("./LeetCode-Scrapper/"+name+".pdf")

def main():
    
    problem_info = get_problem(url)
    print(len(problem_info))

    problem_set = {}

    while len(problem_set)<number_of_problems:
        problem_name, problem_url = random.choice(list(problem_info.items()))
        problem_set[problem_name] = problem_url


    # for problem_name, problem_url in problem_set.items():
    #     to_pdf(problem_name, problem_url)
        
if __name__=="__main__":
    
    main()
    driver.quit()