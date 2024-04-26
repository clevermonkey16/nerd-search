import time
import writedata
import wordextractor

from selenium import webdriver 
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By

# Test link: 'https://boards.greenhouse.io/samsungsemiconductor'

def scrape(company, link):
# Set Path for to ChromeDriver
    website = link

    options = Options()
    options.add_argument("--headless=new") # Uncomment this line to run headless

    driver = webdriver.Chrome(options=options)
    SQL_data = writedata.SQLWriter("jobs.db")
    driver.get(website)

    time.sleep(0.1)
    #test
    #Titles is a list
    titles = driver.find_elements(By.XPATH, '//a[@data-mapped="true"]')
    
    #for j in range(len(titles)):
    for j in range(len(titles)):
        name = titles[j].text
        if "intern" not in name.lower(): 
            # print(name, "not an intern job")
            continue
        i = titles[j]
        job_title_info = titles[j].text
        job_link = titles[j].get_attribute("href")
        i.click()
        time.sleep(0.05)
        location_info = driver.find_element(By.XPATH, '//div[@class="location"]').text
        job_info_list = driver.find_elements(By.XPATH, '//div[@id="content"]')
        job_info = ""
        for i in range(len(job_info_list)):
            #print(job_info_list[i].text)
            job_info += f"{job_info_list[i].text}\n"
            job_info += "\n\n"
        print(job_info)
        #date_posted in Greenhouse
        date_posted = 'NULL'

        degree_info = wordextractor.degreeextract(job_info)
        salary_info = wordextractor.salaryextract(job_info)
        skills_info = wordextractor.skillsextract(job_info)
        
        
        values = (company, job_title_info, location_info, job_info, date_posted, job_link, 1, 'NA', degree_info, skills_info, salary_info)
        SQL_data.insert(values)
        driver.back() 
        #time.sleep(0.2)
        
    #title.click() 
    print("Code is done!")

    SQL_data.close()
    driver.quit()


#scrape('Samsung', 'https://boards.greenhouse.io/samsungsemiconductor')

