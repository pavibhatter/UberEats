
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

def view_unclaimed_orders():
    # try statement to ensure properly closing connection
    try:
        # explanation of goal
        print("User Story: View the details of orders which do not yet have a driver")

        # explanation of how we will demonstrate the goal, along with any hardcoded values
        print("To realize this we will show the order id, drop location, and pickup vendor/location of all of the orders which do not yet have a driver (sorted by time placed)")
        print()

        # the query template
        template = """
            SELECT o.oid, o.drop_location, u.name, u.address
              FROM "Order" AS o
                   JOIN menu_item AS m ON o.item_id = m.item_id
                   JOIN users AS u ON m.v_uid = u.uid
             WHERE o.d_uid IS NULL
             ORDER BY o.order_time
        """

        # makeing the query
        q = cur.mogrify(template)
        print("executing: " + q.decode("utf-8"))
        print()
        cur.execute(q)

        # getting and printing the results
        rows = cur.fetchall()
        print("here are all of the unclaimed orders:")
        for (oid, drop_location, vendor, vendor_address) in rows:
            print("order: %i\tdelivery location: %s\t pickup at: %s - %s" % (oid, drop_location, vendor, vendor_address))

    finally:
        # safely close connection to database
        if cur != None:
            cur.close()
        if conn != None:
            conn.close()

view_unclaimed_orders()

