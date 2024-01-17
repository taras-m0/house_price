CREATE TABLE table_name 
(
    id             INT            NOT NULL,
    property_type  VARCHAR(32)    NOT NULL,
    price          INT            NOT NULL,
    location       VARCHAR(256)   NOT NULL,
    city           VARCHAR(64)    NOT NULL,
    baths          INT            NOT NULL,
    purpose        VARCHAR(64)    NOT NULL,
    bedrooms       INT            NOT NULL,
    Area_in_Marla  NUMERIC(6, 2)  NOT NULL,
    PRIMARY KEY (id)    
);