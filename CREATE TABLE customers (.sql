CREATE TABLE customers (
    cust_id SERIAL PRIMARY KEY,
    cust_name VARCHAR(50) NOT NULL,
    cust_mid_name VARCHAR(50),
    cust_last_name VARCHAR(50) NOT NULL,
    cust_addr1 VARCHAR(50) NOT NULL,
    cust_addr2 VARCHAR(50),
    cust_city VARCHAR(30) NOT NULL,
    cust_postcode CHAR(8) NOT NULL,
    cust_email VARCHAR(150) NOT NULL,
    cust_phone VARCHAR(15) NOT NULL
);

CREATE TABLE playlists (
    playlist_id SERIAL PRIMARY KEY,
    cust_id INT NOT NULL REFERENCES customers(cust_id),
    pl_creation_date DATE NOT NULL,
    pl_last_accessed DATE
);

CREATE TABLE song_playlist (
    playlist_id INT NOT NULL REFERENCES playlists(playlist_id),
    song_id INT NOT NULL REFERENCES songs(song_id),
    PRIMARY KEY(playlist_id, song_id)
);

CREATE TABLE songs (
    song_id SERIAL PRIMARY KEY,
    song_name VARCHAR(200) NOT NULL,
    song_artist VARCHAR(250) NOT NULL,
    song_length INTERVAL NOT NULL,
    song_year DATE
);