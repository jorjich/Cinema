import sqlite3


class Cinema():
    """docstring for Cinema"""


    def show_movies(self):

        conn = sqlite3.connect("cinema_database.db")
        cursor = conn.cursor()

        result = cursor.execute('''SELECT name
                                   FROM movies
                                   ORDER BY rating DESC''')

        for i, row in enumerate(result):
            print("{" + str(i+1) + "} -", row[0])

        conn.commit()
        conn.close()


    # def show_movies_projections(self, movie_id, date = 0):


    # def make_reservaton(self):

    def loop(self):
        c = Cinema()
        command = input(">")
        cmd = command

        while True:
            if cmd == 'sh':
                c.show_movies()
                break

def main():
    new = Cinema()
    new.loop()

if __name__ == '__main__':
    main()
