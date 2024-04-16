import time
import writedata

from selenium import webdriver 
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains

def scrape(link):
    # Set Path for to ChromeDriver
    website = link

    driver = webdriver.Chrome()
    SQL_data = writedata.SQLWriter("jobs.db")
    driver.get(website)

    time.sleep(5)
    #test
    #Titles and location are a lists
    try:
        removeBlocker = driver.find_element(By.XPATH, '//button[@class="onetrust-close-btn-handler onetrust-close-btn-ui banner-close-button ot-close-icon"]')
        removeBlocker.click()
    except:
        print("hello")
    showMorePositions = driver.find_element(By.XPATH, '//button[@class="btn btn-sm btn-secondary show-more-positions"]')
    driver.execute_script("arguments[0].scrollIntoView();", showMorePositions)
    time.sleep(5)
    
    actions = ActionChains(driver)
    actions.move_to_element(showMorePositions).perform()
    actions.move_by_offset(0, -(driver.get_window_size()['height'] / 2))

    
    time.sleep(5)
    showMorePositions.click()
    titles = driver.find_elements(By.XPATH, '//*[contains(@data-test-id, "position-card")]')
    #location = driver.find_elements(By.XPATH, '//p[@class="field-label"]')

    for j in range(len(titles)):
        i = titles[j]
        #location_info = location[j].text
        #link = titles[j].get_attribute("href")
        i.click()
<<<<<<< HEAD
        time.sleep(3)
        job_link = driver.current_url
        location_info = driver.find_element(By.XPATH, '//*[@class="position-location"]').text
=======

        time.sleep(5)
        job_link = driver.current_url

>>>>>>> 7b6ae08cd9bf913efaa1e868bc80782f55ed62df
        job_title_info = driver.find_element(By.XPATH, '//*[@class="position-title"]').text
        job_info = driver.find_element(By.XPATH, '//div[@class="position-job-description"]').text

        # from the two eightfold websites, one of them did not have date posted
        try:
            date_posted = driver.find_element(By.XPATH, '//div[@class="custom-jd-field col-md-2"]').text
        except:
            date_posted = 'NULL'

        values = (job_title_info, location_info, job_info, date_posted, job_link, 1)
        SQL_data.insert(values)
<<<<<<< HEAD
=======
        time.sleep(3)
>>>>>>> 7b6ae08cd9bf913efaa1e868bc80782f55ed62df


        
    #title.click() 

    SQL_data.close()
    driver.quit()

scrape('https://careers.qualcomm.com/careers/?query=intern&location=United%20States&pid=446694599363&domain=qualcomm.com&sort_by=relevance&triggerGoButton=false&triggerGoButton=true')