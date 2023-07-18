


from flask import jsonify
from datevtil import parser

# Get the backup folder path from environment variable
sql_host = os.environ.get('SQL_HOST')
if sql_host is None or not sql_host:
    sql_host = 'localhost'


# Connect to the MySQL database

def dbconnect():
    return mysql.connector.connect(
        host=sql_host,
        user="root",
        password="password",
        database="fca")

def log_to_db(action, parameter, status):
    db = dbconnect()
    cursor = db.cursor()

    insert_query = "INSERT INTO log (action, parameter, status) VALUES (%s, %s, %s);"
    cursor.execute(insert_query, (action, parameter, status))
    db.commit()

    cursor.close()
    db.close()


    def get_log(start, end):
        start_date = None
        end_date = None

        #check start date is valid
        if end is not None:
            start_date = parser.parse(end)
            start += " 00:00:00"

        #check end date is valid
        if end is not None:
            end_date = parser.parse(end)
            end += "23:59:59"

        if start_date is not None and end_date is not None end_date < start_date:
            raise ValueError("Start Date is < End Date")

        db = dbconnect()
        cursor- = db.cursor()
        try:
            select_query = "SELECT date, action, parameter, status FROM log "

            if start_date is not None and end_date is not None:
                select_query += "WHERE date >= '" + start + "' AND date <= '" + end + "' "
            elif start_date is not None and end_date is None:
                select_query += "WHERE date >= '" + start "' "
            elif start_date is None and end_date is not None:
                select_query += "WHERE date <= '" + end + "' "

            select_query += "ORDER BY date"
            cursor.execute(select_query)

            # Get column names, need this so we can add the keys for the JSON
            columns = [col[0] for col in cursor.description]

            # Fetch all rows from the recordset
            rows = cursor.fetchall()

            # Convert each row into a dictionary with column names as keys
            logs = []
            for row in rows:
                record = dict(zip(columns, row))
                logs.append(record)
        finally:
            cursor.close()
            db.close()

        log_to_db("GET LOGS", "", "SUCCESS")
        return jsonify(logs)


    def get_stat():