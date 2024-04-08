import time
import backend.writedata as writedata

from selenium import webdriver 
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By

# Test link: 'https://boards.greenhouse.io/samsungsemiconductor'

def scrape(link):
# Set Path for to ChromeDriver
    website = link

    driver = webdriver.Chrome()
    SQL_data = writedata.SQLWriter("jobs.db")
    driver.get(website)

    time.sleep(10)
    #test
    #Titles is a list
    titles = driver.find_elements(By.XPATH, '//a[@data-mapped="true"]')

    for j in range(len(titles)):
        i = titles[j]
        job_title_info = titles[j].text
        link = titles[j].get_attribute("href")
        i.click()
        time.sleep(5)
        location_info = driver.find_element(By.XPATH, '//div[@class="location"]').text
        job_info = driver.find_element(By.XPATH, '//div[@id="content"]').text
        # No job_id or date_posted in Greenhouse
        job_id = 'NULL'
        date_posted = 'NULL'

        values = (job_title_info, location_info, job_info, date_posted, job_id, link)
        SQL_data.insert(values)
        driver.back() 
        time.sleep(5)
        
    #title.click() 

    SQL_data.close()
    driver.quit()

