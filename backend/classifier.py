import writedata
from dataClassification import data_classify

def classify():
    # 1. Connect to the database
    SQL_data = writedata.SQLWriter("jobs.db")

    # Iterate over rows of database
    cursor = SQL_data.cursor
    cursor.execute("SELECT * FROM jobs")
    jobs = cursor.fetchall()
    #cursor.close()

    #print(jobs)

    #for j in range(len(jobs[0])):
    #        print(jobs[0][j])

    black_box = data_classify()
    
    for i in range(len(jobs)):
        title = jobs[i][1]
        description = jobs[i][3]
        link = jobs[i][5]
        #valid = jobs[i][6]
        category = jobs[i][7]


        # determining tech vs non-tech
        is_this_thing_valid_or_not = black_box.isTech(title)

        #print(is_this_thing_valid_or_not)

        # If classifier returns false, make row bit invalid
        if not is_this_thing_valid_or_not:
            SQL_data.updateValid(link, 0)
        
        # determine if it's intern or not
        bad_words = ["internal", "international"]
        for word in bad_words:
            if word in title.lower():
                SQL_data.updateValid(link, 0)
                is_this_thing_valid_or_not = False
                break

        keyWord = black_box.kWordSearch(title.lower()) 

        #print(keyWord)

        if is_this_thing_valid_or_not:
            if keyWord != "no_kClass":
                SQL_data.updateCategory(link, keyWord)
            else:
                # Run black box classifier on infos
                cat = black_box.classify(description)
                #print(cat)
                SQL_data.updateCategory(link, cat)

    # nuke table of invalid jobs
    # SQL_data.nukeInvalid()

    # close database connection
    # SQL_data.close()

if __name__ == "__main__":
    SQL_data = writedata.SQLWriter("jobs.db")

    SQL_data.updateCategory("https://nvidia.wd5.myworkdayjobs.com/en-US/NVIDIAExternalCareerSite/job/US-CA-Santa-Clara/Research-Intern--ASIC-and-VLSI---Summer-2024_JR1974986?q=intern&locationHierarchy1=2fcb99c455831013ea52fb338f2932d8", "na")
    SQL_data.close()

    classify()