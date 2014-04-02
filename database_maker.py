import sqlite3

def database_creator(cursor):
    cursor.execute('''CREATE TABLE IF NOT EXISTS movies
                        (movies_id INTEGER PRIMARY KEY,
                        name TEXT,
                        rating REAL)''')

    cursor.execute('''CREATE TABLE IF NOT EXISTS projections
                        (proj_id INTEGER PRIMARY KEY,
                        movie_id INTEGER,
                        type TEXT,
                        date TEXT,
                        time TEXT,
                        FOREIGN KEY(movie_id) REFERENCES movies(movies_id))''')

    cursor.execute('''CREATE TABLE IF NOT EXISTS reservations
                        (res_id INTEGER PRIMARY KEY,
                        username TEXT,
                        projection_id INTEGER,
                        row INTEGER,
                        col INTEGER,
                        FOREIGN KEY(projection_id) REFERENCES projections(proj_id) )''')

def main():

    conn = sqlite3.connect("cinema_database.db")
    c = conn.cursor()
    database_creator(c)

if __name__ == '__main__':
    main()
