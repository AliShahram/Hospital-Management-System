from django.db import connection
import psycopg2 as pg2
from .SQL_Queries import *

class Tools:
    """ Tools used in the running queries and processing
        input of users"""

    def __init__(self):
        pass


    def process_form(self, form):
        result = []
        count = 0
        for key, value in form.items():
            if count != 0 and key != 'button':
                result.append(value)
            count += 1
        return result



class Database(Tools):
    """ Connection to the database and running
        sql queries """

    def __init__(self):
        self.cursor = connection.cursor()
        Tools.__init__(self)

    def execute(self, statement, param):
        self.cursor.execute(statement, [param])
        row = self.cursor.fetchone()
        result = row[0]
        return result


#-------------------------------------------------------
#Queries Execution
#-------------------------------------------------------

    def ident_employee_type(self, e_id):
        SELECT_STATEMENT = ident_employee_type
        try:
            result = self.execute(SELECT_STATEMENT, e_id)
        except (Exception, pg2.DatabaseError) as error:
            result = ("Error: ", error)
        return result


    def register_new_doctor(self, form):
        param = self.process_form(form)
        INSERT_STATEMENT = register_new_doctor

        try:
            self.cursor.execute(INSERT_STATEMENT, param)
            result = "Insertion Successful"
        except (Exception, pg2.DatabaseError) as error:
            result = ("Error while inserting into PostgreSQL table", error)
        return result
