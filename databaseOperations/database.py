import mysql.connector


def create_db_connection(host_name, user_name, user_password, db_name):
    connection = None
    try:
        connection = mysql.connector.connect(
            host=host_name,
            user=user_name,
            passwd=user_password,
            database=db_name
        )
        print("MYSQL database connection successfull")
    except Exception as e:
        print(e)
    return connection


connection = create_db_connection("localhost", "root", "root", "encrypted_database")


def database_update(query):
    cursor = connection.cursor()
    try:
        cursor.execute(query)
        connection.commit()
    except Exception as e:
        print(e)  # return "error" next step


def database_select(query):
    cursor = connection.cursor()
    result_string = None
    try:
        cursor.execute(query)
        result_string = cursor.fetchall()
        # list of tuples
        return result_string
    except Exception as e:
        print(e)  # return "error" next step
