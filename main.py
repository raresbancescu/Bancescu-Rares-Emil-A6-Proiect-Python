from rsa import isPrime, generate_parameters, rsa


def encript_file(pk, sk, n):
    cripted = rsa("The reality shows that the distribution of the scores obtained The reality shows that the distribu", "encript", pk, sk, n)
    try:
        file_descriptor = open("cript.txt", "wb")
        cripted=cripted.encode()
        file_descriptor.write(cripted)
    except Exception as e:
        print(str(e))

def decript_file(pk, sk, n):
    try:
        file_descriptor = open("cript.txt", "rb")
        message=file_descriptor.read()
        message=message.decode()
        decript = rsa(message, "decript", pk, sk, n)
        print(decript)
    except:
        print("Eroare")

def main():
    (pk, sk, n) = generate_parameters()
    # print("Public key",pk)
    # print("Private key",sk)
    # cripted = rsa("Andreea", "encript", pk, sk, n)
    # print("decriptare:")
    # print(rsa(cripted, "decript", pk, sk, n))

    encript_file(pk,sk,n)
    decript_file(pk,sk,n)


if __name__ == "__main__":
    main()
