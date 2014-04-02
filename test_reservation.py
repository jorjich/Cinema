from magic_reservation_system import show_movies, show_movies_projections,make_reservaton
import unittest
import os


def create_tables(cursor):
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



def insert_into_movies(item, cursor):
    movies_id = item["movies_id"]
    name = item["name"]
    rating = item["rating"]

    query = '''INSERT INTO movies(movies_id, name, rating) VALUES(?, ?, ?) '''
    cursor.execute(query, (movies_id, name, rating))

def insert_into_reservations(item, cursor):
    res_id = item["res_id"]
    username = item["username"]
    projection_id = item["projection_id"]
    row = item["row"]
    col = item["col"]

    query = '''INSERT INTO reservations(res_id, username, projection_id, row, col) VALUES(?, ?, ?, ?, ?) '''
    cursor.execute(query, (res_id, username, projection_id, row, col))

def insert_into_projections(item, cursor):
    proj_id = item["proj_id"]
    movie_id = item["movie_id"]
    type = item["type"]
    date = item["date"]
    time = item["time"]

    query = '''INSERT INTO projections(proj_id, movie_id, type, date, time) VALUES(?, ?, ?, ?, ?) '''
    cursor.execute(query, (proj_id, movie_id, type, date, time))

movies = [{
    "movies_id": 1,
    "name": "47 Ronin",
    "rating": 8.5
    }, {
    "movies_id": 2,
    "name": "21",
    "rating": 9
}]

reservations = [{
    "res_id": 1,
    "username": "Ivan Georgiev",
    "projection_id": 1,
    "row": 4,
    "col": 6
    }, {
    "res_id": 2,
    "username": "Georgi Hristov",
    "projection_id": 2,
    "row": 5,
    "col": 9
}]

projections = [{
    "proj_id": 1,
    "movie_id": 1,
    "type": "3D",
    "date": "12-10-2014",
    "time": "14:30"
    }, {
    "proj_id": 2,
    "movie_id": 2,
    "type": "4D",
    "date": "26-12-2014",
    "time": "18:00"
    }
}]



class CinemaTest(unittest.TestCase):

    def setUp(self):
        conn = sqlite3.cursor("test_cinema.db")
        c = conn.cursor()

        create_tables(c)

        for item in movies:
            insert_into_movies(item, c)

        for item in reservations:
            insert_into_reservations(item, c)

        for item in projections:
            insert_into_projections(item, c)

        conn.commit()
        conn.close

    def test_show_movies(self):
        expect = [""]

    def tearDown(self):
        os.remove("test_cinema.db")


if __name__ == '__main__':
    unittest.main()
