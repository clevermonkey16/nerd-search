import time
import writedata

from selenium import webdriver 
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By

# Set Path for to ChromeDriver
website = 'https://nvidia.wd5.myworkdayjobs.com/NVIDIAExternalCareerSite?q=intern&locationHierarchy1=2fcb99c455831013ea52fb338f2932d8'

driver = webdriver.Chrome()
SQL_data = writedata.SQLWriter("jobs.db")
driver.get(website)

time.sleep(10)

#frame = driver.find_element("xpath", '//frame[@name="main"]')
#driver.switch_to.frame(frame)


# This is specifically for Workday websites
# Extract internship information and store in SQL db
# titles, job_ids, and list_link is a list
titles = driver.find_elements(By.XPATH, "//a[@data-automation-id='jobTitle']")
job_ids = driver.find_elements(By.XPATH, '//li[@class="css-h2nt8k"]')

for j in range(2):
    job_id = job_ids[j].text
    link = titles[j].get_attribute("href")
    i = titles[j]
    i.click()
    time.sleep(5)
    job_title_info = driver.find_element(By.XPATH, '//*[@data-automation-id="jobPostingHeader"]').text
    # What about the cases in which there are two locations?
    location_info = driver.find_element(By.XPATH, '//*[@data-automation-id="locations"]').text
    job_info = driver.find_element(By.XPATH, '//*[@data-automation-id="jobPostingDescription"]').text
    date_posted = driver.find_element(By.XPATH, '//div[@data-automation-id="postedOn"]').text
    values = (job_title_info, location_info, job_info, date_posted, job_id, link)
    #SQL_data.query(query, values)
    SQL_data.insert(values)

#title.click() 
SQL_data.close()
driver.quit()

