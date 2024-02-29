import sqlite3

class SQLWriter:
    #TITLE, LOCATION, DESCRIPTION, DATE_POSTED, JOB_ID

    def __init__(self, fileName, tableName="jobs"):
        self.connection = sqlite3.connect(fileName)
        self.cursor = self.connection.cursor()
        self.tableName = tableName
        self.query("CREATE TABLE IF NOT EXISTS " + self.tableName +
               """(title        TEXT, 
                   location     TEXT, 
                   description  TEXT, 
                   date_posted  TEXT, 
                   job_id       TEXT UNIQUE, """ #Note that we verify for uniqueness using job_id
                  "link         TEXT UNIQUE)")
        print("Connected to the database")

    def query(self, sql_command, values = ()):
        self.cursor.execute(sql_command, values)
        self.connection.commit()
    
    def remove(self, value): #this to be changed later on
        self.query(f"DELETE FROM {self.tableName} WHERE job_id LIKE ?", value)

    def insert(self, values):
        # values is a tuple of (title, location, description, date_posted, job_id, link)
        try:
            self.query(f"INSERT INTO {self.tableName} VALUES (?, ?, ?, ?, ?, ?)", values)
        except:
            print("job_id not unique")

    def close(self):
        self.connection.close()

if __name__ == "__main__":
    writer = SQLWriter("jobs.db") #Make this an absolute path
    #writer.query("DROP TABLE IF EXISTS duplicate_table")
    values = ("Software Engineer", "Santa Clara", "We are looking for a software engineer", "2021-08-01", "1234")
    writer.insert(values)
    writer.close()