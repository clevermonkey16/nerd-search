# Outline:
# 1. Import the required libraries
# 2. Set every valid bit in jobs.db to false
# 3. Read company links from companies.csv
# 4. For each company, start scraping, calling insert() for each job
# 5. Nuke invalid jobs in jobs.db
# 5.5 Possibly have to nuke invalid postings in other databases 
# 6. Close the database connection

from Webscrapers import workday


def scrape(type, link):
    if type == "workday":
        workday.scrape(link)
    elif type == "eightfold":
        eightfold.scrape(link)
    elif type == "lever":
        lever.scrape(link)
    else:
        print("bruh it no correct")
        pass
        
if __name__ == "__main__":
    scrape("workday", "https://nvidia.wd5.myworkdayjobs.com/NVIDIAExternalCareerSite?q=intern&locationHierarchy1=2fcb99c455831013ea52fb338f2932d8")

