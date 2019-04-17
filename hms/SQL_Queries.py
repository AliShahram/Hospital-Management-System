from django.db import connection

class Database:
    def __init__(self):
        self.cursor = connection.cursor()

    def execute(self, statement, param):
        self.cursor.execute(statement, [param])
        row = self.cursor.fetchone()
        result = row[0]
        return result


    def ident_employee_type(self, e_id):
        SELECT_STATEMENT = """SELECT type FROM employee
                              WHERE e_id = %s
                            """
        try:
            result = self.execute(SELECT_STATEMENT, e_id)
        except:
            result = None
        return result
