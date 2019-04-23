
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

insert_operation_procedure = """
        begin;
        insert into operate (d_id, time, o_id, v_id)
        values (%s, %s, %s, %s)
        commit;
        """

insert_prescription_procedure = """
        begin;
        insert into prescribe (d_id, time, m_id, v_id)
        values (%s, %s, %s, %s)
        commit;
        """

insert_testing_procedure = """
        begin;
        insert into test (d_id, time, t_id, v_id)
        values (%s, %s, %s, %s)
        commit;
        """

find_id_for_operate = """
        select o_id
        from operation
        where name = %s
        """

find_id_for_medicine = """
        select m_id
        from medicine
        where name = %s
        """

find_id_for_test = """
        select t_id
        from testing
        where name = %s
        """

get_visit_id = """
        select max(v_id)
        from visit
        where p_id = %s
        """
