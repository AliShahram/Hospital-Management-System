
ident_employee_type = """

        SELECT type FROM employee
        WHERE e_id = %s
    """


register_new_doctor = """

        BEGIN;
        INSERT INTO employee (type, e_status)
        VALUES('d', '1');

        INSERT INTO doctor (f_name,
                            l_name,
                            dob,
                            address,
                            email,
                            phone,
                            consult_fee)
        VALUES (%s, %s, %s, %s, %s, %s, %s);
        COMMIT;
"""

create_room = """

        INSERT INTO room (type, cost, status)
        VALUES (%s, %s, %s);
"""

insert_operation = """

        INSERT INTO operation (name, cost, r_id)
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
        WHERE r_id = %s;
"""

update_room_info = """

    UPDATE room
    SET (type,
        cost,
        status) = (%s, %s, %s)
    WHERE r_id = %s;
    """

delete_room = """

    UPDATE room
    SET status = 0
    WHERE r_id = %s;
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
        r_id) = (%s, %s, %s)
    WHERE o_id = %s;
    """

update_test_info = """

    UPDATE test
    SET (name,
        cost) = (%s, %s)
    WHERE t_id = %s;
    """
