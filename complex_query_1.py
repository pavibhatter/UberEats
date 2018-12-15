
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

def view_items(vendor_name):
    # try statement to ensure properly closing connection
    try:
        # explanation of goal
        print("User Story: View the items on the menu of the restaurant the user chooses")

        # explanation of how we will demonstrate the goal, along with any hardcoded values
        print("To realize this, the query will show the name, price, and decription of all of the menu items offered by the vendor the user chooses")
        print()

        # the query template
        template = """
            SELECT m.name, m.price, m.description
              FROM menu_item as m JOIN Users as v ON m.v_uid = v.uid
             WHERE v.name ILIKE %s
             ORDER BY name ASC

        """

        # makeing the query
        q = cur.mogrify(template, ("%" + vendor_name + "%",))
        print("executing: " + q.decode("utf-8"))
        print()
        cur.execute(q)

        # getting and printing the results
        rows = cur.fetchall()
        print("Here are all the resulting menu items for the restaurants whose names contain %s:" %vendor_name)
        print()
        for (name, price, description) in rows:
            print("{0}\t${1:.{2}f}\tDescription: {3}".format(name, price / 100, 2, description))

    finally:
        # safely close connection to database
        if cur != None:
            cur.close()
        if conn != None:
            conn.close()

view_items('Piada')


