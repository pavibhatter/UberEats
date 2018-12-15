-- Created by Vertabelo (http://vertabelo.com)
-- Last modification date: 2018-11-28 02:49:48.711

-- tables
-- Table: Customer
CREATE TABLE Customer (
    uid int  NOT NULL,
    CONSTRAINT Customer_pk PRIMARY KEY (uid)
);

-- Table: Drink_Item
CREATE TABLE Drink_Item (
    item_id int  NOT NULL,
    volume int  NOT NULL,
    CONSTRAINT Drink_Item_pk PRIMARY KEY (item_id)
);

-- Table: Driver
CREATE TABLE Driver (
    uid int  NOT NULL,
    license_plate text  NOT NULL,
    CONSTRAINT Driver_pk PRIMARY KEY (uid)
);

-- Table: Food_Item
CREATE TABLE Food_Item (
    item_id int  NOT NULL,
    CONSTRAINT Food_Item_pk PRIMARY KEY (item_id)
);

-- Table: Menu_Item
CREATE TABLE Menu_Item (
    item_id serial  NOT NULL,
    price int  NOT NULL,
    name text  NOT NULL,
    description text  NOT NULL,
    v_uid int  NOT NULL,
    CONSTRAINT Menu_Item_pk PRIMARY KEY (item_id)
);

-- Table: Order
CREATE TABLE "Order" (
    oid serial  NOT NULL,
    drop_location text  NOT NULL,
    fulfill_time timestamp  NULL,
    pick_up_time timestamp  NULL,
    drop_time timestamp  NULL,
    order_time timestamp  NOT NULL,
    c_uid int  NOT NULL,
    d_uid int  NULL,
    item_id int  NOT NULL,
    CONSTRAINT Order_pk PRIMARY KEY (oid)
);

-- Table: Users
CREATE TABLE Users (
    uid serial  NOT NULL,
    name text  NOT NULL,
    address text  NOT NULL,
    CONSTRAINT Users_pk PRIMARY KEY (uid)
);

-- Table: Vendor
CREATE TABLE Vendor (
    uid int  NOT NULL,
    open_time time  NOT NULL,
    close_time time  NOT NULL,
    CONSTRAINT Vendor_pk PRIMARY KEY (uid)
);

-- foreign keys
-- Reference: Drink_Item_Menu_Item (table: Drink_Item)
ALTER TABLE Drink_Item ADD CONSTRAINT Drink_Item_Menu_Item
    FOREIGN KEY (item_id)
    REFERENCES Menu_Item (item_id)  
    NOT DEFERRABLE 
    INITIALLY IMMEDIATE
;

-- Reference: Food_Item_Menu_Item (table: Food_Item)
ALTER TABLE Food_Item ADD CONSTRAINT Food_Item_Menu_Item
    FOREIGN KEY (item_id)
    REFERENCES Menu_Item (item_id)  
    NOT DEFERRABLE 
    INITIALLY IMMEDIATE
;

-- Reference: Menu_Item_Order (table: Order)
ALTER TABLE "Order" ADD CONSTRAINT Menu_Item_Order
    FOREIGN KEY (item_id)
    REFERENCES Menu_Item (item_id)  
    NOT DEFERRABLE 
    INITIALLY IMMEDIATE
;

-- Reference: Menu_Item_Vendor (table: Menu_Item)
ALTER TABLE Menu_Item ADD CONSTRAINT Menu_Item_Vendor
    FOREIGN KEY (v_uid)
    REFERENCES Vendor (uid)  
    NOT DEFERRABLE 
    INITIALLY IMMEDIATE
;

-- Reference: Order_Customer (table: Order)
ALTER TABLE "Order" ADD CONSTRAINT Order_Customer
    FOREIGN KEY (c_uid)
    REFERENCES Customer (uid)  
    NOT DEFERRABLE 
    INITIALLY IMMEDIATE
;

-- Reference: Order_Driver (table: Order)
ALTER TABLE "Order" ADD CONSTRAINT Order_Driver
    FOREIGN KEY (d_uid)
    REFERENCES Driver (uid)  
    NOT DEFERRABLE 
    INITIALLY IMMEDIATE
;

-- Reference: Users_Customer (table: Customer)
ALTER TABLE Customer ADD CONSTRAINT Users_Customer
    FOREIGN KEY (uid)
    REFERENCES Users (uid)  
    NOT DEFERRABLE 
    INITIALLY IMMEDIATE
;

-- Reference: Users_Driver (table: Driver)
ALTER TABLE Driver ADD CONSTRAINT Users_Driver
    FOREIGN KEY (uid)
    REFERENCES Users (uid)  
    NOT DEFERRABLE 
    INITIALLY IMMEDIATE
;

-- Reference: Users_Vendor (table: Vendor)
ALTER TABLE Vendor ADD CONSTRAINT Users_Vendor
    FOREIGN KEY (uid)
    REFERENCES Users (uid)  
    NOT DEFERRABLE 
    INITIALLY IMMEDIATE
;

-- End of file.

