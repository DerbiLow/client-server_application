# client-server_application

|**Ветвь**|**Содержимое**|
|---------|--------------|
|main|Версия с мониторингом|
|SQL|Все про БД|

# SQL

|**Номер**|**Элемент**|**Свойство 1**|**Свойство 2**|
|---------|--------------|--------------|--------------|
| 1 |элемент| свойства | свойства |

В SQL каждая строка хранит свой элемент, а элемент делится на свойства/аргументы (свойства)<br>

Все ключевые слова в SQL пишутся с большой буквы.

# Выборка

* Для выбора из таблиц используется SELECT

SELECT <variable_name> <br>
FROM <table_name>;

* При многочисленной выборе, элементы указываются через запятую.

SELECT <variable_name>, <variable_name>, <variable_name> <br>
FROM <table_name>;

* Для выбора всей таблицы используется символ \*

SELECT \* <br>
FROM <table_name>;

* Для исключения дубликатов выборки используется DISTINCT

SELECT DISTINCT <br>
FROM <table_name>;

* Сортировка по свойству через ORDER BY

SELECT \* <br>
FROM <table_name> <br>
ORDER BY \<name>;

* Сортировка по возрастанию ASC, DESC - по убыванию.

* Сортировка алфавиту ASC - с начала , DESC - с конца.

* Сортировка по свойству через WHERE. При выборке через \* выбираются все столбцы, даже, если сортировка ведется по одному столбцу. При этом столюец сортировки можно и не указывать в SELECT, но сортировкать по нему можно.

SELECT \* <br>
FROM <table_name> <br>
WHERE \<name> = "\<name>";

# Операторы сравнений

<> - не равно <br>
< - меньше <br>
\> - больше <br>
<= - меньше равно <br>
\>= - больше равно

Аналог сравнения - BETWEN<br>
\<column> BETWEN X AND Y; (X, Y - числа)

name <> "name"

# Сортировка строк

\<column> LIKE 'a%' - начинающаяся на a<br>
\<column> LIKE '%a' - заканчивающаяся на a<br>
\<column> LIKE '%' - любое кол-во символов<br>
\<column> LIKE '%a%' - содержит a<br>

# Операторы условий

AND - объединение условий<br>
OR - или<br>
NOT - отрицание условий<br>
\<column> IN (\<value>, \<value>) - аналог OR

# Результат выборки вывести можно, как какое-то значений (псевдоним)

SELECT \<name> AS \<nickname> <br>
FROM <table_name> <br>
WHERE \<name> = "\<name>";

# Агрегационные функции

SELECT MIN(\<column>)<br>
SELECT AVG(\<column>)<br>
SELECT MAX(\<column>)<br>
SELECT COUNT(\<column>) - кол-во элементов в столбце
COUNT (*) - кол-во элементов в таблице

# Фильтрация результата после группировки на основе HAVING

GROUP BY <\column><br>
HAVING  COUNT (*) > 1

HAVING - сортировка после группировка<br>
WHERE - сортировка перед группировкой

# Управление таблицами

INSERT INTO \<table> (\<column>, \<column>) VALUES (\<value>, \<value>)<br>
DELETE FROM \<table> (При отсутствии дальнейших условий сотрется вся таблица)<br>
UPDATE \<table> SET \<column> = "name"<br>
CREATE TABLE \<table> (\<column> тип столбца размерность, \<column> тип столбца размерность)<br>
DROP TABLE - удаление таблицы

# Тип данных 

VARCHAR, INTEGER, CHAR, FLOAT, REAL, BOOLEAN, NCHAR (юникод), NVARCHAR (многобайтовые символы), NUMERIC, BIT (1/0), DATE, DATETIME...

# Изменения существующей таблицы

ALTER TABLE \<table><br>
ADD \<column> тип данных - добавление столбца

ALTER TABLE \<table><br>
DROP \<column> - удаление столбца

ALTER TABLE \<table><br>
RENAME \<column_old> TO \<column_new> - переименование столбца

# Объединение таблиц

JOIN -позволяет объединить таблицы

SELECT \*<br>
FROM \<table_1><br>
JOIN \<table_2><br>
ON \<table_1>.\<column_1> = \<table_2>.\<column_2>; - свойство объединения на основе общего поля 

INNER JOIN = JOIN объединение на основе общих полей<br>
LEFT JOIN объединение с сохранением содержимого левой таблицы и общих полей<br>
RIGHT JOIN объединение с сохранением содержимого правой таблицы и общих полей<br>
SELF JOIN объединение таблицы саму с собой<br>
CROSS JOIN - декартово соединение (Все возможные комбинации. Каждый с каждым.)<br>
LEFT OUTER JOIN - соединение двух таблиц, в результате остается только левая, в которой не совпадают поля с правой<br>
RIGHT OUTER JOIN - соединение двух таблиц, в результате остается только правая, в которой не совпадают поля с левой<br>
FULL OUTER JOIN - полное объединение таблиц<br>

# Подзапросы

Используются, когда необходимо решить задачу, но не при помощи одного запроса. Подзапросов может быть много.

Склярные - вернут одно значение.<br>
Табличные возвращают таблицу

* Пример выбора цены меньше средней

SELECT \<name><br>
FROM \<table><br>
WHERE price < (SELECT AVG(pricr)<br> FROM \<table_2>)

* Принадлежит ли число поддиапазону

WHERE \<column> IN (SELECT \<name><br> FROM \<table>)

NOT IN - не принадлежит поддиапазону<br>
ANY/SOME - Для одного значения (вернут TRUE/FALSE)<br>
ALL - Для всех значений (вернут TRUE/FALSE)<br>

WHERE \<column> = ANY(SELECT \<name> <br> FROM \<table>)
