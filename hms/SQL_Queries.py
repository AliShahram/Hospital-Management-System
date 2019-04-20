
ident_employee_type = """
        SELECT type FROM employee
        WHERE e_id = %s
    """


register_new_employee = """
    INSERT INTO employee (type, e_status)
    VALUES (%s, '1')
    """

get_recent_emp_id = """
    SELECT max(e_id)
    FROM employee;
    """

register_new_doctor = """
        INSERT INTO doctor (d_id,
                            f_name,
                            l_name,
                            dob,
                            address,
                            email,
                            phone,
                            consult_fee)
        VALUES (%s, %s, %s, %s, %s, %s, %s, %s);
        """


register_new_recep = """
        INSERT INTO receptionist (r_id,
                            f_name,
                            l_name,
                            dob,
                            address,
                            email,
                            phone)
        VALUES (%s, %s, %s, %s, %s, %s, %s);
        """
