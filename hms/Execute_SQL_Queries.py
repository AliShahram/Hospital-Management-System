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


    def execute(self, statement):
        self.cursor.execute(statement)
        row = self.cursor.fetchone()
        result = row[0]
        return result


    def execute_select_param(self, statement, param):
        self.cursor.execute(statement, [param])
        row = self.cursor.fetchone()
        return row


    def execute_insert(self, statement, param):
        self.cursor.execute(statement, param)
        return


#-------------------------------------------------------
#Queries Execution
#-------------------------------------------------------

    def validate_employee(self, e_id):
        SELECT_STATEMENT = validate_employee
        status = self.execute_select_param(SELECT_STATEMENT, e_id)

        if status == 1:
            return True
        else:
            return False



    def ident_employee_type(self, e_id):
        SELECT_STATEMENT = ident_employee_type
        try:
            result = self.execute_select_param(SELECT_STATEMENT, e_id)
            result = result[0]
        except (Exception, pg2.DatabaseError) as error:
            result = ("Error: ", error)
        return result


    def get_recent_emp_id(self):
        """return most recent employee ID"""

        SELECT_STATEMENT = get_recent_emp_id
        try:
            result = self.execute(SELECT_STATEMENT)
        except (Exception, pg2.DatabaseError):
            result = None
        return result


    def register_new_employee(self, type):
        """Registers new employee"""

        INSERT_EMPLOYEE = register_new_employee
        try:
            self.execute_insert(INSERT_EMPLOYEE, [type])
            return True
        except (Exception, pg2.DatabaseError) as er:
            return er


    def register_new_doctor(self, form):
        success = self.register_new_employee('d')
        if success == True:
            id = self.get_recent_emp_id()
            param = self.process_form(form)
            param.insert(0, id)

            INSERT_DOCTOR = register_new_doctor

            try:
                self.execute_insert(INSERT_DOCTOR, param)
                result = "Insertion Successful"
            except (Exception, pg2.DatabaseError) as error:
                result = ("Error while inserting Doctor: ", error)

        else:
            result = ("Error while inserting employee", success)
        return result



    def register_new_recep(self, form):
        success = self.register_new_employee('r')
        if success == True:
            id = self.get_recent_emp_id()
            param = self.process_form(form)
            param.insert(0, id)

            INSERT_RECEP = register_new_recep

            try:
                self.execute_insert(INSERT_RECEP, param)
                result = "Insertion Successful"
            except (Exception, pg2.DatabaseError) as error:
                result = ("Error while inserting Receptionist: ", error)

        else:
            result = ("Error while inserting employee table", success)
        return result




    def get_employee_info(self, form):
        param = self.process_form(form)
        e_id = param[0]
        emp_type = self.ident_employee_type(e_id)

        if emp_type == 'd':
            SELECT_STATEMENT = get_doctor_info
        elif emp_type == 'r':
            SELECT_STATEMENT = get_receptionist_info

        try:
            result = self.execute_select_param(SELECT_STATEMENT, e_id)
            message = "Success: employee information retrieved"

        except (Exception, pg2.DatabaseError) as error:
            result = None
            message = ('Failure:', error)
        return result, message


    def update_employee_info(self, form):
        param = self.process_form(form)
        e_id = param[0]
        param.pop(0)  # remove Id from the form
        param.pop(-1)   # remove the empty string, created as a result of name for the button
        param.append(e_id)

        emp_type = self.ident_employee_type(e_id)
        if emp_type == 'd':
            UPDATE_STATEMENT = update_doctor_info
        elif emp_type == 'r':
            UPDATE_STATEMENT = update_receptionist_info

        try:
            self.execute_insert(UPDATE_STATEMENT, param)
            message = "Employee information successfully updated"

        except (Exception, pg2.DatabaseError) as error:
            message = ("Error while updating employee: ", error)

        return message





    def delete_employee(self, form):
        param = self.process_form(form)
        e_id = param[0]
        print(e_id)
        emp_type = self.ident_employee_type(e_id)

        DELETE_STATEMENT = delete_employee

        try:
            self.cursor.execute(DELETE_STATEMENT, [e_id])
            message = "Employee successfuly deleted! Status = 0 "
        except (Exception, pg2.DatabaseError) as error:
            message = ("Error while deleting employee: ", error)

        return message
