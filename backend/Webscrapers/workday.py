import time
import writedata

from selenium import webdriver 
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By

# Testing Link
# https://nvidia.wd5.myworkdayjobs.com/NVIDIAExternalCareerSite?q=intern&locationHierarchy1=2fcb99c455831013ea52fb338f2932d8

def scrape(link):
    # Set Path for to ChromeDriver
    website = link

    driver = webdriver.Chrome()
    #SQL_data = writedata.SQLWriter("backend\jobs.db")
    SQL_data = writedata.SQLWriter("jobs.db")
    driver.get(website)

    time.sleep(10)

    #frame = driver.find_element("xpath", '//frame[@name="main"]')
    #driver.switch_to.frame(frame)


    # This is specifically for Workday websites
    # Extract internship information and store in SQL db
    # titles, job_ids, and list_link is a list
    titles = driver.find_elements(By.XPATH, "//a[@data-automation-id='jobTitle']")
    flag = True
    while(flag):
        # This is just for error handling
        for i in range(len(titles)):
            print(titles[i].text)

        for j in range(len(titles)):
            try:
                link = titles[j].get_attribute("href")
                i = titles[j]
                i.click()
                time.sleep(5)
                job_title_info = driver.find_element(By.XPATH, '//*[@data-automation-id="jobPostingHeader"]').text
                #can not figure out location_info 
                location_info = driver.find_element(By.XPATH, '//dd[@class="css-129m7dg"]').text
                job_info = driver.find_element(By.XPATH, '//*[@data-automation-id="jobPostingDescription"]').text
                date_posted = driver.find_element(By.XPATH, '//div[@data-automation-id="postedOn"]').text
                values = (job_title_info, location_info, job_info, date_posted, link, 1) #if a job is inserted, it's validity is set to 1
                SQL_data.insert(values)
            except:
                print("nothing to print")
                

        try:
            time.sleep(5)
            nextButton = driver.find_element(By.XPATH, '//button[@data-uxi-widget-type="stepToNextButton"]')
            nextButton.click()
            time.sleep(10)
            titles = driver.find_elements(By.XPATH, "//a[@data-automation-id='jobTitle']")
        except:
            flag = False
            
    print("Code is done!")

    #title.click() 
    SQL_data.close()
    driver.quit()
