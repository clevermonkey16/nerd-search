import time
import writedata

from selenium import webdriver 
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By

# Test link: 'https://boards.greenhouse.io/samsungsemiconductor'

def scrape(link):
# Set Path for to ChromeDriver
    website = link

    options = Options()
    options.add_argument("--headless=new") # Uncomment this line to run headless

    driver = webdriver.Chrome(options=options)
    SQL_data = writedata.SQLWriter("jobs.db")
    driver.get(website)

    time.sleep(3)
    #test
    #Titles is a list
    titles = driver.find_elements(By.XPATH, '//a[@data-mapped="true"]')

    for j in range(len(titles)):
        name = titles[j].text
        if "intern" not in name.lower(): 
            # print(name, "not an intern job")
            continue
        i = titles[j]
        job_title_info = titles[j].text
        job_link = titles[j].get_attribute("href")
        i.click()
        #time.sleep(0.2)
        location_info = driver.find_element(By.XPATH, '//div[@class="location"]').text
        job_info = driver.find_element(By.XPATH, '//div[@id="content"]').text
        #date_posted in Greenhouse
        date_posted = 'NULL'

        values = (job_title_info, location_info, job_info, date_posted, job_link, 1)
        SQL_data.insert(values)
        driver.back() 
        #time.sleep(0.2)
        
    #title.click() 

    SQL_data.close()
    driver.quit()

