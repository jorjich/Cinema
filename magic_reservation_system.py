import sqlite3


class Cinema():
    """docstring for Cinema"""


    def show_movies(self):

        conn = sqlite3.connect("cinema_database.db")
        cursor = conn.cursor()

        result = cursor.execute('''SELECT name, rating
                                   FROM movies
                                   ORDER BY rating DESC''')

        for i, row in enumerate(result):
            print("{" + str(i+1) + "} - \"" + row[0] + "\"" + " (" + str(row[1]) + ")")

        conn.commit()
        conn.close()


    def show_movies_projections(self, movie_id, date = 0):
        conn = sqlite3.connect("cinema_database.db")
        cursor = conn.cursor()

        movie_ids = cursor.execute('''SELECT COUNT (movies_id)
                                        FROM movies''')
        for row in movie_ids:
            movie_count = row[0]
        movie_id_parsed = int(movie_id)
        if movie_id_parsed > movie_count or movie_id_parsed < 1:
            print ("There is now such movie!")
        else:
            if date == 0:
                result = cursor.execute('''SELECT proj_id, date, time, type
                                            FROM projections
                                            WHERE movie_id = ?''', (movie_id) )

                for row in result:
                    print("[" + str(row[0]) + "] - " + row[1] + " " + row[2] + " (" + row[3] + ")")
            else:
                result = cursor.execute('''SELECT proj_id, time, type
                                            FROM projections
                                            WHERE movie_id = ? and
                                            date = ?''', (movie_id, date) )

                for row in result:
                    print("[" + str(row[0]) + "] - " + row[1] + " (" + row[2] + ")")


    # def make_reservaton(self):

    def loop(self):
        c = Cinema()

        while True:
            command = input(">")
            cmd = command.split()
            if cmd[0] == 'sh':
                c.show_movies()
                continue
            if cmd[0] == 'sp':
                if (len(cmd)>2):
                    c.show_movies_projections(cmd[1], cmd[2])
                    continue
                else:
                    c.show_movies_projections(cmd[1])
                    continue
            if cmd[0] == 'exit':
                break

def main():
    new = Cinema()
    new.loop()

if __name__ == '__main__':
    main()
