CREATE TABLE IF NOT EXISTS region_bounding_box(
    region_id TEXT PRIMARY KEY,
    region_name TEXT,
    min_latitude REAL,
    min_longitude REAL,
    max_latitude REAL,
    max_longitude REAL
);

CREATE TABLE IF NOT EXISTS booking_distance(
    id INTEGER PRIMARY KEY,
    region_id TEXT,
    from_0_1 INTEGER,
    from_1_2 INTEGER,
    from_2_3 INTEGER,
    from_3_4 INTEGER
);
