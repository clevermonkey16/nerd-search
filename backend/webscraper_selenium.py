import time

from selenium import webdriver 
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By


website = 'https://nvidia.wd5.myworkdayjobs.com/NVIDIAExternalCareerSite?q=intern&locationHierarchy1=2fcb99c455831013ea52fb338f2932d8'

driver = webdriver.Chrome()
driver.get(website)

time.sleep(10)

#frame = driver.find_element("xpath", '//frame[@name="main"]')
#driver.switch_to.frame(frame)
titles = driver.find_elements(By.XPATH, "//a[@data-automation-id='jobTitle']")
for i in titles:
    i.click()
    time.sleep(5)
    jobinfo = driver.find_element(By.XPATH, '//*[@data-automation-id="jobPostingDescription"]').text
    print(jobinfo)
#title.click()

while True:
    ...

driver.quit()

import xlsxwriter