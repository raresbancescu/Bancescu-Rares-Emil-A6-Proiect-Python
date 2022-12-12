import os
import string
import subprocess
from encryptionAlgorithms.rsa import rsa, generate_parameters
from encryptionAlgorithms.des import encrypt, decript, binary_to_text, text_to_binary
from random import choice
from string import ascii_lowercase
from encryptionAlgorithms.des import encrypt, decript
from databaseOperations.database import *


def write_in_file(file_path, message):
    try:
        message = message.encode()
        file_descriptor = open(file_path, "wb")
        file_descriptor.write(message)
        file_descriptor.close()
    except Exception as e:
        print(e)


def read_from_file(file_path):
    try:
        file_descriptor = open(file_path, "rb")
        message = file_descriptor.read()
        message = message.decode()
        return message
    except Exception as e:
        print(e)


def generate_paths():
    paths = []
    for dirs, root, files in os.walk(r"D:\\facultate\\Anul 3\\Semestrul 1\\Python\\Proiect\\secretdata"):
        for file in files:
            paths.append(os.path.abspath(os.path.join(dirs, file)))
    print(paths)
    secret_path = r'D:/facultate/Anul 3/Semestrul 1/Python/Proiect/secretdata'
    pk_name = "".join(choice(string.ascii_lowercase) for i in range(10))
    pk_name = secret_path + "/" + pk_name
    while pk_name in paths:
        pk_name = "".join(choice(string.ascii_lowercase) for i in range(10))
        pk_name = secret_path + "/" + pk_name
    pk_name += ".key"
    paths.append(pk_name)

    sk_name = "".join(choice(string.ascii_lowercase) for i in range(10))
    sk_name = secret_path + "/" + sk_name
    while sk_name in paths:
        sk_name = "".join(choice(string.ascii_lowercase) for i in range(10))
        sk_name = secret_path + "/" + sk_name
    sk_name += ".key"
    paths.append(sk_name)

    key_name = "".join(choice(string.ascii_lowercase) for i in range(10))
    key_name = secret_path + "/" + key_name
    while key_name in paths:
        key_name = "".join(choice(string.ascii_lowercase) for i in range(10))
        key_name = secret_path + "/" + key_name
    key_name += ".key"
    paths.append(key_name)

    return pk_name, sk_name, key_name


def create_file(file_name):
    file_path = r"D:/facultate/Anul 3/Semestrul 1/Python/Proiect/encriptedfiles"
    file_path += "/" + file_name
    try:
        file_descriptor = open(file_path, "w")
        file_descriptor.close()
        subprocess.call(["notepad.exe", file_path])
        while not file_descriptor.closed:
            os.wait()
        file_descriptor = open(file_path, "rb")
        text_from_file = file_descriptor.read()
        print(text_from_file)
        file_descriptor.close()
        os.remove(file_path)
        # encription part
        (pk, sk, n) = generate_parameters()
        # generate a random key for des
        key = "".join(choice(string.ascii_lowercase) for i in range(6))
        encrypted_key = rsa(key, "encrypt", pk, 0, n)
        encrypted_text = encrypt(text_from_file, key)
        encrypted_text = binary_to_text(encrypted_text)
        public_key = str(str(pk) + "\n" + str(n))
        secret_key = str(str(sk) + "\n" + str(n))
        (pk_path, sk_path, key_path) = generate_paths()

        write_in_file(pk_path, public_key)
        write_in_file(sk_path, secret_key)
        write_in_file(key_path, encrypted_key)
        write_in_file(file_path, encrypted_text)
        file_path
        query = "insert into files values (\'%s\',\'%s\',\'%s\',\'%s\',\'%s\')" % (
            file_name, file_path, pk_path, sk_path, key_path)
        print(query)
        database_update(query)
    except Exception as e:
        print(e)


def read_file(file_name):
    query = "select * from files where filename='%s'" % file_name
    result = database_select(query)
    result = result[0]
    paths = list()
    for res in result:
        res = str(res)
        res = res.replace("/", "\\")
        paths.append(res)

    encripted_key = read_from_file(paths[4])
    private_key = read_from_file(paths[3])
    public_key = read_from_file(paths[2])
    text = read_from_file(paths[1])
    private_key = private_key.split("\n")
    public_key = public_key.split("\n")
    sk = int(private_key[0])
    n = int(private_key[1])
    pk = int(public_key[0])
    n = int(public_key[1])
    key = rsa(encripted_key, "decrypt", 0, sk, n)
    text = text_to_binary(text)
    message = decript(text, key)
    message = binary_to_text(message)
    # write the message back in file
    message = str(message)
    message=message[2:]
    message=message[:len(message)-2]
    print(message)
    file_descriptor = open(paths[1], "w+")
    i = 0
    while i < len(message):
        print(message[i])
        if message[i] != '\\':
            file_descriptor.write(message[i])
            i = i + 1
        else:
            if message[i] == '\\' and message[i + 1] != 'r' and message[i + 1] != 'n' and message[i + 1] != 't':
                file_descriptor.write(message[i])
                i = i + 1
            else:
                if message[i + 1] == 'n':
                    file_descriptor.write(chr(10))
                elif message[i + 1] == 't':
                    file_descriptor.write(chr(9))
                else:
                    file_descriptor.write("")
                i = i + 2
    file_descriptor.close()
    subprocess.call(["notepad.exe", paths[1]])
    while not file_descriptor.closed:
        os.wait()

    #read from file,encrypt again,write back in file


# def example():
#     try:
#         file_descriptor = open(r"D:\facultate\Anul 3\Semestrul 1\Python\Proiect\rares.txt", "wb")
#         #scriem in fisierul asta
#         file_descriptor.close()
#         program_name = "notepad.exe"
#         subprocess.call([program_name,r"D:\facultate\Anul 3\Semestrul 1\Python\Proiect\rares.txt"])
#         while not file_descriptor.closed:
#             os.wait()
#         file_descriptor = open(r"D:\facultate\Anul 3\Semestrul 1\Python\Proiect\rares.txt", "r")
#         text = file_descriptor.read()
#         print(text)
#         file_descriptor.close()
#         os.remove(r"D:\facultate\Anul 3\Semestrul 1\Python\Proiect\rares.txt")
#         file_descriptor.close()
#     except Exception as e:
#         print(e)
