import json
import csv


# from tabulate import tabulate

def set_seat():  # write file after payment
    with open("seat.csv", "r") as f:
        csv_reader = csv.reader(f)
        data = list(csv_reader)

    with open("total_seat.csv", "w") as f:
        csv_writer = csv.writer(f)

        csv_writer.writerows(data)


class Payment:
    def __init__(self):
        self.__name = ""
        self.__last = ""
        self.__pay = ""

    def show_payment(self):
        head = ["Name", "City"]
        print("+--------------------------------+")
        print(
            f"|{8 * ' ' + 'Name' + ' ' * 7}| {2 * ' ' + 'Percent' + ' ' * 2}|")
        with open("payment.json", "r") as data:
            promo = json.load(data)
            for i, j in promo.items():
                name = i.ljust(18)
                city = str(j).ljust(8)

                print("+--------------------------------+")
                print(f"| {name}|{4 * ' ' + city}|")
        print("+--------------------------------+")
        print(" ")

    def select_payment(self):  # input dict in parameter
        print("-------PAYMENT-------")
        lit = []
        percent = []
        num = 0
        with open("payment.json", "r") as data:
            promo = json.load(data)
            for i, j in promo.items():
                num += 1
                lit.append(i)
                print(f"{num}. {i} ({j}%)")

        print("---------------------")
        print(" ")

        self.__pay = input("Select payment: ").upper()
        while self.__pay not in lit:
            print("Payment not found.")
            print(" ")
            self.__pay = input("Select payment: ").upper()
        return self.__pay

    def ticket(self, dict, time):
        new_lit = []

        with open("seat.csv", "r") as f:
            csv_reader = csv.reader(f)
            for i in csv_reader:
                new_lit.append(i)
        for (key, values), j in zip(dict.items(), time):
            print("-" * 45 + "ARM CINEMA" + "-" * 2)
            print(f"| Branch Ratchayothin      Showtime: {j}              |")
            print(f"| Movie: {key}{' ' * (23 - len(key))}"
                  f"    Date: {'24/06/2023'}    |")
            print(f"| Seat No:", end="")
            for value in values:
                print(f" {value} ,", end="")
            print(f" ")
            print("-" * 30 + "Movie Film Hub" + "-" * 13)
            print(" ")
            set_seat()

    def total_ticket(self, dict, time, pay):
        BAST_TICKET = 200
        total = 0
        percent = ""
        with open("payment.json", "r") as data:
            promo = json.load(data)
        for i, j in promo.items():
            if pay == i:
                print(f"Your Payment is {pay} and discount {j}%")
                percent = j
        for name, seat in dict.items():
            print(f"___{name}___")
            price = (len(seat) * BAST_TICKET) * (int(percent) / 100)
            print(f"Price {len(seat)} seat is {len(seat) * BAST_TICKET} Baht.")
            print(f"Your Discount is {price} Baht.")
            movie_price = (len(seat) * BAST_TICKET) - (price)
            print(f"Movie price {movie_price} Baht.")
            print(" ")
            total += movie_price

        print(f"Total price {total} Baht.")
        print(" ")

        for (key, values), j in zip(dict.items(), time):
            print("-" * 45 + "ARM CINEMA" + "-" * 2)
            print(f"| Branch Ratchayothin      Showtime: {j}              |")
            print(
                f"| Movie: {key}{' ' * (23 - len(key))}"
                f"    Date: {'24/06/2023'}    |")
            print(f"| Seat No:", end="")
            for value in values:
                print(f" {value} ,", end="")
            print(f" ")
            print("-" * 36 + "Movie Film Hub" + "-" * 7)
            print(" ")
            set_seat()

# x = Payment()
# x.show_payment()
# x.select_payment()
# x.ticket({"DORAEMON THE MOVIE 2023":
# ["A1"],"TALK TO ME": ["A1","A2"]},["12.00"])
# x.total_ticket({"DORAEMON THE MOVIE 2023": ["A1"],
# "TALK TO ME": ["A1","A2"]}, ["12.00"], "MPASS")
