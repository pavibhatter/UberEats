
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

def average_fulfill_time(vendor_id):
    # try statement to ensure properly closing connection
    try:
        # explanation of goal
        print("User Story: A vendor wants to know the average time it takes them to fulfill an order")
        print("To realize this, this query accepts a vendor id and prints their average fulfill time")
        print()

        # the query template
        template = """
            SELECT avg(extract(epoch from (o.fulfill_time - o.order_time)) / 60) as avg
              FROM "Order" AS o
                   JOIN menu_item AS i ON o.item_id = i.item_id
             WHERE i.v_uid = %s

        """

        # makeing the query
        q = cur.mogrify(template, (vendor_id,))
        print("executing: " + q.decode("utf-8"))
        print()
        cur.execute(q)

        # getting and printing the results
        rows = cur.fetchall()
        print("Here is the average fulfill time (in minutes) for vendor %s:" %vendor_id)
        for avg in rows:
            print(avg[0])
    finally:
        # safely close connection to database
        if cur != None:
            cur.close()
        if conn != None:
            conn.close()

average_fulfill_time(14)
