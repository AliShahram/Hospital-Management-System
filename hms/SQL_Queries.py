
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

insert_new_operation = """

        BEGIN;

        INSERT INTO operation (name, cost, r_id)
        VALUES (%s, %s, %s);

        COMMIT;
"""

create_room = """

        INSERT INTO room (type, cost, status)
        VALUES (%s, %s, %s);
"""
