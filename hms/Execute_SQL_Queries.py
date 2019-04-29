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
        result = list(map(lambda s: s.strip(), result))
        return result



class Database(Tools):
    """ Connection to the database and running
        sql queries """

    def __init__(self):
        self.cursor = connection.cursor()
        Tools.__init__(self)


    def execute(self, statement):
        self.cursor.execute(statement)
        row = self.cursor.fetchone()
        result = row[0]
        return result


    def execute_select_param(self, statement, param):
        if len(param)==1:
            param = [param]
        else:
            param = list(param)

        self.cursor.execute(statement, param)
        row = self.cursor.fetchone()
        return row


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

    def register_patient(self, form):
        param = self.process_form(form)
        INSERT_STATEMENT = register_patient
        p_id = param[0]
        try:
            self.cursor.execute(INSERT_STATEMENT, param)
            result = "Insertion Successful. Patient ID is " + p_id
        except (Exception, pg2.DatabaseError) as error:
            result = ("Error while inserting into PostgreSQL table", error)
        return result


    def get_patient_info(self, form):
        param = self.process_form(form)
        p_id = param[0]

        SELECT_STATEMENT = get_patient_info
        try:
            result = self.execute_select_param(SELECT_STATEMENT, p_id)
            if result == None:
                message = "No such patient exists"
            else:
                message = "Success: patient information retrieved"

        except (Exception, pg2.DatabaseError) as error:
            result = None
            message = ('Failure:', error)
        return result, message


    def update_patient_info(self,form):
        param = self.process_form(form)
        p_id = param.pop(0)
        param.pop()
        param.append(p_id)
        INSERT_STATEMENT = update_patient_info

        try:
            self.cursor.execute(INSERT_STATEMENT, param)
            result = "Update Successful"
        except (Exception, pg2.DatabaseError) as error:
            result = ("Error while updating  PostgreSQL table", error)
        return result

    def delete_patient(self,form):
        param = self.process_form(form)
        INSERT_STATEMENT = delete_patient
        p_id = param[0]
        try:
            self.cursor.execute(INSERT_STATEMENT, p_id)
            result = "Delete Successful"
        except (Exception, pg2.DatabaseError) as error:
            result = ("Error while deleting from PostgreSQL table", error)
        return result

    def create_visit(self, form):
        param = self.process_form(form)
        INSERT_STATEMENT = create_visit
        v_id = param[0]
        try:
            self.cursor.execute(INSERT_STATEMENT, param)
            result = "Insertion Successful. Visit id is " + v_id
        except (Exception, pg2.DatabaseError) as error:
            result = ("Error while inserting into PostgreSQL table", error)
        return result

    def get_visit_info(self, form):
        param = self.process_form(form)
        v_id = param[0]
        SELECT_STATEMENT = get_visit_info
        try:
            result = self.execute_select_param(SELECT_STATEMENT, v_id)
            if result == None:
                message = "No such patient exists"
            else:
                message = "Success: patient information retrieved"

        except (Exception, pg2.DatabaseError) as error:
            result = None
            message = ('Failure:', error)
        return result, message

    def update_visit_info(self, form):
        param = self.process_form(form)
        v_id = param.pop(0)
        param.pop()
        param.append(v_id)
        INSERT_STATEMENT = update_visit_info
        try:
            self.cursor.execute(INSERT_STATEMENT, param)
            result = "Update Successful"
        except (Exception, pg2.DatabaseError) as error:
            result = ("Error while updating  PostgreSQL table", error)
            print(error)
        return result

    def delete_visit(self, form):
        param = self.process_form(form)
        INSERT_STATEMENT = delete_visit
        v_id = param[0]
        try:
            self.cursor.execute(INSERT_STATEMENT, v_id)
            result = "Delete Successful"
        except (Exception, pg2.DatabaseError) as error:
            result = ("Error while deleting from PostgreSQL table", error)
        return result


    def create_admission(self, form):
        param = self.process_form(form)
        INSERT_STATEMENT = create_admission
        ad_id = param[0]
        try:
            self.cursor.execute(INSERT_STATEMENT, param)
            result = "Insertion Successful. Admission ID is " + ad_id
        except (Exception, pg2.DatabaseError) as error:
            result = ("Error while inserting into PostgreSQL table", error)
        return result

    def get_admission_info(self, form):
        param = self.process_form(form)
        SELECT_STATEMENT = get_admission_info
        try:
            result = self.execute_select_param(SELECT_STATEMENT, param)
            if result == None:
                message = "No such patient exists"
            else:
                message = "Success: patient information retrieved"

        except (Exception, pg2.DatabaseError) as error:
            result = None
            message = ('Failure:', error)
        return result, message

    def update_admission_info(self, form):
        param = self.process_form(form)
        ad_id = param.pop(0)
        param.pop() #debug why?
        param.append(ad_id)
        INSERT_STATEMENT = update_admission_info
        try:
            self.cursor.execute(INSERT_STATEMENT, param)
            result = "Update Successful"
        except (Exception, pg2.DatabaseError) as error:
            result = ("Error while updating  PostgreSQL table", error)
        return result

    def delete_admission(self, form):
        param = self.process_form(form)
        INSERT_STATEMENT = delete_admission
        ad_id = param[0]
        try:
            self.cursor.execute(INSERT_STATEMENT, ad_id)
            result = "Delete Successful"
        except (Exception, pg2.DatabaseError) as error:
            result = ("Error while deleting from PostgreSQL table", error)
        return result

    def create_appointment(self, form):
        param = self.process_form(form)
        INSERT_STATEMENT = create_appointment
        try:
            self.cursor.execute(INSERT_STATEMENT, param)
            result = "Insertion Successful"
        except (Exception, pg2.DatabaseError) as error:
            result = ("Error while inserting into PostgreSQL table", error)
        return result

    def get_appointment_info(self, form):
        param = self.process_form(form)
        SELECT_STATEMENT = get_appointment_info
        print(param)
        try:
            result = self.execute_select_param(SELECT_STATEMENT, param)
            if result == None:
                message = "No such patient exists"
            else:
                message = "Success: appointment information retrieved"
        except (Exception, pg2.DatabaseError) as error:
            result = None
            message = ('Failure:', error)
        return result, message

    def update_appointment_info(self, form):
        param = self.process_form(form)
        param.pop()
        print(param)
        print(type(param))
        pk = list(param[0]) + param[3:5]
        param = param + pk #slightly less efficient than a for loop, ask ajit if this is a problem
        INSERT_STATEMENT = update_appointment_info
        try:
            self.cursor.execute(INSERT_STATEMENT, param)
            result = "Update Successful"
        except (Exception, pg2.DatabaseError) as error:
            result = ("Error while updating  PostgreSQL table", error)
        print(param)
        print(result)
        return result

    def delete_appointment(self, form):
        param = self.process_form(form)
        param.pop()
        pk = param[2:5]
        INSERT_STATEMENT = delete_appointment
        try:
            self.cursor.execute(INSERT_STATEMENT, pk)
            result = "Delete Successful"
        except (Exception, pg2.DatabaseError) as error:
            result = ("Error while deleting from PostgreSQL table", error)
        return result

    def create_consultation(self, form):
        param = self.process_form(form)
        INSERT_STATEMENT = create_consultation
        try:
            self.cursor.execute(INSERT_STATEMENT, param)
            result = "Insertion Successful"
        except (Exception, pg2.DatabaseError) as error:
            result = ("Error while inserting into PostgreSQL table", error)
        return result

    def get_consultation_info(self, form):
        param = self.process_form(form)

        SELECT_STATEMENT = get_consultation_info
        try:
            result = self.execute_select_param(SELECT_STATEMENT, param)
            if result == None:
                message = "No such consultation exists"
            else:
                message = "Success: consultaiton information retrieved"

        except (Exception, pg2.DatabaseError) as error:
            result = None
            message = ('Failure:', error)
        return result, message

    def update_consultation_info(self, form):
        param = self.process_form(form)
        param.pop()
        pk = [param[0]] + param[2:4]
        param = param + pk
        INSERT_STATEMENT = update_consultation_info
        try:
            self.cursor.execute(INSERT_STATEMENT, param)
            result = "Update Successful"
        except (Exception, pg2.DatabaseError) as error:
            result = ("Error while updating  PostgreSQL table", error)
        return result
