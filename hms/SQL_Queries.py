
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

create_visit = """
BEGIN;
INSERT INTO Visit ( p_id, admit_date, dis_date)
VALUES (%s, %s, %s);
COMMIT;
"""

get_visit_info = """
SELECT *
FROM Visit
WHERE v_id = %s;
"""

update_visit_info = """
BEGIN;
UPDATE  Visit SET
(p_id, admit_date, dis_date)
= ( %s, %s, %s)
WHERE v_id = %s;
COMMIT;
"""

delete_visit = """
BEGIN;
DELETE FROM Visit WHERE v_id = %s;
COMMIT;
"""
create_admission = """
BEGIN;
INSERT INTO Admission (re_id, v_id, ro_id, admit_date, dis_date)
VALUES (%s, %s, %s, %s, %s);
COMMIT;
"""

get_admission_info = """
SELECT *
FROM Admission
WHERE (d_id, ap_date, ap_time) = %s, %s, %s;
"""

update_admission_info = """
BEGIN;
UPDATE  Visit SET
(re_id, v_id, ro_id, admit_date, dis_date)
= (%s, %s, %s, %s, %s)
WHERE ad_id = %s;
COMMIT;
"""

delete_admission = """
BEGIN;
DELETE FROM Admission WHERE ad_id = %s;
COMMIT;
"""

create_appointment = """
BEGIN;
INSERT INTO Appointment (re_id, v_id, d_id, ap_date, ap_time)
VALUES (%s, %s, %s, %s, %s);
COMMIT;
"""

get_appointment_info = """
SELECT *
FROM Admission
WHERE (d_id, ap_date, ap_time) = %s, %s, %s;
"""

update_appointment_info = """
BEGIN;
UPDATE  Visit SET
(re_id, v_id, d_id, date, time)
= (%s, %s, %s, %s, %s)
WHERE ap_id = %s;
COMMIT;
"""

delete_appointment = """
BEGIN;
DELETE FROM Appointment WHERE ap_id = %s;
COMMIT;
"""

#CREATE TABLE Patient (p_id serial, f_name varchar , l_name varchar, d_o_b date, address varchar, email varchar, phone varchar);
#INSERT INTO Patient ( f_name, l_name, d_o_b,  address, email, phone) VALUES ('ali', 'goke', '2001-09-28', 'richmond', '@earlham', 'none');
#INSERT INTO Patient (f_name, l_name, d_o_b,  address, contact) VALUES ('ali', 'goke', '2001-09-28', 'richmond', '@earlham', none);
