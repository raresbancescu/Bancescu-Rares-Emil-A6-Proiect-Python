from rsa import isPrime, generate_parameters,rsa


def main():
    (pk,sk,n)=generate_parameters()
    # print("Public key",pk)
    # print("Private key",sk)
    cripted=rsa("rares","encript",pk,sk,n)
    print(cripted)
    print("decriptare:")
    print(rsa(cripted, "decript", pk, sk, n))
if __name__ == "__main__":
    main()
