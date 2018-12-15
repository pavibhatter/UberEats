\i initialize.sql

\echo "Showing table Food_Item"
\echo notes:
\echo * item_id - the item_id of each menu item which is a food item
SELECT * FROM Food_Item;

\echo "Showing table Drink_Item"
\echo notes:
\echo * item_id - the item_id of each menu item which is a drink item
\echo * volume - the volume (in fluid ounces) of the drink item
SELECT * FROM Drink_Item;

\echo "Showing table Menu_Item"
\echo notes:
\echo * item_id - the id which uniquely identifies the menu item
\echo * price - the price (in US cents) of the menu item
\echo * name - the name of the menu item
\echo * description - a breif description of the item (as it might appear on a menu)
\echo * v_uid - the uid of the Vendor who is selling the menu item
SELECT * FROM Menu_Item;

\echo "Showing table Order"
\echo notes:
\echo * oid - the id which uniquely identifies the order
\echo * drop_location - the address to which the driver should deliver the order
\echo * fulfill_time - (possibly null) the time at which the vendor finishes preparing the order
\echo * pick_up_time - (possibly null) the time at which the driver picks up the order from the vendor
\echo * drop_time - (possibly null) the time at which the driver delivers the order to the drop_location
\echo * order_time - the time at which the order was placed
\echo * c_uid - the uid of the customer who placed the order
\echo * d_uid - (possibly null) the uid of the driver who has claimed the task of delivering the order
\echo * item_id - the item_id of the menu item that was ordered by the customer
SELECT * FROM "Order";

\echo "Showing table Vendor"
\echo notes:
\echo * uid - the uid of the user (who is a vendor)
\echo * open_time - the time of day at which the vendor begins accepting online orders
\echo * close_time - the time of day at which the vendor stops accetoping online orders
SELECT * FROM Vendor;

\echo "Showing table Driver"
\echo notes:
\echo * uid - the uid of the user (who is a driver)
\echo * license_plate - the lisence plate number of the driver
SELECT * FROM Driver;

\echo "Showing table Customer"
\echo notes:
\echo * uid of the user (who is a customer)
SELECT * FROM Customer;

\echo "Showing table Users"
\echo notes:
\echo * uid - the id which uniquely identifies the user (who could be a customer, driver, or vendor)
\echo * name - the name of the user
\echo * address - the address of the user
SELECT * FROM Users;
