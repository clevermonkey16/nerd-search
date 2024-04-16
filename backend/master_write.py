# Outline:
# 1. Import the required libraries
# 2. Set every valid bit in jobs.db to false
# 3. Read company links from companies.csv
# 4. For each company, start scraping, calling insert() for each job
# 5. Nuke invalid jobs in jobs.db
# 5.5 Possibly have to nuke invalid postings in other databases 
# 6. Close the database connection

import csv

import workday
import greenhouse
import lever
import eightfold
import writedata


def scrape(type, link):
    if type == "workday":
        workday.scrape(link)
    elif type == "greenhouse":
        greenhouse.scrape(link)
    elif type == "eightfold":
        eightfold.scrape(link)
    elif type == "lever":
        lever.scrape(link)
    elif type == "greenhouse":
        greenhouse.scrape(link)
    else:
        print("bruh it no correct")
        pass

    
if __name__ == "__main__":
    SQL_data = writedata.SQLWriter("jobs.db")
    
    # 2. Set every valid bit in jobs.db to false
    SQL_data.allInvalid()

    # 3. Read company links from companies.csv
    """
    with open('companies.csv', 'r') as file:
        csv_reader = csv.reader(file)
        for row in csv_reader:

            # 4. For each company, start scraping, calling insert() for each job
            company = row[0]
            type = row[1]
            link = row[2]


    # 4. For each company, start scraping, calling insert() for each job
    # scrape("workday", "https://nvidia.wd5.myworkdayjobs.com/NVIDIAExternalCareerSite?q=intern&locationHierarchy1=2fcb99c455831013ea52fb338f2932d8")
    # scrape("lever", "https://jobs.lever.co/cohere") # broken
    # scrape("greenhouse", "https://boards.greenhouse.io/samsungsemiconductor")
    scrape("eightfold", "https://careers.qualcomm.com/careers/?query=intern&location=United%20States&pid=446694599363&domain=qualcomm.com&sort_by=relevance&triggerGoButton=false&triggerGoButton=true")

    SQL_data.nukeInvalid()
    SQL_data.close()


