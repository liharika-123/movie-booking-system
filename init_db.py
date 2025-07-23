import sqlite3

conn = sqlite3.connect('movie_booking.db')
cursor = conn.cursor()

cursor.execute('''
CREATE TABLE IF NOT EXISTS movies (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    title TEXT NOT NULL,
    date TEXT NOT NULL,
    time TEXT NOT NULL,
    seats_available INTEGER NOT NULL
)
''')

cursor.execute('''
CREATE TABLE IF NOT EXISTS bookings (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT NOT NULL,
    movie_id INTEGER NOT NULL,
    seat_count INTEGER NOT NULL,
    FOREIGN KEY(movie_id) REFERENCES movies(id)
)
''')

cursor.execute("INSERT INTO movies (title, date, time, seats_available) VALUES ('Avengers: Endgame', '2025-08-01', '18:00', 50)")
cursor.execute("INSERT INTO movies (title, date, time, seats_available) VALUES ('Inception', '2025-08-02', '20:00', 40)")
cursor.execute("INSERT INTO movies (title, date, time, seats_available) VALUES ('Interstellar', '2025-08-03', '17:00', 30)")

conn.commit()
conn.close()

print("Database initialized with sample movies.")
