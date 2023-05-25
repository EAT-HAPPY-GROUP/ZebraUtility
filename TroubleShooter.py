import os, sys
import win32print
import tkinter as tk

### print content of e: internal flash memory
def listMemoryE():
    zpl = "^XA^LL300^WDE:*.*^XZ"
    sendToPrinter(bytes(zpl, "utf-8"))

### print content of R: internal RAM memory
def listMemoryR():
    zpl = "^XA^LL300^WDR:*.*^XZ"
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
message = tk.Label(root, text="Print Memory").pack()

canvas = tk.Canvas(root, width=300, height=100, bg='white')
canvas.pack(anchor=tk.LEFT, expand=True)
canvas.Button(root, text="E:", command=listMemoryE).pack()
canvas.Button(root, text="R:", command=listMemoryR).pack()


# keep the window displaying
root.mainloop()


