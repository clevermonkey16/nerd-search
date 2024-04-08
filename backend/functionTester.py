import backend.Webscrapers.writedata as writedata
import time

#SQL_data = writedata.SQLWriter("backend\jobs.db")
SQL_data = writedata.SQLWriter("jobs.db")
fValues = ("one","two","three","four","five", 1)
dValues = ("a", "b", "c", "d", "e", 1)
cValues = ("aardvark", "bat", "cat", "dog", "elephant", 1)


SQL_data.insert(fValues)
SQL_data.insert(dValues)
SQL_data.insert(cValues)


time.sleep(0.5)

#confirmation = input("Are you sure you want to nuke the database (use preagreed codes): ")

#SQL_data.nukeTable(confirmation)

#SQL_data.nukeTable("Yeah, i'm sure")

SQL_data.allInvalid()

SQL_data.nukeInvalid()