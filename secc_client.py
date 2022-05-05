import rsa
import tkinter as tk
import socket




def main():

    #creating basic GUI elements
    window = tk.Tk()
    window.geometry("800x500")
    recieverBox = tk.Text(window, height = 20, width = 80)
    senderBox = tk.Text(window, height = 5, width = 80)
    senderButt = tk.Button(text = "send")

    #placing onto the window
    senderButt.grid(row = 1, column = 1, pady = 10, padx = 10)
    recieverBox.grid(row = 0, column = 0, pady = 10, padx = 1)
    senderBox.grid(row = 1, column = 0, pady = 10, padx = 1)
    window.mainloop()



def genKeys():
    (pubkey, privatekey) = rsa.newkeys(1024)
    return pubkey, privatekey


if __name__ == "__main__":
    main()
