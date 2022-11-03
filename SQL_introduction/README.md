
# SQL - Introduction

-   Novice
-   By:  Guillaume
-   Weight:  1
-   Your score will be updated as you progress.

### Concepts

_For this project, we expect you to look at this concept:_

-   [Databases](https://intranet.hbtn.io/concepts/864)

![](https://s3.amazonaws.com/intranet-projects-files/holbertonschool-higher-level_programming+/272/rtcwz.jpg)

## Resources

**Read or watch**:

-   [What is Database & SQL?](https://intranet.hbtn.io/rltoken/jRAhwW4u4YvZtLtMGU2_6g "What is Database & SQL?")
-   [A Basic MySQL Tutorial](https://intranet.hbtn.io/rltoken/m_0RMf4RcC5NrHyjY1xN3w "A Basic MySQL Tutorial")
-   [Basic SQL statements: DDL and DML](https://intranet.hbtn.io/rltoken/-Qrnbp5eKmo7ajPDZekjfg "Basic SQL statements: DDL and DML")  (_no need to read the chapter “Privileges”_)
-   [Basic queries: SQL and RA](https://intranet.hbtn.io/rltoken/wXN5s1qexSTMh--NkTF1_w "Basic queries: SQL and RA")
-   [SQL technique: functions](https://intranet.hbtn.io/rltoken/7khGjnehvjHnqNZ9yizggg "SQL technique: functions")
-   [SQL technique: subqueries](https://intranet.hbtn.io/rltoken/xnJcopQTZyUke3LdAkOwow "SQL technique: subqueries")
-   [What makes the big difference between a backtick and an apostrophe?](https://intranet.hbtn.io/rltoken/QEr3XcBPhIR-E8NSSn1nzg "What makes the big difference between a backtick and an apostrophe?")
-   [MySQL Cheat Sheet](https://intranet.hbtn.io/rltoken/mNcGgvhZNG0dbFe23E-EjA "MySQL Cheat Sheet")
-   [MySQL 8.0 SQL Statement Syntax](https://intranet.hbtn.io/rltoken/ePNUeloWxfiXwec7HeKe7Q "MySQL 8.0 SQL Statement Syntax")

## Learning Objectives

At the end of this project, you are expected to be able to  [explain to anyone](https://intranet.hbtn.io/rltoken/6bUOgrGi5Yd_I65Jp9bAfg "explain to anyone"),  **without the help of Google**:

### General

-   What’s a database
-   What’s a relational database
-   What does SQL stand for
-   What’s MySQL
-   How to create a database in MySQL
-   What does  `DDL`  and  `DML`  stand for
-   How to  `CREATE`  or  `ALTER`  a table
-   How to  `SELECT`  data from a table
-   How to  `INSERT`,  `UPDATE`  or  `DELETE`  data
-   What are  `subqueries`
-   How to use MySQL functions

## Requirements

### General

-   Allowed editors:  `vi`,  `vim`,  `emacs`
-   All your files will be executed on Ubuntu 20.04 LTS using  `MySQL 8.0`  (version 8.0.25)
-   All your files should end with a new line
-   All your SQL queries should have a comment just before (i.e. syntax above)
-   All your files should start by a comment describing the task
-   All SQL keywords should be in uppercase (`SELECT`,  `WHERE`…)
-   A  `README.md`  file, at the root of the folder of the project, is mandatory
-   The length of your files will be tested using  `wc`

## More Info

### Comments for your SQL file:

```
$ cat my_script.sql
-- 3 first students in the Batch ID=3
-- because Batch 3 is the best!
SELECT id, name FROM students WHERE batch_id = 3 ORDER BY created_at DESC LIMIT 3;
$

```

### Install MySQL 8.0 on Ubuntu 20.04 LTS

```
$ sudo apt update
$ sudo apt install mysql-server
...
$ mysql --version
mysql  Ver 8.0.25-0ubuntu0.20.04.1 for Linux on x86_64 ((Ubuntu))
$

```

Connect to your MySQL server:

```
$ sudo mysql
Welcome to the MySQL monitor.  Commands end with ; or \g.
Your MySQL connection id is 11
Server version: 8.0.25-0ubuntu0.20.04.1 (Ubuntu)

Copyright (c) 2000, 2021, Oracle and/or its affiliates.

Oracle is a registered trademark of Oracle Corporation and/or its
affiliates. Other names may be trademarks of their respective
owners.

Type 'help;' or '\h' for help. Type '\c' to clear the current input statement.

mysql>
mysql> quit
Bye
$

```

### Use the sandbox to run MySQL

**In the container, credentials are  `root/root`**

-   Ask for container  `Ubuntu 20.04`
-   Connect via SSH
-   OR connect via the Web terminal
-   In the container, you should start MySQL before playing with it:

```
$ service mysql start                                                   
 * Starting MySQL database server mysqld 
$
$ cat 0-list_databases.sql | mysql -uroot -p                               
Database                                                                                   
information_schema                                                                         
mysql                                                                                      
performance_schema                                                                         
sys                      
$
```



## Tasks

### 0. List databases

mandatory

Write a script that lists all databases of your MySQL server.


### 1. Create a database

mandatory

Write a script that creates the database  `hbtn_0c_0`  in your MySQL server.

-   If the database  `hbtn_0c_0`  already exists, your script should not fail
-   You are not allowed to use the  `SELECT`  or  `SHOW`  statements


### 2. Delete a database

mandatory

Write a script that deletes the database  `hbtn_0c_0`  in your MySQL server.

-   If the database  `hbtn_0c_0`  doesn’t exist, your script should not fail
-   You are not allowed to use the  `SELECT`  or  `SHOW`  statements

### 3. List tables

mandatory

Write a script that lists all the tables of a database in your MySQL server.

-   The database name will be passed as argument of  `mysql`  command (in the following example:  `mysql`  is the name of the database)

### 4. First table

mandatory

Write a script that creates a table called  `first_table`  in the current database in your MySQL server.

-   `first_table`  description:
    -   `id`  INT
    -   `name`  VARCHAR(256)
-   The database name will be passed as an argument of the  `mysql`  command
-   If the table  `first_table`  already exists, your script should not fail
-   You are not allowed to use the  `SELECT`  or  `SHOW`  statements


### 5. Full description

mandatory

Write a script that prints the full description of the table  `first_table`  from the database  `hbtn_0c_0`  in your MySQL server.

-   The database name will be passed as an argument of the  `mysql`  command
-   You are not allowed to use the  `DESCRIBE`  or  `EXPLAIN`  statements


### 6. List all in table

mandatory

Write a script that lists all rows of the table  `first_table`  from the database  `hbtn_0c_0`  in your MySQL server.

-   All fields should be printed
-   The database name will be passed as an argument of the  `mysql`  command


### 7. First add

mandatory

Write a script that inserts a new row in the table  `first_table`  (database  `hbtn_0c_0`) in your MySQL server.

-   New row:
    -   `id`  =  `89`
    -   `name`  =  `Best School`
-   The database name will be passed as an argument of the  `mysql`  command

### 8. Count 89

mandatory

Write a script that displays the number of records with  `id = 89`  in the table  `first_table`  of the database  `hbtn_0c_0`  in your MySQL server.

-   The database name will be passed as an argument of the  `mysql`  command

### 9. Full creation

mandatory

Write a script that creates a table  `second_table`  in the database  `hbtn_0c_0`  in your MySQL server and add multiples rows.

-   `second_table`  description:
    -   `id`  INT
    -   `name`  VARCHAR(256)
    -   `score`  INT
-   The database name will be passed as an argument to the  `mysql`  command
-   If the table  `second_table`  already exists, your script should not fail
-   You are not allowed to use the  `SELECT`  and  `SHOW`  statements
-   Your script should create these records:
    -   `id`  = 1,  `name`  = “John”,  `score`  = 10
    -   `id`  = 2,  `name`  = “Alex”,  `score`  = 3
    -   `id`  = 3,  `name`  = “Bob”,  `score`  = 14
    -   `id`  = 4,  `name`  = “George”,  `score`  = 8


### 10. List by best

mandatory

Write a script that lists all records of the table  `second_table`  of the database  `hbtn_0c_0`  in your MySQL server.

-   Results should display both the score and the name (in this order)
-   Records should be ordered by score (top first)
-   The database name will be passed as an argument of the  `mysql`  command

### 11. Select the best

mandatory

Write a script that lists all records with a  `score >= 10`  in the table  `second_table`  of the database  `hbtn_0c_0`  in your MySQL server.

-   Results should display both the score and the name (in this order)
-   Records should be ordered by score (top first)

### 12. Cheating is bad

mandatory

Write a script that updates the score of Bob to  `10`  in the table  `second_table`.

-   You are not allowed to use Bob’s id value, only the  `name`  field
-   The database name will be passed as an argument of the  `mysql`  command

### 13. Score too low

mandatory

Write a script that removes all records with a  `score <= 5`  in the table  `second_table`  of the database  `hbtn_0c_0`  in your MySQL server.

-   The database name will be passed as an argument of the  `mysql`  command

### 14. Average

mandatory

Write a script that computes the score average of all records in the table  `second_table`  of the database  `hbtn_0c_0`  in your MySQL server.

-   The result column name should be  `average`
-   The database name will be passed as an argument of the  `mysql`  command

### 15. Number by score

mandatory

Write a script that lists the number of records with the same score in the table  `second_table`  of the database  `hbtn_0c_0`  in your MySQL server.

-   The result should display:
    -   the  `score`
    -   the number of records for this  `score`  with the label  `number`
-   The list should be sorted by the number of records (descending)
-   The database name will be passed as an argument to the  `mysql`  command

### 16. Say my name

mandatory

Write a script that lists all records of the table  `second_table`  of the database  `hbtn_0c_0`  in your MySQL server.

-   Don’t list rows without a  `name`  value
-   Results should display the score and the name (in this order)
-   Records should be listed by descending score
-   The database name will be passed as an argument to the  `mysql`  command

In this example, new data have been added to the table  `second_table`.