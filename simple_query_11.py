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

def fulfill_order(order_id):
    # try statement to ensure properly closing connection
    try:
        # explanation of goal
        print("User Story: A vendor should be able to mark an order as fulfilled")

        # explanation of how we will demonstrate the goal, along with any hardcoded values
        print("To realize this, the query will update the fulfillfed time for the order the vendor choses")
        print()

        # the query template
        template = """
            UPDATE "Order"
               SET fulfill_time = current_timestamp
             WHERE oid = %s
        """

        # makeing the query
        q = cur.mogrify(template, (order_id,))
        print("executing: " + q.decode("utf-8"))
        print()
        cur.execute(q)

        # prove success
        print("Done. To show that this is complete we will select the order that was just fulfilled.")

        template = """
            SELECT oid, drop_location, fulfill_time, pick_up_time, drop_time,order_time, c_uid, d_uid, item_id
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
        print("Here are the details of the order you just fulfilled:")
        for (oid, drop_location, fulfill_time, pick_up_time, drop_time,order_time, c_uid, d_uid, item_id) in rows:
            print("oid: %i drop_location: %s fulfill_time: %s pick_up_time: %s drop_time: %s order_time: %s c_uid: %i d_uid: %s item_id: %i" % (oid, drop_location, fulfill_time, pick_up_time, drop_time,order_time, c_uid, d_uid, item_id))
            print("You can see that the fulfill time is now the current time: %s" % fulfill_time)
    finally:
        # safely close connection to database
        if cur != None:
            cur.close()
        if conn != None:
            conn.close()

fulfill_order(4)
