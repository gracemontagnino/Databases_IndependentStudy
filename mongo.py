import sys
import random
import requests
import pymysql.cursors
from pymongo import MongoClient
import datetime
_API_HOST = 'http://localhost:8080'

def run():
    connection = pymysql.connect(host='localhost',
                                 user='grace',
                                 password='Under the C1!',
                                 database='new_surveys',
                                 cursorclass=pymysql.cursors.DictCursor)
    quit = False
    while not quit:
        try:
            line = input('trellish> ')
            if line:
                inputs = line.strip().lower().split()
                command = inputs[0]
                if command == 'exit':
                    quit = True
                else:
                    process_command(command, inputs[1:])
        except EOFError:
            quit = True
            print()
        except Exception as e:
            print(f'ERROR - {e}')

def process_command(comm, args):

    if comm == 'surveys':
        name = input("Enter survey to translate:")
        with pymysql.connect(host='localhost',
                                   user='grace',
                                   password='Under the C1!',
                                   database='new_surveys',
                                   cursorclass=pymysql.cursors.DictCursor) as connection:
            with connection.cursor() as cursor:
                    sql="SELECT * FROM survey WHERE sname = '" + name + "'"
                    cursor.execute(sql)
                    rows = cursor.fetchall()

        col = my_db["surveys"]
        result = col.insert_many(rows)

        print("Checking it went through, by printing a query of it")
        myquery = { "sname": str(name) }
        mydoc = col.find(myquery)
        for x in mydoc:
          print(x)

    if comm == 'question':
        name = input("Enter survey to translate:")
        with pymysql.connect(host='localhost',
                                   user='grace',
                                   password='Under the C1!',
                                   database='new_surveys',
                                   cursorclass=pymysql.cursors.DictCursor) as connection:
            with connection.cursor() as cursor:
                    sql="SELECT * FROM question WHERE sname = '" + name + "'"
                    cursor.execute(sql)
                    rows = cursor.fetchall()

        col = my_db["question"]
        result = col.insert_many(rows)

        print("Checking it went through, by printing a query of it")
        myquery = { "sname": str(name) }
        mydoc = col.find(myquery)
        for x in mydoc:
          print(x)
    if comm == 'wasgiven':
        name = input("Enter survey to translate:")
        with pymysql.connect(host='localhost',
                                   user='grace',
                                   password='Under the C1!',
                                   database='new_surveys',
                                   cursorclass=pymysql.cursors.DictCursor) as connection:
            with connection.cursor() as cursor:
                    sql="SELECT * FROM wasGiven WHERE sname = '" + name + "'"
                    cursor.execute(sql)
                    rows = cursor.fetchall()

        col = my_db["wasGiven"]
        result = col.insert_many(rows)

        print("Checking it went through, by printing a query of it")
        myquery = { "sname": str(name) }
        mydoc = col.find(myquery)
        for x in mydoc:
          print(x)

    if comm == 'responded':
        with pymysql.connect(host='localhost',
                                   user='grace',
                                   password='Under the C1!',
                                   database='new_surveys',
                                   cursorclass=pymysql.cursors.DictCursor) as connection:
            with connection.cursor() as cursor:
                    sql="SELECT * FROM responded"
                    cursor.execute(sql)
                    rows = cursor.fetchall()

        col = my_db["responded"]
        result = col.insert_many(rows)

        print("Checking it went through, by printing a query of it")
        myquery = { "label": { "$regex": "^q" } }
        mydoc = col.find(myquery)
        for x in mydoc:
          print(x)

    if comm == 'userin':
        with pymysql.connect(host='localhost',
                                   user='grace',
                                   password='Under the C1!',
                                   database='new_surveys',
                                   cursorclass=pymysql.cursors.DictCursor) as connection:
            with connection.cursor() as cursor:
                    sql="SELECT * FROM userIn"
                    cursor.execute(sql)
                    rows = cursor.fetchall()

        col = my_db["userIn"]
        result = col.insert_many(rows)

        print("Checking it went through, by printing a query of it")
        myquery = { "unameFirst": { "$regex": "^A" }}
        mydoc = col.find(myquery)
        for x in mydoc:
          print(x)




if __name__ == '__main__':
    client = MongoClient()
    my_db = client["Mongo_Testing"]
    run()
