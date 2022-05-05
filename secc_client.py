import rsa
import PyQt5
import twisted


def main():
    print("hello!")

def genKeys():
    (pubkey, privatekey) = rsa.newkeys(1024)
    return pubkey, privatekey


if __name__ == "__main__":
    main()
