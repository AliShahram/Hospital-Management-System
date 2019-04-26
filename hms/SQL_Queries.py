
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


get_doctor_info = """
    SELECT * FROM doctor
    WHERE d_id = %s;
    """


get_receptionist_info = """
    SELECT * FROM receptionist
    WHERE r_id = %s;
    """

update_doctor_info = """
    UPDATE doctor
    SET (f_name,
        l_name,
        dob,
        address,
        email,
        phone,
        consult_fee) = (%s, %s, %s, %s, %s, %s, %s)
    WHERE d_id = %s;
    """



update_receptionist_info = """
    UPDATE receptionist
    SET (f_name,
        l_name,
        dob,
        address,
        email,
        phone) = (%s, %s, %s, %s, %s, %s)
    WHERE r_id = %s;
    """



delete_employee = """
    UPDATE employee
    SET e_status = 0
    WHERE e_id = %s;
    """
