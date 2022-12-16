from filesManipulation.operations import *


def check_file(file_name):
    """
    Function used for checking if a file name already exists in ecriptedfiles folder
    :param str file_name: The name of the file we want to check
    :return bool: true or false
    """
    for dirs, root, files in os.walk("D:\\facultate\\Anul 3\\Semestrul 1\\Python\\Proiect\\encriptedfiles"):
        for file in files:
            if file_name == file:
                return False
    return True


def menu():
    """
    Function that implements a menu for this application.
    """
    print("Instructiuni:\n"
          "Create <filename> \n"
          "Read <filename> \n"
          "Delete <filename> \n"
          "Update <filename> \n"
          "Exit for stop \n"
          )
    read_from_keyboard = input("Enter:")
    read_from_keyboard = read_from_keyboard.split()
    while read_from_keyboard[0] != "Exit":
        if len(read_from_keyboard) == 2:
            file = read_from_keyboard[1]
            if read_from_keyboard[0] == "Create":
                if check_file(file):
                    create_file(file)
                else:
                    print("File already exists\n")
            elif read_from_keyboard[0] == "Read":
                if not check_file(file):
                    read_file(file)
                else:
                    print("File doesn't exists. Create first\n")
            elif read_from_keyboard[0] == "Delete":
                if not check_file(file):
                    delete_file(file)
                else:
                    print("File doesn't exists. Create first\n")
            elif read_from_keyboard[0] == "Update":
                if not check_file(file):
                    change_security_for_file(file)
                else:
                    print("File doesn't exists. Create first\n")
            else:
                print("Comanda nu este coreta")
        else:
            print("Comanda nu este corecta")
        read_from_keyboard = input("Enter:")
        read_from_keyboard = read_from_keyboard.split()


def main():
    menu()


if __name__ == "__main__":
    main()
