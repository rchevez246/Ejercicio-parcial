# DB

import pymysql.cursors
def createconnectionDB():
    connection = pymysql.connect(
        host='localhost',
        user='root', # mi usuario es root
        password='240601', # contra es 240601
        database='email_db', # nombre de la bd
        port=3306,
        cursorclass=pymysql.cursors.DictCursor,
    )
    return connection

## Insert method
def insertNewPerson(person):
    connection = createconnectionDB()
    with connection:
        with connection.cursor() as cursor:
            sql = "INSERT INTO `email_db`.`email-address` (`ID`,`name`,`email`)VALUES (%s, %s, %s);"
            cursor.execute(sql, (0, person.name, person.email))
        connection.commit()
        
