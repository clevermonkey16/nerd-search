import sqlite3

class SQLWriter:
    def __init__(self, fileName):
        self.connection = sqlite3.connect(fileName)
        self.cursor = self.connection.cursor()
        print("Connected to the database")

    def write(self, sql_command):
        self.cursor.execute(sql_command)
        self.connection.commit()

    def close(self):
        self.connection.close()

if __name__ == "__main__":
    writer = SQLWriter("jobs.db")
    writer.write("CREATE TABLE jobs (title TEXT, location TEXT, description TEXT)")
    writer.write("INSERT INTO jobs VALUES ('Software Engineer', 'Santa Clara', 'We are looking for a software engineer')")
    writer.close()