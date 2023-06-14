import DatabaseManaging

def perror(*args, **kwargs):
    print("\033[31m", end="")
    print(*args, **kwargs, end="")
    print("\033[0m")

def psucc(*args, **kwargs):
    print("\033[32m", end="")
    print(*args, **kwargs, end="")
    print("\033[0m")


dbw = DatabaseManaging.DatabaseWriter(table="BrowserData", log=True)
dbr = DatabaseManaging.DatabaseReader(table="BrowserData", log=True)

dbw.addField("test", "content", False)
dbr.read("test")
try:
    dbw.addField("test", "content", False)
except DatabaseManaging.DatabaseException as ex:
    perror("it's impossible to add a field with this name")
dbw.deleteField("test")

