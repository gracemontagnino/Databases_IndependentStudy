import pymysql.cursors

# Connect to the database
connection = pymysql.connect(host='localhost',
                             user='grace',
                             password='Under the C1!',
                             database='new_surveys',
                             cursorclass=pymysql.cursors.DictCursor)

with connection:
    '''with connection.cursor() as cursor:
        # Create a new record
        sql = "INSERT INTO `users` (`email`, `password`) VALUES (%s, %s)"
        cursor.execute(sql, ('webmaster@python.org', 'very-secret'))

    # connection is not autocommit by default. So you must commit to save
    # your changes.
    connection.commit()'''

    with connection.cursor() as cursor:
        # Read a single record
        #sql = "SELECT `userID` FROM `userIn` WHERE `unameFirst`=%s"
        #sql = "SELECT `userID`, `COUNT(sname)`, `COUNT(completed)` FROM `wasGiven` GROUP BY `userID`"
        sql="SELECT `userIn.unameFirst`, `responded.scaleValUserIn` FROM `userIn` INNER JOIN `responded` ON `userIn.userID`=`responded.userID` WHERE `unameFirst` = `Kayla` GROUP BY `label`"

        #cursor.execute(sql, ('Kayla',))
        cursor.execute(sql)
        result = cursor.fetchone()
        print(result)
