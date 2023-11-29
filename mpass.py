import json


class Mpass:
    def __init__(self):
        self.__new_user = str
        self.__user = {}
        self.__mail = ""
        self.__phone = ""

    def register(self):
        check = []
        with open("member.json", "r") as data:  # open file
            data_file = json.load(data)
            # print(data_file)
            for i in data_file:
                check.append(i)
                # print(i)
            a = True
            while a:
                print(" ")
                new_user = input("Enter Name: ").upper()
                if new_user not in check:
                    print("Let's get you started!")
                    mail = input("Enter your gmail: ")
                    #if no @gmail u have to add @gmail
                    while True:
                        if "@gmail" not in mail:
                            print("Please enter a Gmail address.")
                            mail = input("Enter your gmail: ")
                        else:
                            break
                    #check number and number must be 10 digits
                    while True:
                        try:
                            phone = int(input("Enter your mobile number 66+: "))
                            if len(str(phone)) == 10:
                                break

                            else:
                                print("Phone number must be 10 digits.")
                        except ValueError:
                            print("Please enter a number.")


                    print("Create Success")
                    print("")
                    self.__user[new_user] = {mail: str(phone)}
                    data_file.update(self.__user)
                    with open('member.json', 'w') as json_file:  # dump file
                        json.dump(data_file, json_file, indent=4)
                    a = False
                else:
                    print("Name already exists.")
                    print("Please, try again.")
                    print(" ")
            return self.__user

    def login(self):
        print("* * * * * * * * * * * * ")
        print(" ")
        print("---------LOGIN---------")
        self.__mail = input("Gmail: ")
        self.__phone = input("Mobile number: ")
        return self.__mail, self.__phone

# x = Mpass()
# x.register()
# x.login()
