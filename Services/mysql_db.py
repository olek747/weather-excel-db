import mysql.connector
from mysql.connector import Error
def create_record(data):
    try:
        conn = mysql.connector.connect(
            host="localhost",  # lub "127.0.0.1",
            user="root",
            password="Powitanie01!",
            database="weather_db"
        )
        if not conn.is_connected():
            raise Error("Nie połączono")

        cursor = conn.cursor(dictionary=True)

        sql = """
            INSERT INTO records 
            (temp,temp_feels_like,pressure,humidity,weather_desc,clouds,place,wind,created) 
            VALUES 
            (%s, %s, %s, %s,%s, %s, %s, %s, NOW());
        """
        variables = (
            data['temp'],
            data['temp_feels_like'],
            data['pressure'],
            data['humidity'],
            data['description'],
            data['clouds'],
            data['place'],
            data['wind'],
        )
        cursor.execute(sql, variables)
        conn.commit()
        print("Zapisano do MySQL")

    except Error as e:
        print(e)
    finally:
        conn.close()
        cursor.close()