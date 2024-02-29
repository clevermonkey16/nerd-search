import writedata
import time

SQL_data = writedata.SQLWriter("jobs.db")

fValues = ("one","two","three","four","five","six")
dValues = ("a", "b", "c", "d", "e", "f")
cValues = ("aardvark", "bat", "cat", "dog", "elephant", "frog")


SQL_data.insert(fValues)
SQL_data.insert(dValues)
SQL_data.insert(cValues)

SQL_data.remove('e')

#SQL_data.noDupeInsert(fValues)