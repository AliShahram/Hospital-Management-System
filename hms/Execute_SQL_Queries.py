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


    def process_form_sorted(self, form):
        result = []
        keys = []
        dict = form.dict()
        for key in dict:
            if key[0].isdigit():
                keys.append(key)
        keys.sort()
        for key in keys:
            value = dict[key]
            result.append(value)
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


    def fill_option_select(self, statement):
        result = []
        self.cursor.execute(statement)
        rows = self.cursor.fetchall()
        for i in rows:
            result.append(i[0])
        return result


    def execute_fetchall(self, statement, param):
        result = []
        self.cursor.execute(statement, param)
        rows = self.cursor.fetchall()
        for i in rows:
            result.append(i[0])
        return result



#-------------------------------------------------------
#Queries Execution
#-------------------------------------------------------

    def validate_employee(self, e_id):
        SELECT_STATEMENT = validate_employee
        result = self.execute_select_param(SELECT_STATEMENT, e_id)
        status = int(result[0])

        if status == 1:
            return True
        else:
            return False


    def ident_employee_type(self, e_id):
        SELECT_STATEMENT = ident_employee_type
        self.current_user = e_id
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





    def create_room(self, form):
        param = self.process_form_sorted(form)
        CREATE_STATEMENT = create_room

        try:
            self.cursor.execute(CREATE_STATEMENT, param)
            result = "Insertion Successful"
        except (Exception, pg2.DatabaseError) as error:
            result = ("Error while inserting into PostgreSQL table", error)
        return result


    def insert_operation(self, form):
        param = self.process_form_sorted(form)
        INSERT_STATEMENT = insert_operation

        try:
            self.cursor.execute(INSERT_STATEMENT, param)
            result = "Insertion Successful"
        except (Exception, pg2.DatabaseError) as error:
            result = ("Error while inserting into PostgreSQL table", error)
        return result


    def insert_medicine(self, form):
        param = self.process_form_sorted(form)
        INSERT_STATEMENT = insert_medicine

        try:
            self.cursor.execute(INSERT_STATEMENT, param)
            result = "Insertion Successful"
        except (Exception, pg2.DatabaseError) as error:
            result = ("Error while inserting into PostgreSQL table", error)
        return result


    def insert_test(self, form):
        param = self.process_form_sorted(form)
        INSERT_STATEMENT = insert_test

        try:
            self.cursor.execute(INSERT_STATEMENT, param)
            result = "Insertion Successful"
        except (Exception, pg2.DatabaseError) as error:
            result = ("Error while inserting into PostgreSQL table", error)
        return result


    def get_room_info(self, form):
        param = self.process_form_sorted(form)
        room_id = param[0]
        SELECT_STATEMENT = get_room_info

        try:
            result = self.execute_select_param(SELECT_STATEMENT, room_id)
            message = "Success: room information retrieved"

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


    def update_room_info(self, form):
        param = self.process_form_sorted(form)
        r_id = param[0]
        param.pop(0)  # remove Id from the form
        param.append(r_id)

        UPDATE_STATEMENT = update_room_info

        try:
            self.execute_insert(UPDATE_STATEMENT, param)
            message = "Room information successfully updated"

        except (Exception, pg2.DatabaseError) as error:
            message = ("Error while updating room: ", error)

        return message


    def delete_room(self, form):
        param = self.process_form_sorted(form)
        r_id = param[0]

        DELETE_STATEMENT = delete_room

        try:
            self.cursor.execute(DELETE_STATEMENT, [r_id])
            message = "Room successfuly deleted! Status = 0 "
        except (Exception, pg2.DatabaseError) as error:
            message = ("Error while deleting room: ", error)

        return message


    def get_medicine_info(self, form):
        param = self.process_form_sorted(form)
        m_id = param[0]
        SELECT_STATEMENT = get_medicine_info

        try:
            result = self.execute_select_param(SELECT_STATEMENT, m_id)
            result = ("medicine", *result)
            message = "Success: medical information retrieved"

        except (Exception, pg2.DatabaseError) as error:
            result = None
            message = ('Failure:', error)
        return result, message


    def get_operation_info(self, form):
        param = self.process_form_sorted(form)
        o_id = param[0]
        SELECT_STATEMENT = get_operation_info

        try:
            result = self.execute_select_param(SELECT_STATEMENT, o_id)
            result = ("operation", *result)
            message = "Success: operation information retrieved"

        except (Exception, pg2.DatabaseError) as error:
            result = None
            message = ('Failure:', error)
        return result, message


    def get_test_info(self, form):
        param = self.process_form_sorted(form)
        t_id = param[0]
        SELECT_STATEMENT = get_test_info

        try:
            result = self.execute_select_param(SELECT_STATEMENT, t_id)
            result = ("test", *result)
            message = "Success: test information retrieved"

        except (Exception, pg2.DatabaseError) as error:
            result = None
            message = ('Failure:', error)
        return result, message


    def update_medical_info(self, form):
        param = self.process_form_sorted(form)
        id = param[0]
        param.pop(0)  # remove Id from the form
        param.append(id)

        type = param[0]
        param.pop(0) # remove type from the form

        if type == "medicine":
            UPDATE_STATEMENT = update_medicine_info
        if type == "operation":
            UPDATE_STATEMENT = update_operation_info
        if type == "test":
            UPDATE_STATEMENT = update_test_info

        try:
            self.execute_insert(UPDATE_STATEMENT, param)
            message = "Medical information successfully updated"

        except (Exception, pg2.DatabaseError) as error:
            message = ("Error while updating medical: ", error)
        return message









    def get_visit_id(self, p_id):

        statement = get_visit_id

        try:
            result = self.execute_select_param(statement, p_id)
            result =  result[0]
        except(Exception, pg2.DatabaseError) as er:
            result = None
        return result

    def get_oper_id(self, name):
        statement = find_id_for_operate

        try:
            result = self.execute_select_param(statement, name)
            result = result[0]
        except(Exception, pg2.DatabaseError):
            result = None
        return result

    def get_med_id(self, name):
        statement = find_id_for_medicine

        try:
            result = self.execute_select_param(statement, name)
            result = result[0]
        except(Exception, pg2.DatabaseError):
            result = None
        return result

    def get_test_id(self, name):
        statement = find_id_for_test

        try:
            result = self.execute_select_param(statement, name)
            result = result[0]
        except(Exception, pg2.DatabaseError):
            result = None
        return result


    def register_opeartion(self, form):

        param = self.process_form(form)
        visit = self.get_visit_id(param[0])
        operation = self.get_oper_id(param[2])
        doctor = self.current_user
        param[0] = doctor
        param[2] = operation
        param.insert(3, visit)

        INSERT_STATEMENT = insert_operation_procedure

        try:
            self.cursor.execute(INSERT_STATEMENT, param)
            result = "Insertion Successful"
        except (Exception, pg2.DatabaseError) as error:
            print(error)
            result = ("Error while inserting into PostgreSQL table", error)
        return result

    def register_prescription(self, form):

        param = self.process_form(form)

        visit = self.get_visit_id(param[0])
        medicine = self.get_med_id(param[2])
        doctor = self.current_user
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

        visit = self.get_visit_id(param[0])
        test = self.get_test_id(param[2])
        doctor = self.current_user
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

    def get_operation_name(self):
        statement = get_operation_name
        try:
            result = self.fill_option_select(statement)
        except (Exception, pg2.DatabaseError) as error:
            result = ("Error: ", error)
        return result

    def get_medicine_name(self):
        result = []
        statement = get_medicine_name
        try:
            result = self.fill_option_select(statement)
        except (Exception, pg2.DatabaseError) as error:
            result = ("Error: ", error)
        return result

    def get_test_name(self):
        statement = get_test_name
        try:
            result = self.fill_option_select(statement)
        except (Exception, pg2.DatabaseError) as error:
            result = ("Error: ", error)
        return result



    def get_medical_history(self, form):
        param = self.process_form(form)
        p_id = param[0]

        try:
            operation = self.execute_fetchall(get_operation_history, p_id)
            message = "Success: employee information retrieved"
        except (Exception, pg2.DatabaseError) as error:
            operation = None
            message = ('Failure:', error)
        try:
            Prescription = self.execute_fetchall(get_prescription_history, p_id)
            message = "Success: employee information retrieved"
        except (Exception, pg2.DatabaseError) as error:
            Prescription = None
            message = ('Failure:', error)
        try:
            test = self.execute_fetchall(get_test_history, p_id)
            message = "Success: employee information retrieved"
        except (Exception, pg2.DatabaseError) as error:
            test = None
            message = ('Failure:', error)

        return operation, Prescription, test, message
