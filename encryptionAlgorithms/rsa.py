import math
import random


# Miller-Rabbin primality test
def isPrime(n):
    """
dsakdjshakdjsahkjh
    :param n: numarul pe care il verificam daca este prim
    :return:
    """
    n = int(n)
    b = 0
    if n <= 3 or n % 2 == 0:
        return False
    u = n - 1
    k = 0
    while u % 2 == 0:
        u = u // 2
        k += 1

    for trials in range(5):
        a = random.randint(2, n - 1)
        # b = a ^ u mod n
        b = pow(a, u, n)
        if b != 1:
            i = 0
            while b != n - 1:
                if i == k - 1:
                    return False
                else:
                    i += 1
                    b = (b ** 2) % n
    return True


# Generam 2 numere prime pe 512 biti p si q ( RSA 1024 ) si calculam prodului lor n=p*q
# cheia publica e(prima valoare la return): numar random pe max 32 biti prim cu (p-1)(q-1)
# cheia privata d este e^(-1) mod (p-1)(q-1)
def generate_parameters():
    ok = 0
    first_number = 0
    second_number = 0
    pk = 0
    sk = 0
    while first_number == 0:
        p = random.getrandbits(512)
        if isPrime(p) == True:
            first_number = p
    while second_number == 0:
        q = random.getrandbits(512)
        if isPrime(q) == True:
            second_number = q

    n = p * q
    coprime = (p - 1) * (q - 1)
    ok = 0
    while ok == 0:
        pk = random.randrange(1, 4294967295)
        if math.gcd(coprime, pk) == 1:
            ok = 1
    sk = pow(pk, -1, coprime)
    return pk, sk, n


def rsa(message, mode, pk, sk, n):
    if mode == "encrypt":
        number = 0
        for c in message:
            if len(str(ord(c))) == 2:
                number = number * 100
                number = number + ord(c)
            if len(str(ord(c))) == 3:
                number = number * 1000
                number = number + ord(c)
            if len(str(ord(c))) == 1:
                number = number * 10
                number = number + ord(c)

        cripted_message = pow(int(number), pk, n)

        ascii_cripted_message = ""
        ok = 0
        if len(str(cripted_message)) % 2 == 1:
            cripted_message = str(cripted_message)
            cripted_message += '0'
            ok = 1
        cripted_message = str(cripted_message)
        for i in range(0, len(cripted_message), 2):
            ascii_cripted_message += chr(int(cripted_message[i:i + 2]))
        if ok == 1:
            ascii_cripted_message += "-1"
        return ascii_cripted_message
    elif mode == "decrypt":
        decript_number = 0
        ok = 0
        message = str(message)
        if message.__contains__("-1"):
            ok = 1
            message = message[0:len(message) - 2]
        for i in message:
            decript_number *= 100;
            decript_number += ord(i)
        if ok == 1:
            decript_number = str(decript_number)
            decript_number = decript_number[0:len(decript_number) - 1]
            decript_number = int(decript_number)
        decripted_message = pow(int(decript_number), sk, n)
        decripted_message = str(decripted_message)

        decripted_string = ""
        i = 0
        while i < len(decripted_message):
            add = 2
            current_value = int(decripted_message[i:i + 2])
            if current_value < 26:
                current_value = int(decripted_message[i:i + 3])
                add = 3
            decripted_string += chr(current_value)
            i += add
        return decripted_string
