import sqlite3
import re


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


    def make_reservaton(self):
        m = Cinema()
        conn = sqlite3.connect("cinema_database.db")
        cursor = conn.cursor()

        name = input("Step 1 (User): Choose name>")
        number_of_tickets = input("Step 1 (User): Choose number of tickets>")
        print("\nCurrent movies:")


        m.show_movies()
        print()

        movie_id = input("Step 2 (Movie): Choose a movie>")
        movie_name = cursor.execute('''SELECT name
                                       FROM movies
                                       WHERE movies_id = ?''', (movie_id))
        for row in movie_name:
            name_of_the_movie = row[0]
        print("Projection for movie \'" + name_of_the_movie + "\':")


        m.show_movies_projections(movie_id)
        print()

        projection_id = input("Step 3 (Projection): Choose a projection>")
        print("Available seats (marked with a dot):")

        taken_seats = cursor.execute('''SELECT row, col
                                        FROM reservations
                                        WHERE projection_id = ?''', (projection_id))

        hall = [[ ".  " for x in range(11)] for x in range(11)]
        for i in range(0, 11):
            if i < 10:
                hall[i][0] = str(i) + "   "
            else:
                hall[i][0] = str(i) + "  "
        for i in range(0, 11):
            hall[0][i] = str(i) + "  "

        for seat in taken_seats:
            row = int(seat[0])
            col = int(seat[1])
            hall[row][col] = "X  "

        for i,row in enumerate(hall):
            print(''.join(row))

        counter = 0
        while int(number_of_tickets)> counter:
            choose_seat = (input("Step 4 (Seats): Choose seat %d>"%(counter+1)))
            users_choice = re.findall(r'\d+', choose_seat)
            row_choice = int(users_choice[0])
            col_choice = int(users_choice[1])
            if(row_choice<11 and row_choice>0 and col_choice<11 and col_choice>0):
                if (hall[row_choice][col_choice] == ".  "):
                    new_seat = cursor.execute('''INSERT INTO reservations(username, projection_id, row, col) VALUES(?, ?, ?, ?) ''', (name, projection_id, row_choice, col_choice))

                    counter += 1
                else:
                    print("The plase is taken. Try again!")
            else:
                print("The place is incorrect! Try again!")
        print("This is your reservation:")
        select_movie_name = cursor.execute('''SELECT name, rating
                                              FROM movies
                                              WHERE movies_id = ?''', (movie_id))
        for row in select_movie_name:
            select_name = row[0]
            select_rating = str(row[1])
        print("Movie:\"" + select_name + "\" (" + select_rating + ")")
        # select_date_time = cursor.execute('''SELECT date, time, type
        #                                      FROM projections
        #                                      WHERE proj_id = ? ''', (projection_id))
        # for row in select_date_time:

        # print("Date and Time: " 2014-04-02 19:30 (2D))



        conn.commit()
        conn.close()



    def loop(self):
        c = Cinema()

        while True:
            command = input(">")
            cmd = command.split()
            if cmd[0] == 'show_movies':
                c.show_movies()
                continue
            elif cmd[0] == 'show_movies_projections':
                if (len(cmd)>2):
                    c.show_movies_projections(cmd[1], cmd[2])
                    continue
                else:
                    c.show_movies_projections(cmd[1])
                    continue
            elif cmd[0] == 'mr':
                c.make_reservaton()
                continue
            elif cmd[0] == 'exit':
                break
            else:
                continue

def main():
    new = Cinema()
    new.loop()

if __name__ == '__main__':
    main()
