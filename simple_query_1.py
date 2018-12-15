# needed import
import psycopg2
import datetime

# connect to the database
try:
    db = "ubereats"
    user = "isdb"
    conn = psycopg2.connect(database=db, user=user)
    conn.autocommit = True
    cur = conn.cursor()
except psycopg2.Error as e:
    print("Unable to open connection: %s" % (e,))

def place_order(location, customer_id, item_id):
    # try statement to ensure properly closing connection
    try:
        # explanation of goal
        print("User Story: Place an order for the vendor and menu item the user chooses, from a specific vendor")

        # explanation of how we will demonstrate the goal, along with any hardcoded values
        print("To realize this, insert an order with sample values and then show that the order table has been updated.")
        print()

        current_time = datetime.datetime.now()
        # the query template
        template = """
            INSERT INTO "Order"(order_time, drop_location, c_uid, item_id)
                VALUES (current_timestamp, %s, %s, %s);
        """

        # making the query
        q = cur.mogrify(template, (location, customer_id, item_id))
        print("executing: " + q.decode("utf-8"))
        print()
        cur.execute(q)
        print("Done. Now I will select the newly placed order to prove it exists")

        # the query template
        template = """
            SELECT *
              FROM "Order"
             WHERE drop_location = %s
               AND c_uid = %s
               AND item_id = %s
        """

        # making the query
        q = cur.mogrify(template, (location, customer_id, item_id))
        print("executing: " + q.decode("utf-8"))
        print()
        cur.execute(q)

        # getting and printing the results
        rows = cur.fetchall()
        print("Here are all the orders, you can verify that your order is in there:")
        for (oid, drop_location, fulfill_time, pick_up_time, drop_time,order_time, c_uid, d_uid, item_id) in rows:
            print("oid: %i drop_location: %s fulfill_time: %s pick_up_time: %s drop_time: %s order_time: %s c_uid: %i d_uid: %s item_id: %i" % (oid, drop_location, fulfill_time, pick_up_time, drop_time,order_time, c_uid, d_uid, item_id))
            print("You can see that the fulfill time is now the current time: %s" % fulfill_time)
    finally:
        # safely close connection to database
        if cur != None:
            cur.close()
        if conn != None:
            conn.close()


place_order("5000 Forbes Ave, Pittsburgh, PA 15213", 5, 10)

