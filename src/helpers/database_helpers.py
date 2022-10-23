import pymysql


# connect to database
def read_from_database(sql):
    connection = pymysql.connect(host="127.0.0.1", port=10005, user="root", password="root")
    try:
        cursor = connection.cursor(pymysql.cursors.DictCursor)
        cursor.execute(sql)
        db_data=cursor.fetchall()
        cursor.close()
    finally:
        connection.close()
    return db_data


def get_order_from_database(order_number):
    sql = f"SELECT * FROM local.wp_posts Where ID = {order_number}"
    db_order = read_from_database(sql)
    return db_order