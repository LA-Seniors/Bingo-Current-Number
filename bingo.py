#Bingo Current Number 
#Bingo Current Number © 2024 by Fairfax Senior Center is licensed under Creative Commons Attribution-NonCommercial-ShareAlike 4.0 International 

#Thank you to Farhan from Fiverr.com
#The font colors are WCAG 2 AAA and AA rated
#This python code will display the current Bingo "Letter" and "Number" when typed on a keyboard
#I suggest a Raspberry Pi Zero or old used computer with Ubuntu OS or Raspbian OS installed
#I suggest a big monitor or TV to display "Current Bingo Number"
#I suggest a USB wireless keyboard 
#No WIFI connection is needed
#You need Python3 installed to run this code

#To Start and Stop "Bingo Current Number" code

#1. open "Terminal"
#2. change your directory to where the file name "bingo.py" is located, maybe it is in Downloads. type "cd Downloads" and then push the "enter key"
#3. type "python3 bingo.py" and then push the "enter key"
#4. "alt"+"F4" to exit or stop the code

#Keyboard Commands and How to use "Currrent Bingo Nuumber"

#esc = return to the home screen, the "Clear Your Cards" screen
#"alt" key + "F4" key to exit "Bingo Current Number" code
#type a number "1 through 75" and then "enter" - The Bingo "Letter and Number" will displayed on your screen

#How to edit the code

#to edit the dislpay, font color, and border size you need to change the numbers in the code below. 
#Start with 0 pad and then increase or decrease your font size until your TV screen looks how you like it

import tkinter as tk
from tkinter import ttk

number = ""
prevNum = ""
start = False
startPrev = False

label2 = None
label3 = None
label4 = None

def onKeyPress(event):
    global number
    global prevNum
    global start
    global startPrev
    
    global label1
    global label2
    global label3
    global label4
    
    global frame
    
    pad = 15
    
    if event.char == '\x1b':
        number = ""
        prevNum = ""
        start = False
        startPrev = False

        for widget in root.winfo_children():
            widget.destroy()

        root.grid_columnconfigure(1, weight=0)

        label1=ttk.Label(root, foreground='#0051A5', text="CLEAR\nYOUR\nCARDS", font='Arial 200 bold', justify=tk.CENTER)
        label1.grid(row=0, column=0)
        
    if event.char in ['\r', '\n', '\r\n']:

        if len(number) > 0:
            if int(number) == 0:
                number = ""
                return
        
            if not start:
            
                for widget in root.winfo_children():
                    widget.destroy()

                root.grid_columnconfigure(1, weight=0)
                
                label1=ttk.Label(root, foreground='#0051A5', text="CURRENT BINGO NUMBER", font='Arial 103 bold', justify=tk.CENTER)
                label1.grid(row=0, column=0, pady=pad)

                label2=ttk.Label(root, foreground='#0051A5', text="", font='"Times New Roman" 480 bold', justify=tk.CENTER, borderwidth=0, relief="solid")
                label2.grid(row=1, column=0, pady=pad)

                label3=ttk.Label(root, foreground='#333333', text="", font='Arial 80', justify=tk.CENTER)
                label3.grid(row=2, column=0, pady=pad)
                
                start = True

            if not startPrev:
                if prevNum != "":

                    for widget in root.winfo_children():
                        widget.destroy()

                    root.grid_columnconfigure(1, weight=1)

                    label1=ttk.Label(root, foreground='#0051A5', text="CURRENT BINGO NUMBER", font='Arial 103 bold', justify=tk.CENTER)
                    label1.grid(row=0, column=0, columnspan=2, pady=pad)

                    label2=ttk.Label(root, foreground='#0051A5', text="", font='"Times New Roman" 480 bold', justify=tk.CENTER, borderwidth=0, relief="solid")
                    label2.grid(row=1, column=0, columnspan=2, pady=pad)

                    label3=ttk.Label(root, foreground='#333333', text="PREVIOUS BINGO NUMBER", font='Arial 80 bold', justify=tk.CENTER)
                    label3.grid(row=2, column=0, pady=pad)

                    label4=ttk.Label(root, foreground='#333333', text="", font='"Times New Roman" 95 bold', justify=tk.CENTER, borderwidth=5, relief="solid")
                    label4.grid(row=2, column=1, pady=pad)
                    
                    startPrev = True
            
            if int(number) > 60:
                number = "O  " + number
            elif int(number) > 45:
                number = "G  " + number
            elif int(number) > 30:
                number = "N  " + number
            elif int(number) > 15:
                number = "I  " + number
            elif int(number) > 0:
                number = "B  " + number
            else:
                return
            
            label2.config(text=number)
            
            if prevNum != "":
                label4.config(text=prevNum)
                        
            prevNum = number
            number = ""
        
    else:
        if len(event.char) == 0:
            return
            
        if not event.char.isdigit():
            return

        if len(number) >= 2:
            return
            
        if len(number) == 1:
            if int(number[0]) > 7:
                return

            if int(number[0]) == 7:
                if int(event.char) > 5:
                    return
        
        number = number + event.char
    
# writing code needs to
# create the main window of 
# the application creating 
# main window object named root
root = tk.Tk()
root.attributes('-fullscreen', True)
 
# giving title to the main window
root.title("First_Program")
root.grid_rowconfigure(0, weight=1)
root.grid_columnconfigure(0, weight=1)

root.bind('<KeyPress>', onKeyPress)

frame=ttk.Frame(root, width=300, height=300)
frame.grid(row=0, column=0)

#frame.place(relx=0.5, rely=0.5, relwidth=0.5, relheight=1, anchor="c")
        
# Create a label widget
label1=ttk.Label(root, foreground='#0051A5', text="CLEAR\nYOUR\nCARDS", font='Arial 200 bold', justify=tk.CENTER)
label1.grid(row=0, column=0)
#label1.place(relx=0.5, rely=0.5, anchor=tk.CENTER)

 
# calling mainloop method which is used
# when your application is ready to run
# and it tells the code to keep displaying 
root.mainloop()
