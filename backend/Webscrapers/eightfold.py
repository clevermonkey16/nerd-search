import time
import writedata

from selenium import webdriver 
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By

# Set Path for to ChromeDriver
website = 'https://careers.qualcomm.com/careers/?query=intern&location=United%20States&pid=446694599363&domain=qualcomm.com&sort_by=relevance&triggerGoButton=false&triggerGoButton=true'


driver = webdriver.Chrome()
SQL_data = writedata.SQLWriter("jobs.db")
driver.get(website)

time.sleep(10)
#test
#Titles and location are a lists



showMorePositions = driver.find_element(By.XPATH, '//div[@class="iframe-button-wrapper"]')
showMorePositions.click()

titles = driver.find_elements(By.XPATH, '//*[contains(@data-test-id, "position-card")]')
location = driver.find_elements(By.XPATH, '//p[@class="field-label"]')

time.sleep(5) 

# modify range later depending 
for j in range(2):
    i = titles[j]
    location_info = location[j].text
    #link = titles[j].get_attribute("href")
    i.click()
    time.sleep(5)
    link = driver.current_url
    job_title_info = driver.find_element(By.XPATH, '//*[@class="position-title"]').text
    job_info = driver.find_element(By.XPATH, '//div[@class="position-job-description"]').text

    # from the two eightfold websites, one of them did not have date posted
    try:
        date_posted = driver.find_element(By.XPATH, '//div[@class="custom-jd-field col-md-2"]').text
    except:
        data_posted = 'NULL'

    values = (job_title_info, location_info, job_info, date_posted, link, 1)
    SQL_data.insert(values)
    time.sleep(5)


    
#title.click() 

SQL_data.close()
driver.quit()

