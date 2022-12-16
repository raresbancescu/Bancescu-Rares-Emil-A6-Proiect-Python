# initial permutation
IP = [58, 50, 42, 34, 26, 18, 10, 2,
      60, 52, 44, 36, 28, 20, 12, 4,
      62, 54, 46, 38, 30, 22, 14, 6,
      64, 56, 48, 40, 32, 24, 16, 8,
      57, 49, 41, 33, 25, 17, 9, 1,
      59, 51, 43, 35, 27, 19, 11, 3,
      61, 53, 45, 37, 29, 21, 13, 5,
      63, 55, 47, 39, 31, 23, 15, 7]

# d-box expansion
RE = [32, 1, 2, 3, 4, 5, 4, 5,
      6, 7, 8, 9, 8, 9, 10, 11,
      12, 13, 12, 13, 14, 15, 16, 17,
      16, 17, 18, 19, 20, 21, 20, 21,
      22, 23, 24, 25, 24, 25, 26, 27,
      28, 29, 28, 29, 30, 31, 32, 1]

# Straight Permutation Table per
box_permutation = [16, 7, 20, 21,
                   29, 12, 28, 17,
                   1, 15, 23, 26,
                   5, 18, 31, 10,
                   2, 8, 24, 14,
                   32, 27, 3, 9,
                   19, 13, 30, 6,
                   22, 11, 4, 25]

# S-box Table
s_box_matrix = [[[14, 4, 13, 1, 2, 15, 11, 8, 3, 10, 6, 12, 5, 9, 0, 7],
                 [0, 15, 7, 4, 14, 2, 13, 1, 10, 6, 12, 11, 9, 5, 3, 8],
                 [4, 1, 14, 8, 13, 6, 2, 11, 15, 12, 9, 7, 3, 10, 5, 0],
                 [15, 12, 8, 2, 4, 9, 1, 7, 5, 11, 3, 14, 10, 0, 6, 13]],

                [[15, 1, 8, 14, 6, 11, 3, 4, 9, 7, 2, 13, 12, 0, 5, 10],
                 [3, 13, 4, 7, 15, 2, 8, 14, 12, 0, 1, 10, 6, 9, 11, 5],
                 [0, 14, 7, 11, 10, 4, 13, 1, 5, 8, 12, 6, 9, 3, 2, 15],
                 [13, 8, 10, 1, 3, 15, 4, 2, 11, 6, 7, 12, 0, 5, 14, 9]],

                [[10, 0, 9, 14, 6, 3, 15, 5, 1, 13, 12, 7, 11, 4, 2, 8],
                 [13, 7, 0, 9, 3, 4, 6, 10, 2, 8, 5, 14, 12, 11, 15, 1],
                 [13, 6, 4, 9, 8, 15, 3, 0, 11, 1, 2, 12, 5, 10, 14, 7],
                 [1, 10, 13, 0, 6, 9, 8, 7, 4, 15, 14, 3, 11, 5, 2, 12]],

                [[7, 13, 14, 3, 0, 6, 9, 10, 1, 2, 8, 5, 11, 12, 4, 15],
                 [13, 8, 11, 5, 6, 15, 0, 3, 4, 7, 2, 12, 1, 10, 14, 9],
                 [10, 6, 9, 0, 12, 11, 7, 13, 15, 1, 3, 14, 5, 2, 8, 4],
                 [3, 15, 0, 6, 10, 1, 13, 8, 9, 4, 5, 11, 12, 7, 2, 14]],

                [[2, 12, 4, 1, 7, 10, 11, 6, 8, 5, 3, 15, 13, 0, 14, 9],
                 [14, 11, 2, 12, 4, 7, 13, 1, 5, 0, 15, 10, 3, 9, 8, 6],
                 [4, 2, 1, 11, 10, 13, 7, 8, 15, 9, 12, 5, 6, 3, 0, 14],
                 [11, 8, 12, 7, 1, 14, 2, 13, 6, 15, 0, 9, 10, 4, 5, 3]],

                [[12, 1, 10, 15, 9, 2, 6, 8, 0, 13, 3, 4, 14, 7, 5, 11],
                 [10, 15, 4, 2, 7, 12, 9, 5, 6, 1, 13, 14, 0, 11, 3, 8],
                 [9, 14, 15, 5, 2, 8, 12, 3, 7, 0, 4, 10, 1, 13, 11, 6],
                 [4, 3, 2, 12, 9, 5, 15, 10, 11, 14, 1, 7, 6, 0, 8, 13]],

                [[4, 11, 2, 14, 15, 0, 8, 13, 3, 12, 9, 7, 5, 10, 6, 1],
                 [13, 0, 11, 7, 4, 9, 1, 10, 14, 3, 5, 12, 2, 15, 8, 6],
                 [1, 4, 11, 13, 12, 3, 7, 14, 10, 15, 6, 8, 0, 5, 9, 2],
                 [6, 11, 13, 8, 1, 4, 10, 7, 9, 5, 0, 15, 14, 2, 3, 12]],

                [[13, 2, 8, 4, 6, 15, 11, 1, 10, 9, 3, 14, 5, 0, 12, 7],
                 [1, 15, 13, 8, 10, 3, 7, 4, 12, 5, 6, 11, 0, 14, 9, 2],
                 [7, 11, 4, 1, 9, 12, 14, 2, 0, 6, 10, 13, 15, 3, 5, 8],
                 [2, 1, 14, 7, 4, 10, 8, 13, 15, 12, 9, 0, 3, 5, 6, 11]]]

# Final Permutation Table final_perm
IPF = [40, 8, 48, 16, 56, 24, 64, 32,
       39, 7, 47, 15, 55, 23, 63, 31,
       38, 6, 46, 14, 54, 22, 62, 30,
       37, 5, 45, 13, 53, 21, 61, 29,
       36, 4, 44, 12, 52, 20, 60, 28,
       35, 3, 43, 11, 51, 19, 59, 27,
       34, 2, 42, 10, 50, 18, 58, 26,
       33, 1, 41, 9, 49, 17, 57, 25]

key_perm = [57, 49, 41, 33, 25, 17, 9,
            1, 58, 50, 42, 34, 26, 18,
            10, 2, 59, 51, 43, 35, 27,
            19, 11, 3, 60, 52, 44, 36,
            63, 55, 47, 39, 31, 23, 15,
            7, 62, 54, 46, 38, 30, 22,
            14, 6, 61, 53, 45, 37, 29,
            21, 13, 5, 28, 20, 12, 4]

# for keys generation
shift_bits = [1, 1, 2, 2,
              2, 2, 2, 2,
              1, 2, 2, 2,
              2, 2, 2, 1]

key_compression = [14, 17, 11, 24, 1, 5,
                   3, 28, 15, 6, 21, 10,
                   23, 19, 12, 4, 26, 8,
                   16, 7, 27, 20, 13, 2,
                   41, 52, 31, 37, 47, 55,
                   30, 40, 51, 45, 33, 48,
                   44, 49, 39, 56, 34, 53,
                   46, 42, 50, 36, 29, 32]

rpt = [0] * 100
lpt = [0] * 100
copy_rpt = [0] * 100
s_box = [0] * 100
generated_keys = []
plain_text = []
copy_plain_text = []
encrypted_text = []
main_text = []
encrypted_text_final = []
number_of_bits = 0


def text_to_binary(message):
    """
    Function used transform a message from ascii to binary form. If the message is not a multiple of 64 bits we append
    0 until the message is a multiple of 64 bits
    :param str message: The message to transform into binary form
    :return str: The binary form of the message
    """
    message = str(message)
    message_binary = ''.join(format(ord(i), '08b') for i in message)
    while len(message_binary) % 64 != 0:
        message_binary += '0'

    for bit in message_binary:
        main_text.append(bit)
    return message_binary


def shift_left(k, nth_shifts):
    """
    Function used for shifting the binary list k nth_shifts to the left
    :param str k: The list we want to shift n bits to the left
    :param int nth_shifts: The number of bytes we want to shift
    :return str: the list shifted
    """
    s = ""
    for i in range(nth_shifts):
        for j in range(1, len(k)):
            s = s + k[j]
        s = s + k[0]
        k = s
        s = ""
    return k


def xor(a, b):
    """
    Function that applies xor on binary number a and binary number b ( represented as str )
    :param str a:
    :param str b:
    :return str: xor between a and b
    """
    ans = ""
    for i in range(len(a)):
        if a[i] == b[i]:
            ans = ans + "0"
        else:
            ans = ans + "1"
    return ans


def permute(to_perm, permutation_table, n):
    """
    Function that applies the permutation from a permutation table ( Standard permutations for DES ) on to_perm
    :param str to_perm: the string (binary) we want to permute
    :param list permutation_table: An standard permutation of DES
    :param int n: the size of the permutation_table
    :return str: the string to_perm permuted
    """
    permutation = ""
    for i in range(0, n):
        permutation = permutation + to_perm[permutation_table[i] - 1]
    return permutation


def round_keys(key):
    """
Function that generates 16 round keys, one for each permutation of DES
    :param str key: DES key
    :return list: The list with all 16 keys
    """
    left = key[0:28]
    right = key[28:56]
    round_k = []
    for i in range(0, 16):
        left = shift_left(left, shift_bits[i])
        right = shift_left(right, shift_bits[i])
        combine_str = left + right
        # Compression of key from 56 to 48 bits
        round_key = permute(combine_str, key_compression, 48)
        round_k.append(round_key)
    return round_k


def binary_to_decimal(binary):
    """
    Function that converts a number from base 2 to base 10
    :param int binary: The binary number we want to convert
    :return str: The number converted to base 10
    """
    decimal, i, n = 0, 0, 0
    while binary != 0:
        dec = binary % 10
        decimal = decimal + dec * pow(2, i)
        binary = binary // 10
        i += 1
    return decimal


def decimal_to_binary(number):
    """
    Function that converts a number from base 10 to base 2
    :param int number: The decimal number we want to convert
    :return str: The number converted to base 2
    """
    res = bin(number).replace("0b", "")
    if len(res) % 4 != 0:
        div = len(res) / 4
        div = int(div)
        counter = (4 * (div + 1)) - len(res)
        for i in range(0, counter):
            res = '0' + res
    return res


def binary_to_text(bit_string):
    """
    Function that transforms a text from ASCII to binary form
    :param str bit_string: the bit string we want to transform to text
    :return str: Text form of the binary message
    """
    returned_text = ""
    for i in range(0, len(bit_string), 8):
        current_bit_string = bit_string[i:i + 8]
        number = 0
        power = 1
        current_bit_string = int(current_bit_string)
        while current_bit_string > 0:
            rem = current_bit_string % 10
            current_bit_string = current_bit_string // 10
            number += rem * power
            power = power * 2
        returned_text += chr(number)
    return returned_text


def key_to_binary(message):
    """
    Function that transform the DES key from text to binary form
    :param str message: The key we want to transform
    :return str: The binary form of the key
    """
    binary_key = text_to_binary(message)
    return binary_key


def encrypt(plain, key):
    """
    The main function for DES encryption. The function encrypts blocks of 64 bits in ECB mode.
    The main steps of DES encryption:
    0. Generate round keys(One key for each round)
    1. Initial permutation
    2. Split the text into 2 halves (LPT and RPT)
    3. LPT and RPT goes through 16 rounds of the encryption process
    4. Join LPT and RPT
    5. Perform the final Permutation
    6. We get the 64 bits block encrypted
    :param str plain: The text we want to encrypt
    :param str key: The key for DES encryption
    :return str: The message encrypted
    """
    final_return = ""
    key = key_to_binary(key)
    # round keys
    plain = text_to_binary(plain)
    key = permute(key, key_perm, 56)
    round_k = round_keys(key)
    for block in range(0, len(plain), 64):
        pt = plain[block:block + 64]
        # 1. Initial permutation
        pt = permute(pt, IP, 64)

        # 2. Split into 2 halves
        left = pt[0:32]
        right = pt[32:64]
        # 16 rounds
        for i in range(0, 16):
            right_expanded = permute(right, RE, 48)
            xor_x = xor(right_expanded, round_k[i])
            s_sbox_str = ""
            for j in range(0, 8):
                row = binary_to_decimal(int(xor_x[j * 6] + xor_x[j * 6 + 5]))
                col = binary_to_decimal(
                    int(xor_x[j * 6 + 1] + xor_x[j * 6 + 2] + xor_x[j * 6 + 3] + xor_x[j * 6 + 4]))
                val = s_box_matrix[j][row][col]
                s_sbox_str = s_sbox_str + decimal_to_binary(val)
            s_sbox_str = permute(s_sbox_str, box_permutation, 32)
            result = xor(left, s_sbox_str)
            left = result
            if i != 15:
                left, right = right, left
        combine = left + right
        cipher_text = permute(combine, IPF, 64)
        final_return += cipher_text
    return final_return


def decrypt(enc_text, key):
    """
    The main function for DES decryption. The function decrypts an encrypted message(in ECB mode).
    The main steps of DES decryption:
    0. Generate round keys(One key for each round,in the reverse order of encryption)
    1. Initial permutation
    2. Split the text into 2 halves (LPT and RPT)
    3. LPT and RPT goes through 16 rounds of the encryption process
    4. Join LPT and RPT
    5. Perform the final Permutation
    6. We get the 64 bits block encrypted
    :param str enc_text: The text we want to decrypt
    :param str key: The key for DES decryption (the same key that we used for encryption)
    :return str: The message encrypted
    """
    final_return = ""
    enc_text = binary_to_text(enc_text)
    key = key_to_binary(key)
    enc_text = text_to_binary(enc_text)
    key = permute(key, key_perm, 56)
    round_k = round_keys(key)
    # put the keys in reverse order
    round_k = round_k[::-1]
    for block in range(0, len(enc_text), 64):
        cipher = enc_text[block:block + 64]
        cipher = permute(cipher, IP, 64)

        # Splitting
        left = cipher[0:32]
        right = cipher[32:64]
        for i in range(0, 16):
            right_expanded = permute(right, RE, 48)
            xor_x = xor(right_expanded, round_k[i])
            s_box_str = ""
            for j in range(0, 8):
                row = binary_to_decimal(int(xor_x[j * 6] + xor_x[j * 6 + 5]))
                col = binary_to_decimal(
                    int(xor_x[j * 6 + 1] + xor_x[j * 6 + 2] + xor_x[j * 6 + 3] + xor_x[j * 6 + 4]))
                val = s_box_matrix[j][row][col]
                s_box_str = s_box_str + decimal_to_binary(val)
            s_box_str = permute(s_box_str, box_permutation, 32)
            result = xor(left, s_box_str)
            left = result
            if i != 15:
                left, right = right, left
        combine = left + right
        cipher_text = permute(combine, IPF, 64)
        final_return += cipher_text
    return final_return
