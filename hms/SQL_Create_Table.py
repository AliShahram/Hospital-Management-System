
#SQL


CREATE_ALL = """
    BEGIN;

    CREATE TABLE employee (
        e_id  SERIAL PRIMARY KEY,
        type  VARCHAR(1),
        e_status  VARCHAR(1)
    );


    CREATE TABLE doctor(
        d_id SERIAL,
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
        re_id SERIAL,
        f_name VARCHAR(64),
        l_name VARCHAR(64),
        dob DATE,
        address VARCHAR(64),
        email VARCHAR(64),
        phone INT,
        PRIMARY KEY (re_id),
        FOREIGN KEY (re_id) REFERENCES employee(e_id)
    );


    CREATE TABLE admin(
        a_id SERIAL,
        f_name VARCHAR(64),
        l_name VARCHAR(64),
        dob DATE,
        address VARCHAR(64),
        email VARCHAR(64),
        PRIMARY KEY (a_id),
        FOREIGN KEY (a_id) REFERENCES employee(e_id)
    );


    CREATE TABLE patient(
        p_id SERIAL,
        f_name VARCHAR,
        l_name VARCHAR,
        d_o_b DATE,
        email VARCHAR,
        address VARCHAR,
        phone VARCHAR,
        PRIMARY KEY (p_id)
    );


    CREATE TABLE visit(
        v_id serial primary key,
        p_id int REFERENCES patient(p_id),
        admit_date date,
        discharge_date date NULL
    );


    CREATE TABLE admission(
        re_id INT,
        v_id INT,
        ro_id INT,
        admit_date date,
        dis_date date,
        PRIMARY KEY (ro_id, admit_date),
        FOREIGN KEY (v_id) REFERENCES visit(v_id),
        FOREIGN KEY (re_id)  REFERENCES receptionist(re_id)
    );


    CREATE TABLE appointment(
        re_id INT,
        v_id INT,
        d_id INT,
        ap_date date,
        ap_time time,
        PRIMARY KEY (d_id, ap_date, ap_time),
        FOREIGN KEY (re_id) REFERENCES receptionist(re_id),
        FOREIGN KEY (v_id)  REFERENCES visit(v_id)
    );


    CREATE TABLE consultation(
        d_id INT,
        re_id INT,
        v_id INT,
        date DATE,
        time TIME,
        PRIMARY KEY (d_id, date, time),
        FOREIGN KEY (re_id) REFERENCES receptionist(re_id),
        FOREIGN KEY (v_id) REFERENCES visit(v_id)
    );


    CREATE TABLE room(
        room_id SERIAL PRIMARY KEY,
        type VARCHAR(64),
        cost REAL,
        status VARCHAR(1)
    );


    CREATE TABLE medicine(
        m_id SERIAL PRIMARY KEY,
        name VARCHAR(64),
        cost REAL
    );


    CREATE TABLE operation(
        o_id SERIAL PRIMARY KEY,
        name VARCHAR(64),
        cost REAL,
        room_id INT,
        FOREIGN KEY (room_id) REFERENCES room(room_id)
    );


    CREATE TABLE test(
        t_id SERIAL PRIMARY KEY,
        name VARCHAR(64),
        cost REAL
    );


    CREATE TABLE operate(
        d_id int REFERENCES doctor(d_id),
        o_id int REFERENCES operation(o_id),
        v_id int REFERENCES visit(v_id),
        datetime date
    );


    CREATE TABLE prescribe(
        d_id int REFERENCES doctor(d_id),
        m_id int REFERENCES medicine(m_id),
        v_id int REFERENCES visit(v_id),
        datetime date
    );


    CREATE TABLE testing(
        d_id int REFERENCES doctor(d_id),
        t_id int REFERENCES test(t_id),
        v_id int REFERENCES visit(v_id),
        datetime date
    );


    COMMIT;
"""
