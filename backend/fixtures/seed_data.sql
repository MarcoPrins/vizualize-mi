CREATE TABLE IF NOT EXISTS region_bounding_box(
    region_id TEXT PRIMARY KEY,
    region_name TEXT,
    min_latitude TEXT,
    min_longitude TEXT,
    max_latitude TEXT,
    max_longitude TEXT
);

CREATE TABLE IF NOT EXISTS booking_distance(
    id INTEGER PRIMARY KEY,
    region_id TEXT,
    from_0_1 INTEGER,
    from_1_2 INTEGER,
    from_2_3 INTEGER,
    from_3_4 INTEGER
);

INSERT INTO region_bounding_box(
    region_id,
    region_name,
    min_latitude,
    min_longitude,
    max_latitude,
    max_longitude
) 
VALUES (
    'de_berlin',
    'Berlin',
    '52.527919', 
    '13.340148', 
    '52.562995', 
    '13.506317'
);

INSERT INTO region_bounding_box(
    region_id,
    region_name,
    min_latitude,
    min_longitude,
    max_latitude,
    max_longitude
) 
VALUES (
    'de_cologne',
    'Cologne',
    '50.908075', 
    '6.857800', 
    '50.977732', 
    '6.949810'
);

INSERT INTO region_bounding_box(
    region_id,
    region_name,
    min_latitude,
    min_longitude,
    max_latitude,
    max_longitude
) 
VALUES (
    'de_munich',
    'Munich',
    '47.998308', 
    '11.063490', 
    '48.437515', 
    '11.898451'
);

INSERT INTO region_bounding_box(
    region_id,
    region_name,
    min_latitude,
    min_longitude,
    max_latitude,
    max_longitude
) 
VALUES (
    'de_munster',
    'Munster',
    '51.810844', 
    '7.334275', 
    '52.342733', 
    '8.267126'
);
