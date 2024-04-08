# Outline:
# 1. Import the required libraries
# 2. Set every valid bit in jobs.db to false
# 3. Read company links from companies.csv
# 4. For each company, start scraping, calling insert() for each job
# 5. Nuke invalid jobs in jobs.db
# 5.5 Possibly have to nuke invalid postings in other databases 
# 6. Close the database connection

import workday
import eightfold
import lever
import greenhouse


def scrape(type, link):
    if type == "workday":
        workday.scrape(link)
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
    scrape("lever", "https://jobs.lever.co/cohere")

