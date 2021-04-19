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
          number of surveys yet to complete

            with connection.cursor() as cursor:
                # Read a single record
                sql = "SELECT userID, COUNT(sname), COUNT(completed) FROM wasGiven
        GROUP BY userID;=%s"
                cursor.execute(sql, ('Kayla',))
                result = cursor.fetchone()
                print(result)'''


    elif comm == 'show-lists':
        '''user <id>

        Show information about user with ID <id>:

        Report:
          name
          ID
          surveys completed and for each such survey the user's response to all the survey questions
          surveys yet to complete'''


    elif comm == 'surveys':

        '''with connection.cursor() as cursor:
            # Read a single record
            sql = "SELECT sname, label, COUNT(completed) FROM wasGiven
    GROUP BY userID;=%s"
            cursor.execute(sql, ('Kayla',))
            result = cursor.fetchone()
            print(result)

        Show all surveys in the system

        For each survey, report:
          name
          list of questions
          number of users having completed this survey
          percentage of users having completed this survey
'''


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

    elif comm == 'create-survey':
        '''create-survey

        Lets you create a new survey. You'll probably want to query for the name of the survey, and for the questions to put in the survey'''



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
