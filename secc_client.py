import rsa
import PyQt5
import socket




def main():
    print("hello! Generating keys...")
    pubkey, privatekey = genKeys()


def genKeys():
    (pubkey, privatekey) = rsa.newkeys(1024)
    return pubkey, privatekey


if __name__ == "__main__":
    main()
