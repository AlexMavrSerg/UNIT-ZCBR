# UNIT-ZCBR
ЮНИТ ЗЦБР

## Модуль: DatabaseManaging

### ВАЖНО:
Модуль предназначен только для работы с таблицами формата (name | data), с другими таблицами работать не будет.

Модуль имеет 3 класса:
- DatabaseReader
- DatabaseWriter
- DatabaseException

Первый класс (DatabaseReader) отвечает за чтение с таблицы. Имеет две функции (по идее доступные пользователю) для получения информации из бд и одну для установки таблицы, из которой будет происходить сбор информации.

```python3
from DatabaseManaging import DatabaseReader

dbr = DatabaseReader() # Создание объекта класса
dbr.setTable("table for test") # указание таблицы

result = None
if dbr.fieldExists("some name"): # Проверка на существование строки 
    result = dbr.read("some name") # Чтение строки
else:
    result = dbr.read("__ALLPOSTS__") # Значение __ALLPOSTS__ говорит программе, что вы хотите получить все строки из таблицы

print(result)
```

Второй класс (DatabaseWriter) отвечает за изменения в таблице, а именно за запись и удаление строк. Также возможна перезапись строк. Ему также можно указать рабочую таблицу.

```python3
from DatabaseManaging import DatabaseWriter

dbw = DatabaseWriter()
dbw.setTable("table for test")

dbw.addField("some name", "some data") # Запись строки в таблицу (название строки, информация)
dbw.deleteField("some name") # Удаление строки
```

Третий класс (DatabaseException) является вспомогательным и он служит помощью в отлавливании ошибок, связанных именно с модулем DatabaseManaging.

```python3
from DatabaseManaging import DatabaseWriter, DatabaseException

dbw = DatabaseWriter(table="some table") # Таблицу можно указать при создании

new_name = "new name"
new_data = "new data"
try:
    dbw.addField(new_name, new_data, False) # Запрещаю перезапись строк, в случае, если строка с таким названием существует, будет выкинуто исключение DatabaseException
except DatabaseException:
    print("There is already exists this fieald")
except Exception as e:
    print("Unexpected exception:\n{}".format(e))
```
