
#SQL

CREATE_EMP_DOC_ADMIN_RECEP = """
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
        r_id SERIAL,
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
        a_id SERIAL,
        f_name VARCHAR(64),
        l_name VARCHAR(64),
        dob DATE,
        address VARCHAR(64),
        email VARCHAR(64),
        PRIMARY KEY (a_id),
        FOREIGN KEY (a_id) REFERENCES employee(e_id)
    );

    COMMIT;
"""


create_table_room = """
    CREATE TABLE room(
    r_id SERIAL,
    type VARCHAR(64),
    cost REAL,
)"""


"""
CREATE TABLE medicine(
    m_id SERIAL,
    name VARCHAR(64),
    cost REAL,
    r_id SERIAL,
    FOREIGN KEY (r_id) REFERENCES room(r_id)
);


CREATE TABLE operation(
    o_id SERIAL,
    name VARCHAR(64),
    cost REAL,
);


CREATE TABLE test(
    t_id SERIAL,
    name VARCHAR(64),
    cost REAL,
);



"""
