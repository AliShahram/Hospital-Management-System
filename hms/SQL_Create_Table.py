
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

"""

create_table_procedure = """
BEGIN;
    create table patient(
    p_id serial primary key,
    name varchar(200),
    DOB date,
    address varchar(200),
    email VARCHAR(100),
    contact varchar(200)
    );

    create table visit(
    v_id serial primary key,
    p_id int REFERENCES patient(p_id),
    admit_date date,
    discharge_date date NULL
    );

    CREATE TABLE room(
    r_id SERIAL primary key,
    type VARCHAR(64),
    cost REAL
);

CREATE TABLE medicine(
    m_id SERIAL primary key,
    name VARCHAR(64),
    cost REAL
);


CREATE TABLE operation(
    o_id SERIAL primary key,
    name VARCHAR(64),
    cost REAL
);


CREATE TABLE test(
    t_id SERIAL primary key,
    name VARCHAR(64),
    cost REAL
);

create table operate(
    d_id int REFERENCES doctor(d_id),
    o_id int REFERENCES operation(o_id),
    v_id int REFERENCES visit(v_id),
    datetime date
);

create table prescribe(
    d_id int REFERENCES doctor(d_id),
    m_id int REFERENCES medicine(m_id),
    v_id int REFERENCES visit(v_id),
    datetime date
);

create table testing(
    d_id int REFERENCES doctor(d_id),
    t_id int REFERENCES test(t_id),
    v_id int REFERENCES visit(v_id),
    datetime date
);

COMMIT;

"""
