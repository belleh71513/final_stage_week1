from mysql.connector import pooling
from dotenv import load_dotenv
import os
import mysql.connector

load_dotenv()


dbconfig = {
"host":os.getenv("DB_HOST"),
"user":os.getenv("DB_USER"),
"password":os.getenv("DB_PASSWORD"),
"database":os.getenv("DB_DATABASE")
}

pool = mysql.connector.pooling.MySQLConnectionPool(
  pool_name = "my_pool",
  pool_size = 5,
  pool_reset_session = True,
  **dbconfig
)


def insert_message(message, image):
  try:
    con = pool.get_connection()
    cursor = con.cursor(buffered=True)
    sql = """
          INSERT INTO message_board (message, image) VALUES (%s, %s)
          """
    cursor.execute(sql, (message, image))
    return True
  except mysql.connector.Error as e:
    con.rollback()
    print(f"insert_message function {e}")
    return False
  finally:
    con.commit()
    con.close()

def get_message():
  try:
    con = pool.get_connection()
    cursor = con.cursor(buffered=True, dictionary=True)
    sql = """
          select * from message_board
          """
    cursor.execute(sql)
    result = cursor.fetchall()
    print(result)
    return result
  except mysql.connector.Error as e:
    con.rollback()
    print(f"get_message function {e}")
    return False
  finally:
    con.close()