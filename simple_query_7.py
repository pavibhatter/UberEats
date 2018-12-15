
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

def update_item(item_id, name=None, price=None, description=None):
    # try statement to ensure properly closing connection
    try:
        # explanation of goal
        print("User Story: Update menu items")

        # explanation of how we will demonstrate the goal, along with any hardcoded values
        print("To realize this, this function accepts an item id, along with keyword args of the other fields to be updated.")
        print()

        # the query template
        template = "UPDATE menu_item SET item_id = %s, "
        vars = [str(item_id)]
        if name != None:
            template += " name = %s, "
            vars.append(str(name))
        if price != None:
            template += " price = %s, "
            vars.append(str(price))
        if description != None:
            template += " description = %s, "
            vars.append(str(description))
        template = template[0:-2]
        template += " WHERE item_id = %s"
        vars.append(str(item_id))

        # makeing the query
        q = cur.mogrify(template, vars)
        print("executing: " + q.decode("utf-8"))
        print()
        cur.execute(q)

        print("Done. Now to validate the change I will select the item and show the fields.")
        template = """
            SELECT item_id, name, price, description
              FROM menu_item
             WHERE item_id = %s
        """

        q = cur.mogrify(template, (item_id,))
        print("executing: " + q.decode("utf-8"))
        print()
        cur.execute(q)

        # getting and printing the results
        rows = cur.fetchall()
        print("So here is the updated menu item: ")
        for (item_id, name, price, description) in rows:
            print("Item ID: {0}\t{1}\t${2:.{3}f}\tDescription: {4}".format(item_id, name, price / 100, 2, description))

    finally:
        # safely close connection to database
        if cur != None:
            cur.close()
        if conn != None:
            conn.close()

update_item(3, price=399, name="Fries", description="they are yummy")


