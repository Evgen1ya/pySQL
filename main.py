import psycopg2

conn = psycopg2.connect(database="netology_db", user="postgres", password="491850")
cur = conn.cursor()
class Clients:
    def __init__(self, table_name, clients_firstname, clients_surname, clients_email):
        self.table_name = table_name
        self.clients_firstname = clients_firstname
        self.clients_surname = clients_surname
        self.clients_email = clients_email

    def create_table(self):
        cur.execute("""
        CREATE TABLE IF NOT EXISTS table_name=%s (
                id SERIAL PRIMARY KEY,
                clients_firstname=%s VARCHAR(40) NOT NULL,
                clients_surname=%s VARCHAR(40) N,
                clients_email=%s text;  
        """, (
        self.table_name, self.clients_firstname, self.clients_surname, self.clients_email))
        # print(cur.fetchall())

    def create_table_clients_phone(self, clients_number):
        self.clients_number = clients_number
        cur.execute("""
                CREATE TABLE IF NOT EXISTS Clients_phone (
                        id SERIAL PRIMARY KEY,
                        clients_id=%s INTEGER REFERENCES Clients_db(id),
                        clients_number=%s INTEGER
                """, (
            self.clients_number))
        # print(cur.fetchall())


    def add_client(self, surname, firstname, email):
        self.firstname = firstname
        self.surname = surname
        self.email = email
        cur.execute("""
            INSERT INTO table_name=%s (clients_firstname=%s, clients_surname=%s, clients_email=%s) 
            VALUES(firstname=%s, surname=%s, email=%s);
            """, (
        self.table_name, self.clients_firstname, self.clients_surname, self.clients_email,
        firstname, surname, email))
        # print(cur.fetchall())

    def update_number(self, number, clients_id, id: str):
        self.clients_id = clients_id
        self.number = number
        self.id = id
        cur.execute("""
            UPDATE Clients_phone
                SET clients_number=%s = number=%
                WHERE id=%s = clients_id=%s;
            """, (self.clients_number, self.id, number, clients_id))
        # print(cur.fetchall())

    def update_info(self, firstname, surname, email, clients_id: str):
        self.firstname = firstname
        self.surname = surname
        self.email = email
        self.clients_id = clients_id
        cur.execute("""
            UPDATE table_name=%s
                SET clients_firstname=%s = firstname=%s, self.clients_surname=%s = surname=%s,
                clients_email=%s = email=%s
                WHERE id=%s = clients_id=%s;
            """, (
        self.table_name, self.clients_firstname, self.clients_surname,  self.clients_email,
        self.id, firstname, surname, email, clients_id))
        # print(cur.fetchall())

    def delete_number(self, number, clients_id: str):
        self.clients_id = clients_id
        self.number = number
        cur.execute("""
            UPDATE Clients_phone
                SET clients_number=%s = NULL
                WHERE id=%s = clients_id=%s;
            """, (self.table_name, self.clients_number, self.id, number, clients_id))
        # print(cur.fetchall())

    def delete_client(self, clients_id: str):
        self.clients_id = clients_id
        cur.execute("""
            DELETE FROM table_name=%s
                WHERE id=%s = clients_id=%s;
            """, (self.table_name, self.id, clients_id))
        # print(cur.fetchall())

    def find_client(self, firstname, surname, email, number: str):
        self.firstname = firstname
        self.surname = surname
        self.number = number
        self.email = email
        cur.execute("""
                    SELECT id FROM table_name=%s
                    WHERE firstname=%s OR surname=%s OR email=%s OR number=%s;
                    """, (self.table_name, firstname, surname, email, number))
        # print(cur.fetchall())

        conn.close()




with psycopg2.connect(database="netology_db", user="postgres", password="491850") as conn:
    cur = conn.cursor()
    table_1 = Clients('Clients_db', 'first_name', 'last_name', 'email')
    table_1.create_table()
    client_1 = Clients()
    client_1.add_client('Kim', 'Kate', 'None', 'None')
    client_1.update_number('789283', '1')
    client_1.update_info('Kim', 'Kate', '334232', 'fwefw', '1')

    conn.close()
