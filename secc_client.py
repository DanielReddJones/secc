####################
#Author: Daniel Jones
#Language: Python 3.10.2
#IDE: Atom
#OS: Windows/PopOS
#last modified: 5/13/2022
####################


import rsa #used for text encryption/decryption
import tkinter as tk 
import socket
import cryptography #used for voice encryption/decryption




def main():

    #creating basic GUI elements
    window = tk.Tk()
    window.geometry("800x500")
    recieverBox = tk.Text(window, height = 20, width = 80)
    senderBox = tk.Text(window, height = 5, width = 80)
    voiceBox = tk.Button(text= "speak")
    senderButt = tk.Button(text = "send")

    #placing onto the window
    senderButt.grid(row = 1, column = 1, pady = 10, padx = 10)
    recieverBox.grid(row = 0, column = 0, pady = 10, padx = 1)
    senderBox.grid(row = 1, column = 0, pady = 10, padx = 1)
    voiceBox.grid(row = 1, column = 2, pady = 10, padx = 10)
    window.mainloop()



def genKeys():
    (pubkey, privatekey) = rsa.newkeys(1024)
    return pubkey, privatekey


if __name__ == "__main__":
    main()
