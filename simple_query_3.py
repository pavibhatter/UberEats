
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

def accept_order(driver_id, order_id):
    # try statement to ensure properly closing connection
    try:
        # explanation of goal
        print("User Story: A driver should be able to accept an order")

        # explanation of how we will demonstrate the goal, along with any hardcoded values
        print("To realize this, the query will update the driver_id column for the order the driver choses")
        print()

        # the query template
        template = """
            UPDATE "Order"
               SET d_uid = %s
             WHERE oid = %s
        """

        # makeing the query
        q = cur.mogrify(template, (driver_id, order_id))
        print("executing: " + q.decode("utf-8"))
        print()
        cur.execute(q)

        # prove success
        print("Done. Now I will select the orders belonging to drive %s so that you can see that order %s is there." % (driver_id, order_id))

        # the query template
        template = """
            SELECT oid, order_time, drop_location, fulfill_time, pick_up_time, drop_time, c_uid, d_uid, item_id
              FROM "Order"
             WHERE oid = %s
        """

        # makeing the query
        q = cur.mogrify(template, (order_id,))
        print("executing: " + q.decode("utf-8"))
        print()
        cur.execute(q)

        # getting and printing the results
        rows = cur.fetchall()
        print("here are the details of the order you just accepted:")
        for (oid, order_time, drop_location, fulfill_time, pick_up_time, drop_time, c_uid, d_uid, item_id) in rows:
            print("order id: %i\torder time: %s\tdrop_location: %s\tfulfill time: %s\tpickup time: %s\tdrop_time: %s\tcustomer id: %i\tdriver id: %i\titem_id: %i" % (oid, order_time, drop_location, fulfill_time, pick_up_time, drop_time, c_uid, d_uid, item_id))
    finally:
        # safely close connection to database
        if cur != None:
            cur.close()
        if conn != None:
            conn.close()

accept_order(9,5)
