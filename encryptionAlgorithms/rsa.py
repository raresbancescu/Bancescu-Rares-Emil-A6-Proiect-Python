import math
import random


# Miller-Rabbin primality test
def is_prime(n):
    """
Miller-Rabbin primality test: check is a given number is likely to be prime. We use this primality test because we check
if a number of 512 bits is prime. A non-deterministic algorithm for a number of this size will not be able to compute
the result in a reasonable time
    :param int n: a number that we want to check if it is prime
    :return: True if the number is prime, False otherwise
    """
    n = int(n)
    if n <= 3 or n % 2 == 0:
        return False
    u = n - 1
    k = 0
    # search for u such that n-1=m*2^k
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


def generate_parameters():
    """
This function generate the parameters we need for RSA-Encryption: Public key(pk) and Secret key(sk).
First we generate two prime numbers(512 bits) p and q which are used for computing RSA-1024
n=p*q
e small exponent 1<e<Φ(n) ( Φ(n)=(p-1)(q-1) ) and co-prime to Φ(n)
public key(pk): e,n
secret key(sk) d,n where d= e^-1 mod Φ(n)
    :return: e d n
    """
    first_number = 0
    second_number = 0
    pk = 0
    while first_number == 0:
        p = random.getrandbits(512)
        if is_prime(p):
            first_number = p
    while second_number == 0:
        q = random.getrandbits(512)
        if is_prime(q):
            second_number = q

    n = first_number * second_number
    co_prime = (first_number - 1) * (second_number - 1)
    ok = 0
    while ok == 0:
        pk = random.randrange(1, co_prime)
        if math.gcd(co_prime, pk) == 1:
            ok = 1
    sk = pow(pk, -1, co_prime)
    return pk, sk, n


def rsa(message, mode, pk, sk, n):
    """
The main function of the Rsa encryption algorithm. The message is transformed into a number using ascii encoding
,and we apply the transformation on this number. After that we change back the number to ascii encoding.
We use mode to know if we encrypt or decrypt a message
    :param string message: The message we want to encrypt/decrypt
    :param string mode: "encrypt" for encrypting the message, "decrypt" for decrypting the message
    :param int pk: e from generate_parameters
    :param int sk: d from generate_parameters
    :param int n:  n from generate_parameters
    :return string: encrypted or decrypted message, it depends on mode parameter
    """
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

        encrypted_message = pow(int(number), pk, n)

        ascii_encrypted_message = ""
        ok = 0
        if len(str(encrypted_message)) % 2 == 1:
            encrypted_message = str(encrypted_message)
            encrypted_message += '0'
            ok = 1
        encrypted_message = str(encrypted_message)
        for i in range(0, len(encrypted_message), 2):
            ascii_encrypted_message += chr(int(encrypted_message[i:i + 2]))
        if ok == 1:
            ascii_encrypted_message += "-1"
        return ascii_encrypted_message
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
