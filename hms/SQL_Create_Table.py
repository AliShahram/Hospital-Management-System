
#SQL


CREATE_EMP_DOC_ADMIN_RECEP = """
    BEGIN;

    CREATE TABLE employee (
        e_id  SERIAL PRIMARY KEY,
        type  VARCHAR(1),
        e_status  VARCHAR(1)
    );


    CREATE TABLE doctor(
        d_id INT,
        f_name VARCHAR(64),
        l_name VARCHAR(64),
        dob DATE,
        address VARCHAR(64),
        email VARCHAR(64),
        phone INT,
        consult_fee FLOAT,
        PRIMARY KEY (d_id),
        FOREIGN KEY (d_id) REFERENCES employee(e_id)
    );


    CREATE TABLE receptionist(
        r_id INT,
        f_name VARCHAR(64),
        l_name VARCHAR(64),
        dob DATE,
        address VARCHAR(64),
        email VARCHAR(64),
        phone INT,
        PRIMARY KEY (r_id),
        FOREIGN KEY (r_id) REFERENCES employee(e_id)
    );


    CREATE TABLE admin(
        a_id INT,
        f_name VARCHAR(64),
        l_name VARCHAR(64),
        dob DATE,
        address VARCHAR(64),
        email VARCHAR(64),
        PRIMARY KEY (a_id),
        FOREIGN KEY (a_id) REFERENCES employee(e_id)
    );

    CREATE TABLE Patient(
    p_id SERIAL,
    f_name VARCHAR,
    l_name VARCHAR,
    d_o_b DATE,
    email VARCHAR,
    address VARCHAR,
    phone VARCHAR,
    PRIMARY KEY (p_id)
    );

    CREATE TABLE Visit(
    v_id serial,
    p_id int,
    admit_date date,
    dis_date date,
    PRIMARY KEY (v_id),
    FOREIGN KEY (p_id) REFERENCES patient(p_id)
    );

    CREATE TABLE Appointment(
    re_id varchar,
    v_id varchar,
    d_id varchar,
    ap_date date,
    ap_time time,
    PRIMARY KEY (d_id, ap_date, ap_time),
    FOREIGN KEY (re_id) REFERENCES receptionist(re_id),
    FOREIGN KEY (v_id)  REFERENCES visit(v_id),
    );

    CREATE TABLE Consultation(
    d_id SERIAL,
    t_id VARCHAR,
    v_id VARCHAR,
    date DATE,
    time TIME,
    PRIMARY KEY (d_id, date, time),
    FOREIGN KEY (re_id) REFERENCES receptionist(re_id),
    FOREIGN KEY (v_id)  REFERENCES visit(v_id),
    FOREIGN (a_id) REFERENCES admission(a_id)
    );

    CREATE TABLE Admission(
    re_id INT,
    v_id INT,
    ro_id INT,
    admit_date date,
    dis_date date,
    PRIMARY KEY (ro_id, admit_date),
    FOREIGN KEY (v_id) REFERENCES visit(v_id),
    FOREIGN KEY (re_id)  REFERENCES receptionist(re_id)
    );
    COMMIT;
"""


create_aleks_work = """
    BEGIN;

    CREATE TABLE room(
        r_id SERIAL,
        type VARCHAR(64),
        cost REAL,
        status VARCHAR(1),
    );


    CREATE TABLE medicine(
        m_id SERIAL,
        name VARCHAR(64),
        cost REAL,
    );


    CREATE TABLE operation(
        o_id SERIAL,
        name VARCHAR(64),
        cost REAL,
        r_id INT,
        FOREIGN KEY (r_id) REFERENCES room(r_id),
    );


    CREATE TABLE test(
        t_id SERIAL,
        name VARCHAR(64),
        cost REAL,
    );

    COMMIT;
"""
