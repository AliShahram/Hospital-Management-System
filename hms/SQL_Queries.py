
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

        insert into operate (d_id, datetime, o_id, v_id)
        values (%s, %s, %s, %s);

        """

insert_prescription_procedure = """

        insert into prescribe (d_id, datetime, m_id, v_id)
        values (%s, %s, %s, %s);

        """

insert_testing_procedure = """

        insert into testing (d_id, datetime, t_id, v_id)
        values (%s, %s, %s, %s);

        """

find_id_for_operate = """
        select o_id
        from operation
        where name = %s;
        """

find_id_for_medicine = """
        select m_id
        from medicine
        where name = %s;
        """

find_id_for_test = """
        select t_id
        from test
        where name = %s;
        """

get_visit_id = """
        select max(v_id)
        from visit
        where p_id = %s;
        """

get_operation_name = """
        select name
        from operation;"""
get_medicine_name = """
        select name
        from medicine;"""
get_test_name = """
        select name
        from test;"""

get_operation_history = """
        select name
        from operation
        where o_id in(
        select o_id
        from operate
		where v_id = (
        select max(v_id)
	    from visit
		where p_id = %s));
"""
get_prescription_history = """
        select name
        from medicine
        where m_id in(
        select m_id
        from prescribe
		where v_id = (
        select max(v_id)
	    from visit
		where p_id = %s));
"""
get_test_history = """
        select name
        from test
        where t_id in(
        select t_id
        from testing
		where v_id = (
        select max(v_id)
	    from visit
		where p_id = %s));
"""
