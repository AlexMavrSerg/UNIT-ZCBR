from DatabaseManaging import DatabaseWriter as DBW
from DatabaseManaging import DatabaseReader as DBR
from DatabaseManaging import DatabaseException as DBE

dbr = DBR(table="BrowserData", log=True)
all = dbr.read("__ALLPOSTS__")

dbw = DBW(table="BrowserData", log=True)
for post in all:
    dbw.deleteField(post[0])