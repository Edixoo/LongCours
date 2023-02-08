import psycopg2

def query_database(query):
    try:
        connection = psycopg2.connect(
            host="postgresql-saejv.alwaysdata.net",
            database="saejv_longcours",
            user="saejv",
            password="jeuvideo123.."
        )

        cursor = connection.cursor()
        cursor.execute(query)
        result = cursor.fetchall()

        return result
    except (Exception, psycopg2.Error) as error:
        print("Error while connecting to PostgreSQL", error)
    finally:
        if(connection):
            cursor.close()
            connection.close()
            print("PostgreSQL connection is closed")

def create_table(table_name, columns):
    try:
        connection = psycopg2.connect(
            host="postgresql-saejv.alwaysdata.net",
            database="saejv_longcours",
            user="saejv",
            password="jeuvideo123.."
        )

        cursor = connection.cursor()
        create_table_query = f"CREATE TABLE {table_name} ({columns});"
        cursor.execute(create_table_query)
        connection.commit()
        print(f"Table {table_name} créée avec succès.")
    except (Exception, psycopg2.Error) as error:
        print("Error while connecting to PostgreSQL", error)
    finally:
        if(connection):
            cursor.close()
            connection.close()
            print("PostgreSQL connection is closed")

def insert_into_table(table_name, values):
    try:
        connection = psycopg2.connect(
            host="postgresql-saejv.alwaysdata.net",
            database="saejv_longcours",
            user="saejv",
            password="jeuvideo123.."
        )

        cursor = connection.cursor()
        insert_query = f"INSERT INTO {table_name} VALUES {values};"
        cursor.execute(insert_query)
        connection.commit()
        print("Ligne insérée avec succès.")
    except (Exception, psycopg2.Error) as error:
        print("Error while connecting to PostgreSQL", error)
    finally:
        if(connection):
            cursor.close()
            connection.close()
            print("PostgreSQL connection is closed")



table_name = "Classement"
"""columns = "Pseudo varchar, Position int"
create_table(table_name, columns) 
values = "('Bernard', 1)"
insert_into_table(table_name, values)"""
query = "SELECT * FROM Classement"
result = query_database(query)
print(result)