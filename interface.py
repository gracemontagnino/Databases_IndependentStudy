import sys
import datetime
import random
import requests
import pymysql.cursors
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

    if comm == 'users':
        '''Show all users in the system

        For each user, report:
          name
          ID
          number of surveys completed
          number of surveys yet to complete'''
        with pymysql.connect(host='localhost',
                                   user='grace',
                                   password='Under the C1!',
                                   database='new_surveys',
                                   cursorclass=pymysql.cursors.DictCursor) as connection:
            with connection.cursor() as cursor:
                sql="SELECT userID, COUNT(sname), COUNT(completed) FROM wasGiven GROUP BY userID"
                cursor.execute(sql)
                rows = cursor.fetchall()
                print(rows)


    elif comm == 'show-lists':
        '''user <id>

        Show information about user with ID <id>:

        Report:
          name
          ID
          surveys completed and for each such survey the user's response to all the survey questions
          surveys yet to complete'''
        id = input("Enter user ID:")
        with pymysql.connect(host='localhost',
                             user='grace',
                             password='Under the C1!',
                             database='new_surveys',
                             cursorclass=pymysql.cursors.DictCursor) as connection:
            with connection.cursor() as cursor:
                sql="SELECT question.sname, userIn.userID, responded.label, userIn.unameFirst, responded.scaleValUserIn FROM userIn INNER JOIN responded ON userIn.userID=responded.userID INNER JOIN question on responded.label=question.label WHERE userIn.userID = %s GROUP BY label, scaleValUserIn, unameFirst, sname"
                cursor.execute(sql, (id))
                rows = cursor.fetchall()
                print(rows)


    elif comm == 'surveys':

        '''
        Show all surveys in the system

        For each survey, report:
          name
          list of questions
          number of users having completed this survey
          percentage of users having completed this survey
'''
        with pymysql.connect(host='localhost',
                                   user='grace',
                                   password='Under the C1!',
                                   database='new_surveys',
                                   cursorclass=pymysql.cursors.DictCursor) as connection:
            with connection.cursor() as cursor:
                sql="SELECT q.sname, r.label, COUNT(r.scaleValUserIn) FROM responded as r INNER JOIN question as q on r.label=q.label GROUP BY label, sname;"
                cursor.execute(sql)
                rows = cursor.fetchall()
                print(rows)


    elif comm == 'show-list':
        '''survey <name>

        Show info + statistics about survey with name <name>

        Report:
          name
          list of questions
          - for each question, counts of each answer, and average answer
          number of users having completed the survey
          percentage of users having completed the survey
          average completion time of the survey'''
        id = input("Enter survey name:")
        with pymysql.connect(host='localhost',
                       user='grace',
                       password='Under the C1!',
                       database='new_surveys',
                       cursorclass=pymysql.cursors.DictCursor) as connection:
            with connection.cursor() as cursor:
                sql='''SELECT DATEDIFF(w.completed, s.created), q.sname, r.label, COUNT(r.scaleValUserIn), AVG(r.scaleValUserIn)
                FROM responded AS r
                INNER JOIN question as q ON r.label=q.label
                INNER JOIN survey as s ON q.sname=s.sname
                LEFT JOIN wasGiven as w ON s.sname=w.sname
                WHERE q.sname = %s
                GROUP BY sname, label, DATEDIFF(w.completed, s.created)'''
                cursor.execute(sql, (id,))
                rows = cursor.fetchall()
                print(rows)

    elif comm == 'create-survey':
        '''create-survey
        Lets you create a new survey. You'll probably want to query for the name of the survey, and for the questions to put in the survey'''
        id = input("Enter survey name: ")
        question = int(input("Enter number of questions in survey: "))
        qs=[]
        for x in range(0, question):
            qs.append(input("Enter question: "))
        query = "INSERT INTO survey (sname, created) VALUES ('" + str(id) + "', '2021-01-01 00:00:00'); "
        query2 = []
        for y in range(0, question):
            new = "INSERT INTO question (label, ordinal, sname) VALUES ('" + str(qs[y]) + "'," + str(y+1)+ ", '" + str(id)+ "'); "
            query2.append(new)

        with pymysql.connect(host='localhost',
                       user='grace',
                       password='Under the C1!',
                       database='new_surveys',
                       cursorclass=pymysql.cursors.DictCursor) as connection:
            with connection.cursor() as cursor:
                cursor.execute(query)
                for i in range(0,question):
                    cursor.execute(query2[i])
                #rows = cursor.fetchall()
                #print(rows)



    elif comm == 'show-cards':
        '''run-survey <name>

        This should simulate running the survey:

        - go through each user of the system
        - give each user the survey
        - for each user, determine if they've completed the survey or not
        - for each user determine to have completed the survey, generate answers for that user for every question in the survey
'''
        sname = input("Enter survey name:")
        with pymysql.connect(host='localhost',
                       user='grace',
                       password='Under the C1!',
                       database='new_surveys',
                       cursorclass=pymysql.cursors.DictCursor) as connection:

            with connection.cursor() as cursor:
                users = []
                users_ugly=[]
                queries=[]
                questions=[]
                sql= "SELECT userID FROM userIn"
                cursor.execute(sql)
                users_ugly = cursor.fetchall()
                sql2= "SELECT label FROM question WHERE sname = '" + str(sname) +"'"
                cursor.execute(sql2)
                questions = cursor.fetchall()
                for dicts in users_ugly:
                    for key in dicts:
                        users.append((int(dicts[key])))
                TIMESTAMP_FORMAT = '%Y-%m-%d %H:%M:%S'
                for userID in users:
                    if random.randint(1, 10) < 8:
                        queries.append((f"INSERT INTO wasGiven (userID, sname, completed) VALUES ({userID}, '{sname}', '2021-02-01 00:00:00');"))
                        skew = random.randint(-1, 2)
                        for q in questions:
                            feedback = max(min(random.randint(1, 5) + skew, 5), 1)
                            queries.append((f"INSERT INTO responded (userID, label, scaleValUserIn) VALUES ({userID}, '{q}', {feedback});"))
                    else:
                        queries.append((f"INSERT INTO wasGiven (userID, sname, completed) VALUES ({userID}, '{sname}', NULL);"))

                for i in range(0,len(queries)):
                        cursor.execute(queries[i])

        
if __name__ == '__main__':
    run()
