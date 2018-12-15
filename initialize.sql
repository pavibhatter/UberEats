
DROP DATABASE IF EXISTS ubereats;
CREATE database ubereats;
\c ubereats
\i create.sql
\copy Users (name, address) FROM 'Users.csv'  delimiter ';'  csv header
\copy Customer (uid) FROM 'Customer.csv'  delimiter ';'  csv header
\copy Driver (uid, license_plate) FROM 'Driver.csv'  delimiter ';'  csv header
\copy Vendor (uid, open_time, close_time) FROM 'Vendor.csv'  delimiter ';'  csv header
\copy Menu_Item(price, name, description, v_uid) FROM 'Menu_Item.csv'  delimiter ';'  csv header
\copy Food_Item(item_id) FROM 'Food_Item.csv'  delimiter ';'  csv header
\copy Drink_Item(item_id, volume) FROM 'Drink_Item.csv'  delimiter ';'  csv header
\copy "Order"(order_time, drop_location, fulfill_time, pick_up_time, drop_time, c_uid, d_uid, item_id) FROM 'Order.csv'  delimiter ';'  csv header


