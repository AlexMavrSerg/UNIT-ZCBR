import json
from DatabaseManaging import DatabaseWriter as DBW
from DatabaseManaging import DatabaseException as DBE
from src.nieMoje import niemoje

def perror(*args, **kwargs):
    print("\033[31m", end="")
    print(*args, **kwargs, end="")
    print("\033[0m")

def insert(name: str, data: str):
    try:
        dbw.addField(name, data)
    except DBE:
        perror("It's impossible to insert a post with name '{}' because it's already exists in the database".format(name))
    except Exception as e:
        perror("Unexpected error:\n{}".format(e))


dbw = DBW(table="BrowserData", log=True)

print("Inserting Bud' V Dvirzenii:")
for post in niemoje:
    insert(post["name"], json.dumps(post, ensure_ascii=False))

print("Inserting Junarmiejskije Lagieria:")
yunarmy = None
with open("src/yunarmy-res.json", "r", encoding="utf-8") as file:
    yunarmy = json.loads(file.read())
for post_name in yunarmy.keys():
    insert(post_name, json.dumps(yunarmy[post_name], ensure_ascii=False))