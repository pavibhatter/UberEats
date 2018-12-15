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

def view_unfulfilled_orders(vendor_id):
    # try statement to ensure properly closing connection
    try:
        # explanation of goal
        print("User Story: A vendor should be able to view the orders customers placed for my restaurant that have not been fulfilled yet")

        # explanation of how we will demonstrate the goal, along with any hardcoded values
        print("To realize this, the query will output all the orders for the vendors id which have not been fulfilled yet")
        print()

        # the query template
        template = """
            SELECT o.oid, o.order_time, o.c_uid, o.d_uid, o.item_id
              FROM "Order" as o JOIN Menu_Item as m ON o.item_id = m.item_id
             WHERE  m.v_uid = %s and (o.fulfill_time IS NULL);
        """

        # makeing the query
        q = cur.mogrify(template, (vendor_id,))
        print("executing: " + q.decode("utf-8"))
        print()
        cur.execute(q)

        # getting and printing the results
        rows = cur.fetchall()
        print("here are the details of the orders for your restaurant that are not yet fulfilled:")
        for (oid, order_time, c_uid, d_uid, item_id) in rows:
            print("order id: %i\t time placed: %s\tcustomer id: %i\tdriver id: %i\titem id: %i" % (oid, order_time, c_uid, d_uid, item_id))
    finally:
        # safely close connection to database
        if cur != None:
            cur.close()
        if conn != None:
            conn.close()

view_unfulfilled_orders(12)
