
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
        INSERT INTO receptionist (re_id,
                            f_name,
                            l_name,
                            dob,
                            address,
                            email,
                            phone)
        VALUES (%s, %s, %s, %s, %s, %s, %s);
        """

# INSERT INTO receptionist (re_id,
#                     f_name,
#                     l_name,
#                     dob,
#                     address,
#                     email,
#                     phone)
# VALUES (1,'as','asd','1222-12-12','asd','asd', 123);
        # INSERT INTO doctor (d_id,
        #                     f_name,
        #                     l_name,
        #                     dob,
        #                     address,
        #                     email,
        #                     phone,
        #                     consult_fee)
        # VALUES (1,'as','asd','1222-12-12','asd','asd', 123,123);

get_doctor_info = """
    SELECT * FROM doctor
    WHERE d_id = %s;
    """


get_receptionist_info = """
    SELECT * FROM receptionist
    WHERE re_id = %s;
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
    WHERE re_id = %s;
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
		where p_id = %s));"""



register_patient = """
BEGIN;
INSERT INTO Patient (f_name, l_name, d_o_b, email, address, phone)
VALUES (%s, %s, %s, %s, %s, %s);
COMMIT;
"""


get_patient_info = """
SELECT * FROM patient
    WHERE p_id = %s;
"""

delete_patient = """
BEGIN;
DELETE FROM Patient WHERE p_id = %s;
COMMIT;
"""

update_patient_info = """
BEGIN;
UPDATE  Patient SET
(f_name, l_name, d_o_b, email, address, phone)
= ( %s, %s, %s, %s, %s, %s)
WHERE p_id = %s;
COMMIT;
"""

get_max_p_id="""
SELECT MAX(p_id) FROM Patient;
"""


create_visit = """
BEGIN;
INSERT INTO Visit ( p_id, admit_date, discharge_date)
VALUES (%s, %s, %s);
COMMIT;
"""

create_visit_discharge_null = """
BEGIN;
INSERT INTO Visit (p_id, admit_date)
VALUES (%s, %s);
COMMIT;
"""

get_visit_info = """
SELECT *
FROM Visit
WHERE v_id = (%s);
"""

update_visit_info = """
BEGIN;
UPDATE  Visit SET
(p_id, admit_date, discharge_date)
= (%s, %s, %s)
WHERE v_id = (%s);
COMMIT;
"""

delete_visit = """
BEGIN;
DELETE FROM Visit WHERE v_id = (%s);
COMMIT;
"""
get_max_v_id = """
SELECT MAX(v_id) FROM Visit;
"""

get_admission_info = """
SELECT *
FROM Admission
WHERE ad_id = (%s);
"""

update_admission_info = """
BEGIN;
UPDATE  Admission SET
(re_id, v_id, ro_id, admit_date)
= (%s, %s, %s, %s)
WHERE ad_id =(%s);
COMMIT;
"""

update_admission_discharge_null = """
BEGIN;
UPDATE  Admission SET
(re_id, v_id, ro_id, admit_date)
= (%s, %s, %s, %s)
WHERE ad_id =(%s);
COMMIT;
"""

delete_admission = """
BEGIN;
DELETE FROM Admission WHERE ad_id = (%s);
COMMIT;
"""

create_admission ="""
BEGIN;
INSERT INTO Admission (re_id, v_id, ro_id, admit_date, dis_date)
VALUES (%s, %s, %s, %s, %s);
COMMIT;
"""

create_admission_discharge_null ="""
BEGIN;
INSERT INTO Admission (re_id, v_id, ro_id, admit_date)
VALUES (%s, %s, %s, %s);
COMMIT;
"""

get_max_ad_id = """
SELECT MAX(ad_id) FROM Admission;
"""

get_appointment_info = """
SELECT *
FROM Appointment
WHERE (d_id, ap_date, ap_time) = (%s, %s, %s);
"""

update_appointment_info = """
BEGIN;
UPDATE  Appointment SET
(re_id, v_id, d_id, ap_date, ap_time)
= (%s, %s, %s, %s, %s)
WHERE (d_id, ap_date, ap_time)= (%s, %s, %s);
COMMIT;
"""

delete_appointment = """
BEGIN;
DELETE FROM Appointment WHERE (d_id, ap_date, ap_time)= (%s, %s, %s);
COMMIT;
"""


get_consultation_info = """
SELECT *
FROM Consultation
WHERE (d_id, cons_date, cons_time) = (%s, %s, %s);
"""

update_consultation_info = """
BEGIN;
UPDATE Consultation SET (d_id, re_id, v_id, cons_date, cons_time)
= (%s, %s, %s, %s, %s)
WHERE (d_id, cons_date, cons_time) = (%s, %s, %s);
COMMIT;
"""


create_appointment = """
BEGIN;
INSERT INTO Appointment (re_id, v_id, d_id, ap_date, ap_time)
VALUES (%s, %s, %s, %s, %s);
COMMIT;
"""

create_consultation = """
BEGIN;
INSERT INTO Consultation (d_id, re_id, v_id, cons_date, cons_time)
VALUES (%s, %s, %s, %s, %s);
COMMIT;
"""

delete_consultation = """
BEGIN;
DELETE FROM Consultation WHERE (d_id, re_id, cons_date, cons_time)= (%s, %s, %s, %s);
COMMIT;
"""
