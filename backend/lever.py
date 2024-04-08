import time
import writedata as writedata

from selenium import webdriver 
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By

# testing link 'https://jobs.lever.co/cohere'

def scrape(link):
# Set Path for to ChromeDriver
    website = link

    driver = webdriver.Chrome()
    SQL_data = writedata.SQLWriter("jobs.db")
    driver.get(website)

    time.sleep(10)

    #Titles and Job_title are both lists
    titles = driver.find_elements(By.XPATH, '//a[@class="posting-title"]')
    #job_title = driver.find_elements(By.XPATH, '//*[@data-qa="posting-name"]')

    for j in range(3):
        i = titles[j]
        #job_title_info = job_title[j].text
        job_title_info = titles[j].text
        link = titles[j].get_attribute("href")
        i.click()
        time.sleep(5)
        location_info = driver.find_element(By.XPATH, '//div[@class="sort-by-time posting-category medium-category-label width-full capitalize-labels location"]').text
        job_info = driver.find_element(By.XPATH, '//div[@class="section-wrapper page-full-width"]').text
        # No job_id or date_posted in lever
        job_id = 'NULL'
        date_posted = 'NULL'
        values = (job_title_info, location_info, job_info, date_posted, job_id, link)
        SQL_data.insert(values)
        driver.back() 
        time.sleep(5)


    #title.click() 
    SQL_data.close()
    driver.quit()

