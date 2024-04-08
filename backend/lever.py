import time
import writedata

from selenium import webdriver 
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By

# testing link 'https://jobs.lever.co/cohere'

def scrape(link):
# Set Path for to ChromeDriver
    website = link

    options = Options()
    options.add_argument("--headless=new") # Uncomment this line to run headless

    driver = webdriver.Chrome(options=options)
    SQL_data = writedata.SQLWriter("jobs.db")
    driver.get(website)

    time.sleep(10)

    #Titles and Job_title are both lists
    titles = driver.find_elements(By.XPATH, '//a[@class="posting-title"]')
    #job_title = driver.find_elements(By.XPATH, '//*[@data-qa="posting-name"]')

    for j in range(len(titles)):
        i = titles[j]
        #job_title_info = job_title[j].text
        job_title_info = titles[j].text
        link = titles[j].get_attribute("href")
        i.click()
        time.sleep(5)
        location_info = driver.find_element(By.XPATH, '//div[@class="sort-by-time posting-category medium-category-label width-full capitalize-labels location"]').text
        job_info = driver.find_element(By.XPATH, '//div[@class="section-wrapper page-full-width"]').text
        # date_posted in lever
        date_posted = 'NULL'
        values = (job_title_info, location_info, job_info, date_posted, link, 1)
        SQL_data.insert(values)
        driver.back() 
        time.sleep(5)


    #title.click() 
    SQL_data.close()
    driver.quit()

