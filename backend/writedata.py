import sqlite3

class SQLWriter:
    #TITLE, LOCATION, DESCRIPTION, DATE_POSTED, JOB_ID

    def __init__(self, fileName, tableName="jobs"):
        self.connection = sqlite3.connect(fileName)
        self.cursor = self.connection.cursor()
        self.tableName = tableName
        self.query("CREATE TABLE IF NOT EXISTS " + self.tableName +
               """(company_name TEXT,
                   title        TEXT, 
                   location     TEXT, 
                   description  TEXT, 
                   date_posted  TEXT, 
                   link         TEXT UNIQUE,
                   valid        BIT,
                   category     TEXT,
                   degree       TEXT,
                   skills       TEXT,
                   salary       TEXT)""")
        print("Connected to the database")

    def query(self, sql_command, values = ()):
        self.cursor.execute(sql_command, values)
        self.connection.commit()
    
    def remove(self, value): #this to be changed later on
        self.query(f"DELETE FROM {self.tableName} WHERE valid LIKE ?", [value])

    def insert(self, values):
        # values is a tuple of (company, title, location, description, date_posted, link, validity(bit)) 
        try:
            self.query(f"INSERT INTO {self.tableName} VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)", values)
        except sqlite3.IntegrityError:
            self.query(f"UPDATE {self.tableName} SET valid = ? WHERE link LIKE ?", [1, values[5]]) #now the job is "verified" if it is a dupe
            print("job_id not unique", values[5])
        except:
            print("fatal error, entry not inserted")
    
        # Laurence: this is just for me to test what errors i have in my webscraping code, ill delete after done
        #self.query(f"INSERT INTO {self.tableName} VALUES (?, ?, ?, ?, ?, ?)", values)
    
    def allInvalid(self):
        self.query(f"UPDATE {self.tableName} SET valid = ?", [0])

    def nukeInvalid(self):
        self.remove(0)
    
    def nukeTable(self, confirm): #use this one cautiously
        if(confirm == "Yeah, i'm sure"):
            self.cursor.execute(f"DROP TABLE {self.tableName}")
        else:
            print("check your nuclear launch codes")

    def close(self):
        self.connection.close()

if __name__ == "__main__":
    writer = SQLWriter("jobs.db") #Make this an absolute path
    values = ("Software Engineer", "Santa Clara", "We are looking for a software engineer", "2021-08-01", "1234")
    writer.insert(values)
    writer.close()