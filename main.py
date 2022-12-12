from rsa import isPrime, generate_parameters, rsa
from des import *
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


def hibrid_encription():
    (pk, sk, n) = generate_parameters()
    key="criptocr"
    cripted_key=rsa(key,"encript",pk,0,n)
    decripted_key=rsa(cripted_key,"decript",0,sk,n)

    c=encrypt("orem Ipsum is simply dummy text of the printing and typesetting industry. Lorem Ipsum has been the industry's standard dummy text ever since the 1500s, when an unknown printer took a galley of type and scrambled it to make a type specimen book. It has survived not only five centuries, but also the leap into electronic typesetting, remaining essentially unchanged. It was popularised in the 1960s with the release of Letraset sheets containing Lorem Ipsum passages, and more recently with desktop publishing software like Aldus PageMaker including versions of Lorem Ipsum.",decripted_key)
    normal=decript(c,decripted_key)
    print(binary_to_text(normal))

def main():
    # (pk, sk, n) = generate_parameters()
    # print("Public key",pk)
    # print("Private key",sk)
    # cripted = rsa("test", "encript", pk, sk, n)
    # print("decriptare:")
    # print(rsa(cripted, "decript", pk, sk, n))
    # encript_file(pk,sk,n)
    # decript_file(pk,sk,n)
    hibrid_encription()


if __name__ == "__main__":
   main()
