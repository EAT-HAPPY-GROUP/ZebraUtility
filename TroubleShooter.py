import os, sys
import win32print
import tkinter as tk
import binascii

### print content of e: internal flash memory
def listMemoryE():
    zpl = "^XA^LL300^WDE:*.*^XZ"
    sendToPrinter(bytes(zpl, "utf-8"))

### print content of R: internal RAM memory
def listMemoryR():
    zpl = "^XA^LL300^WDR:*.*^XZ"
    sendToPrinter(bytes(zpl, "utf-8"))

def loadFontEHBasic():
    file = 'EH-BASIC.TTF'
    with open(file, 'rb') as f:
        binaryData = f.read()

    #convert to hex string
    hexData = binascii.hexlify(binaryData)


    #Load ttf to PRINTER. https://docs.zebra.com/content/tcm/us/en/printers/software/zebra-zpl-ii,-zbi-2,-set-get-do,-mirror,-wml-programming-guide/c-zpl-zpl-commands/r-zpl-du.html
    zpl = "^XA^CI~DUE:"+file.upper()+","+str(len(binaryData))+","+ str(hexData)[2:-1].upper()

    #print teststring
    zpl = zpl +"^FO30,60^A@N,70,40,E:"+file[:-4]+".FNT^FDEAT Happyness^FS"

    #close 
    zpl = zpl + "^XZ"
    sendToPrinter(bytes(zpl, "utf-8"))

### send given bytes to default printer
def sendToPrinter(data):
    printer_name = win32print.GetDefaultPrinter()
    
    #send data to printer
    hPrinter = win32print.OpenPrinter (printer_name)
    try:
        #send command to reset to factory defaults
        hJob = win32print.StartDocPrinter (hPrinter, 1, ("Print", None, "RAW"))
        try:
            win32print.StartPagePrinter (hPrinter)
            win32print.WritePrinter (hPrinter, data)
            win32print.EndPagePrinter (hPrinter)
        finally:
            win32print.EndDocPrinter (hPrinter)
    finally:
        win32print.ClosePrinter (hPrinter)
    
    print("sendToPrinter done")


root = tk.Tk()
#root.geometry('300x200')
#root.resizable(False, False)
#root.title('Zebra Troubleshooter Util')


# place a label on the root window
tk.Label(root, text="Print Memory").pack()

tk.Button(root, text="E:", command=listMemoryE).pack()
tk.Button(root, text="R:", command=listMemoryR).pack()
tk.Label(root, text="Load Font").pack()
tk.Button(root, text="EH-BASIC.TTF", command=loadFontEHBasic).pack()


# keep the window displaying
root.mainloop()


