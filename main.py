from filesManipulation.operations import *


def menu():
    read_from_keyboard = ""
    print("Instructiuni:\n"
          "Create <filename> \n"
          "Read <filename> \n"
          "Delete <filename> \n"
          )
    read_from_keyboard = input("Enter:")
    read_from_keyboard = read_from_keyboard.split()
    while read_from_keyboard[0] != "Exit":
        if len(read_from_keyboard) == 2:
            file = read_from_keyboard[1]
            if read_from_keyboard[0] == "Create":
                create_file(file)
            if read_from_keyboard[0] == "Read":
                read_file(file)
            if read_from_keyboard[0] == "Delete":
                print("Delete ", file)
        else:
            print("Comanda nu este corecta")
        read_from_keyboard = input("Enter:")
        read_from_keyboard = read_from_keyboard.split()


def main():

    # create_file("rares2.txt")
    menu()
    #read_file("rares2.txt")



if __name__ == "__main__":
    main()
