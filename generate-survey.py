#
# Generate survey, questions, and responses for a given set of user IDs
#
# For instance, generate a survey named 'test survey' with three questions (question A, question B, question C),
# created on 2021-01-01, and generate responses at random for users with ID between 1000 and 1009 (inclusive)
#
# Databases_IndependentStudy (main)*$ python3 generate-survey.py 'test survey' 'question A;question B;question C' 2021-01-01 1000 1009
# INSERT INTO survey (sName, created) VALUES ('test survey', '2021-01-01 00:00:00')
# INSERT INTO question (label, ordinal) VALUES ('question A', 1)
# INSERT INTO hasquestion (sname, label) VALUES ('test survey', 'question A')
# INSERT INTO question (label, ordinal) VALUES ('question B', 2)
# INSERT INTO hasquestion (sname, label) VALUES ('test survey', 'question B')
# INSERT INTO question (label, ordinal) VALUES ('question C', 3)
# INSERT INTO hasquestion (sname, label) VALUES ('test survey', 'question C')
# INSERT INTO wasgiven (userId, sName, completed) VALUES (1000, 'test survey', '2021-01-08 06:06:52')
# INSERT INTO responded (userId, label, scale_val_user_in) VALUES (1000, 'question A', 5)
# INSERT INTO responded (userId, label, scale_val_user_in) VALUES (1000, 'question B', 3)
# INSERT INTO responded (userId, label, scale_val_user_in) VALUES (1000, 'question C', 1)
# INSERT INTO wasgiven (userId, sName, completed) VALUES (1001, 'test survey', '2021-01-08 23:52:23')
# INSERT INTO responded (userId, label, scale_val_user_in) VALUES (1001, 'question A', 4)
# INSERT INTO responded (userId, label, scale_val_user_in) VALUES (1001, 'question B', 1)
# INSERT INTO responded (userId, label, scale_val_user_in) VALUES (1001, 'question C', 3)
# INSERT INTO wasgiven (userId, sName, completed) VALUES (1002, 'test survey', '2021-01-09 09:22:08')
# INSERT INTO responded (userId, label, scale_val_user_in) VALUES (1002, 'question A', 1)
# INSERT INTO responded (userId, label, scale_val_user_in) VALUES (1002, 'question B', 2)
# INSERT INTO responded (userId, label, scale_val_user_in) VALUES (1002, 'question C', 5)
# INSERT INTO wasgiven (userId, sName, completed) VALUES (1003, 'test survey', NULL)
# INSERT INTO wasgiven (userId, sName, completed) VALUES (1004, 'test survey', '2021-01-02 15:55:22')
# INSERT INTO responded (userId, label, scale_val_user_in) VALUES (1004, 'question A', 2)
# INSERT INTO responded (userId, label, scale_val_user_in) VALUES (1004, 'question B', 4)
# INSERT INTO responded (userId, label, scale_val_user_in) VALUES (1004, 'question C', 1)
# INSERT INTO wasgiven (userId, sName, completed) VALUES (1005, 'test survey', '2021-01-07 12:33:36')
# INSERT INTO responded (userId, label, scale_val_user_in) VALUES (1005, 'question A', 3)
# INSERT INTO responded (userId, label, scale_val_user_in) VALUES (1005, 'question B', 1)
# INSERT INTO responded (userId, label, scale_val_user_in) VALUES (1005, 'question C', 4)
# INSERT INTO wasgiven (userId, sName, completed) VALUES (1006, 'test survey', '2021-01-09 20:13:21')
# INSERT INTO responded (userId, label, scale_val_user_in) VALUES (1006, 'question A', 2)
# INSERT INTO responded (userId, label, scale_val_user_in) VALUES (1006, 'question B', 3)
# INSERT INTO responded (userId, label, scale_val_user_in) VALUES (1006, 'question C', 3)
# INSERT INTO wasgiven (userId, sName, completed) VALUES (1007, 'test survey', '2021-01-05 12:25:44')
# INSERT INTO responded (userId, label, scale_val_user_in) VALUES (1007, 'question A', 1)
# INSERT INTO responded (userId, label, scale_val_user_in) VALUES (1007, 'question B', 2)
# INSERT INTO responded (userId, label, scale_val_user_in) VALUES (1007, 'question C', 1)
# INSERT INTO wasgiven (userId, sName, completed) VALUES (1008, 'test survey', '2021-01-09 10:28:02')
# INSERT INTO responded (userId, label, scale_val_user_in) VALUES (1008, 'question A', 5)
# INSERT INTO responded (userId, label, scale_val_user_in) VALUES (1008, 'question B', 5)
# INSERT INTO responded (userId, label, scale_val_user_in) VALUES (1008, 'question C', 3)
# INSERT INTO wasgiven (userId, sName, completed) VALUES (1009, 'test survey', NULL)
#

import sys
import datetime
import random

TIMESTAMP_FORMAT = '%Y-%m-%d %H:%M:%S'

def gen_survey(sname, questions, date, usersStart, usersEnd):
    '''
    Create a new survey with associated questions
    and insert responses for all users with IDs in `users`
    '''
    print(f"INSERT INTO survey (sName, created) VALUES ('{sname}', '{date.strftime(TIMESTAMP_FORMAT)}')")
    for (i, q) in enumerate(questions):
        print(f"INSERT INTO question (label, ordinal) VALUES ('{q}', {i + 1})")
        print(f"INSERT INTO hasquestion (sname, label) VALUES ('{sname}', '{q}')")

    for userId in range(usersStart, usersEnd + 1):
        # 70% chance of completion
        if random.randint(1, 10) < 8:
            time_spent = datetime.timedelta(days=random.randint(0, 10), seconds=random.randint(0, 3600 * 24))
            completed = date + time_spent
            print(f"INSERT INTO wasgiven (userId, sName, completed) VALUES ({userId}, '{sname}', '{completed.strftime(TIMESTAMP_FORMAT)}')")
            skew = random.randint(-1, 2)
            for q in questions:
                # random choice of 1-5, adjusted for skew (which favors positives), constrained between 1 and 5
                feedback = max(min(random.randint(1, 5) + skew, 5), 1)
                print(f"INSERT INTO responded (userId, label, scale_val_user_in) VALUES ({userId}, '{q}', {feedback})")
        else:
            print(f"INSERT INTO wasgiven (userId, sName, completed) VALUES ({userId}, '{sname}', NULL)")
            
    
if __name__ == '__main__':
    if len(sys.argv) > 5:
        gen_survey(sys.argv[1], sys.argv[2].split(';'), datetime.datetime.strptime(sys.argv[3], '%Y-%m-%d'), int(sys.argv[4]), int(sys.argv[5]))
    else:
        print("USAGE: generate-survey <name> <questions separated by ;> <date created> <userId start> <userId end>")
        
