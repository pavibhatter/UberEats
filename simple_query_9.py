
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

def add_to_menu(price, name, description, vendor_id):
    # try statement to ensure properly closing connection
    try:
        # explanation of goal
        print("User Story: A vendor should be able to add a menu item")
        print("To realize this we will add a menu item with sample values")
        print()

        # the query template
        template = """
            INSERT INTO Menu_Item VALUES(DEFAULT,%s,%s,%s,%s)
        """

        # makeing the query
        q = cur.mogrify(template, (price, name, description,vendor_id))
        print("executing: " + q.decode("utf-8"))
        print()
        cur.execute(q)

        # proving success
        print("Done. Now to demonstrate success we will select the item we just inserted:")

        template = """
            SELECT *
              FROM Menu_Item
             WHERE price = %s
               AND name = %s
               AND description = %s
               AND v_uid = %s
        """

        # makeing the query
        q = cur.mogrify(template, (price, name, description,vendor_id))
        print("executing: " + q.decode("utf-8"))
        print()
        cur.execute(q)

        # getting and printing the results
        rows = cur.fetchall()
        print("Here are the results of the select (if this has been run more than once you will see multiple rows):")
        for row in rows:
            print(row)
    finally:
        # safely close connection to database
        if cur != None:
            cur.close()
        if conn != None:
            conn.close()

add_to_menu(9, "pizza", "Very delicious pizza", 12)
