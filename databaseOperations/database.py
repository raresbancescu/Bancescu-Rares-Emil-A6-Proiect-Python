import mysql.connector


def create_db_connection(host_name, user_name, user_password, db_name):
    """
    Function used for establishing the connection with the database
    :param str host_name: host name for the database(localhost)
    :param str user_name: database username
    :param str user_password: database user password
    :param str db_name: the name of the database
    :return CMySQLConnection connection: The connection to the database if the connection succeeded
    """
    conn = None
    try:
        conn = mysql.connector.connect(
            host=host_name,
            user=user_name,
            passwd=user_password,
            database=db_name
        )
        print("MYSQL database connection successful")
    except Exception as e:
        print(e)
    return conn


connection = create_db_connection("localhost", "root", "root", "encrypted_database")


def database_update(query):
    """
    Function used for updating the database
    :param str query: SQL query to be executed
    """
    cursor = connection.cursor()
    try:
        cursor.execute(query)
        connection.commit()
    except Exception as e:
        print(e)  # return "error" next step


def database_select(query):
    """
    FUnction used for extracting the information from the database
    :param str query: SQL query to be executed
    :return list: List with all the information we need from the database
    """
    cursor = connection.cursor()
    try:
        cursor.execute(query)
        result_string = cursor.fetchall()
        # list of tuples
        return result_string
    except Exception as e:
        print(e)  # return "error" next step
