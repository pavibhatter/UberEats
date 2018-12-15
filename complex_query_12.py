
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

def peak_hours(vendor_id):
    # try statement to ensure properly closing connection
    try:
        # explanation of goal
        print("User Story: a vendor wants to know the peak hours when people order their food.")

        # explanation of how we will demonstrate the goal, along with any hardcoded values
        print("To realize this, the query will show all the hours when people order their food and the number of people who ordered in that hours, in descending order of count")
        print()

        # the query template
        template = """
            SELECT EXTRACT(hour FROM o.order_time), COUNT(o.oid)
              FROM "Order" AS o JOIN menu_item AS m ON o.item_id = m.item_id
             WHERE m.v_uid = %s
             GROUP BY EXTRACT(hour FROM o.order_time)
             ORDER BY count DESC
        """

        # makeing the query
        q = cur.mogrify(template, (vendor_id,))
        print("executing: " + q.decode("utf-8"))
        print()
        cur.execute(q)

        # getting and printing the results
        rows = cur.fetchall()
        print("here are the most common hours for vendor %s (military time):" %vendor_id)
        for (hour, count) in rows:
            print("hour: %s:00\t count: %s" % (int(hour), count))

    finally:
        # safely close connection to database
        if cur != None:
            cur.close()
        if conn != None:
            conn.close()

peak_hours(13)

