
validate_employee = """
    SELECT e_status
    FROM employee
    WHERE e_id = %s;
    """


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
        COMMIT;
"""

create_room = """

        INSERT INTO room (type, cost, status)
        VALUES (%s, %s, %s);
"""

insert_operation = """

        INSERT INTO operation (name, cost, room_id)
        VALUES (%s, %s, %s);
"""

insert_medicine = """

        INSERT INTO medicine (name, cost)
        VALUES (%s, %s);
"""

insert_test = """

        INSERT INTO test (name, cost)
        VALUES (%s, %s);
"""

get_room_info = """

        SELECT * FROM room
        WHERE room_id = %s;
"""

update_room_info = """

    UPDATE room
    SET (type,
        cost,
        status) = (%s, %s, %s)
    WHERE room_id = %s;
    """

delete_room = """

    UPDATE room
    SET status = 0
    WHERE room_id = %s;
    """

get_medicine_info = """

        SELECT * FROM medicine
        WHERE m_id = %s;
"""

get_operation_info = """

        SELECT * FROM operation
        WHERE o_id = %s;
"""

get_test_info = """

        SELECT * FROM test
        WHERE t_id = %s;
"""

update_medicine_info = """

    UPDATE medicine
    SET (name,
        cost) = (%s, %s)
    WHERE m_id = %s;
    """

update_operation_info = """

    UPDATE operation
    SET (name,
        cost,
        room_id) = (%s, %s, %s)
    WHERE o_id = %s;
    """

update_test_info = """

    UPDATE test
    SET (name,
        cost) = (%s, %s)
    WHERE t_id = %s;
    """
