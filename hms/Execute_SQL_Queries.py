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

    def execute_select_param(self, statement, param):
        self.cursor.execute(statement, [param])
        row = self.cursor.fetchone()
        result = row[0]
        return result


    def execute_insert(self, statement, param):
        self.cursor.execute(statement, param)
        return



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

    def get_visit_id(self, p_id):

        statement = get_visit_id

        try:
            result = self.execute(statement, p_id)
        except(Exception, pg2.DatabaseError):
            result = None
        return result

    def get_oper_id(self, name):
        statement = find_id_for_operate

        try:
            result = self.execute(statement, name)
        except(Exception, pg2.DatabaseError):
            result = None
        return result

    def get_med_id(self, name):
        statement = find_id_for_medicine

        try:
            result = self.execute(statement, name)
        except(Exception, pg2.DatabaseError):
            result = None
        return result

    def get_test_id(self, name):
        statement = find_id_for_test

        try:
            result = self.execute(statement, name)
        except(Exception, pg2.DatabaseError):
            result = None
        return result


    def register_opeartion(self, form):

        param = self.process_form(form)

        visit = self.get_visit_id(form[0])
        operation = self.get_oper_id(form[2])
        doctor = "I dont know"
        param[0] = doctor
        param[2] = operation
        param.insert(3, visit)

        INSERT_STATEMENT = insert_operation_procedure

        try:
            self.cursor.execute(INSERT_STATEMENT, param)
            result = "Insertion Successful"
        except (Exception, pg2.DatabaseError) as error:
            result = ("Error while inserting into PostgreSQL table", error)
        return result

    def register_prescription(self, form):

        param = self.process_form(form)

        visit = self.get_visit_id(form[0])
        medicine = self.get_med_id(form[2])
        doctor = "I dont know"
        param[0] = doctor
        param[2] = medicine
        param.insert(3, visit)

        INSERT_STATEMENT = insert_prescription_procedure

        try:
            self.cursor.execute(INSERT_STATEMENT, param)
            result = "Insertion Successful"
        except (Exception, pg2.DatabaseError) as error:
            result = ("Error while inserting into PostgreSQL table", error)
        return result

    def register_testing(self, form):

        param = self.process_form(form)

        visit = self.get_visit_id(form[0])
        test = self.get_test_id(form[2])
        doctor = "I dont know"
        param[0] = doctor
        param[2] = test
        param.insert(3, visit)

        INSERT_STATEMENT = insert_testing_procedure

        try:
            self.cursor.execute(INSERT_STATEMENT, param)
            result = "Insertion Successful"
        except (Exception, pg2.DatabaseError) as error:
            result = ("Error while inserting into PostgreSQL table", error)
        return result
