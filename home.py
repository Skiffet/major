import csv


class Home:
    def __init__(self):
        """TODO: Wtite a comment docstring comment in each function"""
        self.__lit_of_seat = {}
        self.__time = []

    def moviename(self):
        number = 0
        with open("seat.csv") as f:
            data = csv.reader(f)
            for seat in data:
                number += 1

                print(f"{number}. {seat[0]} (Time: {seat[1]})")
        print("PAYMENT")
        print("EXIT")

    def seat(self, movie):

        with open("seat.csv") as f:
            data = csv.reader(f)
            count = 0
            check = False

            for seat in data:
                if movie == seat[0]:
                    check = True
                    print(" ")
                    print("+---------------------------------------------+")
                    print("|                    Screen                   |")
                    print("+---------+---------+---------+---------+-----+")
                    print(f"|   {seat[2]}   |   {seat[3]}    |   {seat[4]}   |"
                          f"   {seat[5]}   |   {seat[6]}   |")
                    print("+---------+---------+---------+---------+-----+")
                    print(f"|   {seat[7]}   |   {seat[8]}    |   {seat[9]}   |"
                          f"   {seat[10]}   |   {seat[11]}   |")
                    print("+---------+---------+---------+---------+-----+")
                    print(" ")
                    num_seat = []

                    # is_payment = False
                    while True:
                        try:
                            many = int(
                                input("How many seats will you choose: "))

                            if isinstance(many, int):
                                # for if seat not enough to reserve.
                                rs_seats = seat[2:].count("RS")
                                if many <= 10 - rs_seats and many > 0 or many == 0:
                                    break

                                if many < 0:
                                    print("Please enter a positive number.")

                                else:
                                    print("Not enough seats.")
                            else:
                                print("Please enter a valid number of seats.")

                        except ValueError:
                            print("Please enter a number of seats.")

                    # input seat
                    while True:
                        count += 1
                        no_seat = input(f"Please choose your seat{count}: ")
                        if no_seat not in seat or no_seat in num_seat:
                            print("Seat already reserved.")
                            print("Please, try again.")
                            print(" ")
                            count -= 1

                        elif no_seat in seat and no_seat not in num_seat:
                            num_seat.append(no_seat)
                            self.__time.append(seat[1])
                            new_lit = []
                            # delete seat
                            with open("seat.csv", "r") as f:
                                csv_reader = csv.reader(f)
                                for i in csv_reader:
                                    new_lit.append(i)
                            for row in new_lit:
                                if row[0] == movie:
                                    for i in range(len(row)):
                                        if row[i] in no_seat:
                                            row[i] = "RS"  # Reserved seat

                            with open('seat.csv', 'w', newline='') as file:
                                csv_writer = csv.writer(file)
                                for row in new_lit:
                                    csv_writer.writerow(row)
                            # print(num_seat)

                        if len(num_seat) == many:
                            # print(len(num_seat))
                            break




                    # input movie and seat
                    if movie in self.__lit_of_seat:
                        self.__lit_of_seat[movie].extend(num_seat)
                    else:
                        self.__lit_of_seat[movie] = num_seat

            if not check and movie != "PAYMENT" and movie != "EXIT":
                print(f"Movie ({movie}) exist.")  # Change a word

        return self.__lit_of_seat, self.__time

    @property
    def select_seat(self):
        return self.__lit_of_seat

# x = Home()
# x.moviename()
# x.seat("TALK TO ME")
# x.edit_seat()

# x.select_seat()