
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

def view_popular_items(vendor_id):
    # try statement to ensure properly closing connection
    try:
        # explanation of goal
        print("User Story: Sort the items on my menu by popularity")

        # explanation of how we will demonstrate the goal, along with any hardcoded values
        print("To realize this, we will show the names and number of orders of the menu items for vendor %i, sorted by number of orders." % vendor_id)
        print()

        # the query template
        template = """
            SELECT m.name, COUNT(o.oid)
              FROM menu_item AS m
                   JOIN "Order" as o ON m.item_id = o.item_id
             WHERE m.v_uid = %s
             GROUP BY m.item_id, m.name
             ORDER BY COUNT(o.oid) DESC

        """

        # makeing the query
        q = cur.mogrify(template, (vendor_id,))
        print("executing: " + q.decode("utf-8"))
        print()
        cur.execute(q)

        # getting and printing the results
        rows = cur.fetchall()
        print("here are all the results for vendor %s:" % vendor_id)
        for (name, count) in rows:
            print("item: %s\tcount: %i\t" % (name, count))

    finally:
        # safely close connection to database
        if cur != None:
            cur.close()
        if conn != None:
            conn.close()

view_popular_items(13)


