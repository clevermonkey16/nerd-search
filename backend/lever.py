import time
import writedata
import wordextractor

from selenium import webdriver 
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By

# testing link 'https://jobs.lever.co/cohere'

def scrape(company, link):
# Set Path for to ChromeDriver
    website = link

    options = Options()
    options.add_argument("--headless=new") # Uncomment this line to run headless

    driver = webdriver.Chrome(options=options)
    SQL_data = writedata.SQLWriter("jobs.db")
    driver.get(website)

    time.sleep(0.1)

    #Titles and links are both lists
    titles = driver.find_elements(By.XPATH, '//a[@class="posting-title"]//h5[@data-qa="posting-name"]')
    #this is for the driver to get job_link later on
    links = driver.find_elements(By.XPATH, '//a[@class="posting-title"]')
   
    for j in range(len(titles)):

        name = titles[j].text
        if "intern" not in name.lower(): 
            # print(name, "not an intern job")
            continue
        i = titles[j]

        job_title_info = titles[j].text
        job_link = links[j].get_attribute("href")
        driver.get(job_link)
        time.sleep(0.05)
        location_info = driver.find_element(By.XPATH, '//div[@class="sort-by-time posting-category medium-category-label width-full capitalize-labels location"]').text
        job_info_list = driver.find_elements(By.XPATH, '//*[@class="section-wrapper page-full-width"]')
        job_info = ""
        for i in range(len(job_info_list)):
            #print(job_info_list[i].text)
            job_info += f"{job_info_list[i].text}\n"
            job_info += "\n"
        # no date_posted in lever
        date_posted = 'NULL'
        
        degree_info = wordextractor.degreeextract(job_info)
        salary_info = wordextractor.salaryextract(job_info)
        skills_info = wordextractor.skillsextract(job_info)

        values = (company, job_title_info, location_info, job_info, date_posted, job_link, 1, 'na', degree_info, skills_info, salary_info)
        SQL_data.insert(values)
        driver.back() 
        time.sleep(3)

    #title.click() 
    print("code is done!")
    SQL_data.close()
    driver.quit()


# Testing out script
#scrape("PlusAI", "https://jobs.lever.co/plus-2?")