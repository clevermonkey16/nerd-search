import time
import writedata

from selenium import webdriver 
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By


website = 'https://nvidia.wd5.myworkdayjobs.com/NVIDIAExternalCareerSite?q=intern&locationHierarchy1=2fcb99c455831013ea52fb338f2932d8'

driver = webdriver.Chrome()
SQL_data = writedata.SQLWriter("jobs.db")
driver.get(website)

time.sleep(10)

#frame = driver.find_element("xpath", '//frame[@name="main"]')
#driver.switch_to.frame(frame)
titles = driver.find_elements(By.XPATH, "//a[@data-automation-id='jobTitle']")
for j in range(2):
    i = titles[j]
    i.click()
    time.sleep(5)
    job_title_info = driver.find_element(By.XPATH, '//*[@data-automation-id="jobPostingHeader"]').text
    location_info = driver.find_element(By.XPATH, '//*[@class="css-129m7dg"]').text
    job_info = driver.find_element(By.XPATH, '//*[@data-automation-id="jobPostingDescription"]').text
    query = "INSERT INTO jobs VALUES (?, ?, ?)"
    values = (job_title_info, location_info, job_info)
    SQL_data.query(query, values)

#title.click()
SQL_data.close()
driver.quit()

import xlsxwriter