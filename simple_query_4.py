
# needed import
import psycopg2

# connect to the database
try:
    db = "ubereats"
    user = "isdb"
    conn = psycopg2.connect(database=db, user=user)
    conn.autocommit = True
    cur = conn.cursor()
except psycopg2.Error as e:
    print("Unable to open connection: %s" % (e,))

def average_delivery_time(driver_id):
    # try statement to ensure properly closing connection
    try:
        # explanation of goal
        print("User Story: A driver should be able to know his average delivery time")
        print("Do demonstrate this we will find the average delivery time (in minutes) for driver %s" % driver_id)
        print()

        # the query template
        template = """
            SELECT avg(extract(epoch from (drop_time - fulfill_time)) / 60) as avg
              FROM "Order"
             WHERE d_uid = %s

        """

        # makeing the query
        q = cur.mogrify(template, (driver_id, ))
        print("executing: " + q.decode("utf-8"))
        print()
        cur.execute(q)

        # getting and printing the results
        rows = cur.fetchall()
        print("Here is the average delivery time (in minutes) for driver %s:" %driver_id)
        for avg in rows:
            print(avg[0])
    finally:
        # safely close connection to database
        if cur != None:
            cur.close()
        if conn != None:
            conn.close()

average_delivery_time(8)
