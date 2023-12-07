from home import Home
from payment import Payment
from mpass import Mpass

import json
import csv

home = Home()
payment = Payment()
mpass = Mpass()

# # if you not pay, the seat will not be reserved
with open("total_seat.csv", "r") as f:
    csv_reader = csv.reader(f)
    data = list(csv_reader)

with open("seat.csv", "w") as f:
    csv_writer = csv.writer(f)
    csv_writer.writerows(data)

while True:
    # select choice
    print("_____Welcome to Movie Film Hub_____")
    print("1.-MOVIES-")
    print("2.-PAYMENT/PROMOTION-")  # check promotion
    print("3.-MPASS-")  # register
    print("4.-EXIT-")
    # function show menu

    while True:
        try:
            menu = int(input("Select: "))
            if menu in [1, 2, 3, 4]:
                break
            else:
                print("Please enter a valid answer.")
        except ValueError:
            print("Please enter a number.")

    if menu == 1:
        check = False
        while True:
            print(" ")
            home.moviename()
            movie = input("Enter name of movie or Payment: ").upper()
            dict, time = home.seat(movie)

            if movie == "PAYMENT":
                pay = payment.select_payment()
                if pay == "MPASS":
                    while True:
                        mail, phone = mpass.login()

                        with open("member.json", "r") as data:

                            data_file = json.load(data)
                            for i, j in data_file.items():
                                print(i, j)
                                if mail in j and phone == j[mail]:
                                    print("Login successful.")
                                    print(" ")
                                    payment.total_ticket(dict, time, pay)
                                    exit()
                            else:
                                print("Login failed.")
                                print("Please, try again.")
                                print(" ")
                                choice = input(
                                    "Do you want to try again?(Y/N): ").upper()
                                while choice != "Y" and choice != "N":
                                    print("Please enter Y(es) or N(o).")
                                    choice = input(
                                        "Do you want to try again?(Y/N): ").upper()

                                if choice == "N":
                                    break


                elif pay == "PROMO CODE":
                    with open("name.txt", "r") as data:
                        data_file = data.read().splitlines()
                        while True:
                            promo = input("Enter your promo code: ").upper()
                            if promo in data_file:
                                print("Promo code successful.")
                                print(" ")
                                payment.ticket(dict, time)
                                exit()

                            else:
                                print("Promo code not found.")
                                print("Please, try again.")
                                print(" ")

                elif pay != "MPASS" and pay != "PROMO CODE":
                    payment.total_ticket(dict, time, pay)
                    exit()

            else:
                for i, j in dict.items():
                    print(
                        f"Name: {i} {len(j)} seat(s) selected successful.")

    elif menu == 2:
        payment.show_payment()

    elif menu == 3:
        mpass.register()

    elif menu == 4:
        exit()
