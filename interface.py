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
        connection = pymysql.connect(host='localhost',
                             user='grace',
                             password='Under the C1!',
                             database='new_surveys',
                             cursorclass=pymysql.cursors.DictCursor)
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
        connection = pymysql.connect(host='localhost',
                                   user='grace',
                                   password='Under the C1!',
                                   database='new_surveys',
                                   cursorclass=pymysql.cursors.DictCursor)
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
        connection = pymysql.connect(host='localhost',
                       user='grace',
                       password='Under the C1!',
                       database='new_surveys',
                       cursorclass=pymysql.cursors.DictCursor)
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
        #print(query)
        query2 = ""
        for y in range(0, question):
            new = "INSERT INTO question (label, ordinal, sname) VALUES ('" + str(qs[y]) + "'," + str(y+1)+ ", '" + str(id)+ "'); "
            #print(new)
            query2 += new
        final_query=query+query2
        #print(final_query)
        connection = pymysql.connect(host='localhost',
                       user='grace',
                       password='Under the C1!',
                       database='new_surveys',
                       cursorclass=pymysql.cursors.DictCursor)
        with connection.cursor() as cursor:
            sql=final_query
            cursor.execute(sql)
            rows = cursor.fetchall()
            print(rows)



    elif comm == 'show-cards':
        '''run-survey <name>

        This should simulate running the survey:

        - go through each user of the system
        - give each user the survey
        - for each user, determine if they've completed the survey or not
        - for each user determine to have completed the survey, generate answers for that user for every question in the survey
'''


    else:
        print('Unknown command')


if __name__ == '__main__':
    run()
