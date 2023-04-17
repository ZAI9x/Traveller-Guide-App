#CS111 Project 
#Traveller Guied App
#Main window 


import tkinter as tk #tk because it make it easire to use
from tkinter import Label #importing the label 

from CurrencyExchange import currency_window #this is the function  fot button2
from TicketPrices import ticket_window #this is the function  fot button1



#The window
root = tk.Tk() #use tkinter to build our window
root.title("TRAVELLER GUIDE APP") #the title of the window
root.geometry("800x350") #geometry() is for measuring the window

background_image = tk.PhotoImage(file='TravellerGuide.png') #name a vatiable for the background photo. and to upload the photo use the function PhotoImage() 
background_label = tk.Label(root, image=background_image) #name a vatiable for the background label. and to upload the photo inside the label the Property Image
background_label.place(relx=0, rely=0, relwidth=1 , relheight=1 ) #locate it and size it 


frame = tk.Frame(root, bg='lightCyan2', bd=5) #name a variable for the frame and located in the root, and use Frame() function to do the frame
frame.place(relx=0.5, rely=0.1, relwidth=0.75, relheight=0.1 ,anchor='n')#locate it and size it


label1 = tk.Label(frame, text=" WELCOME TO TRAVELLER GUIDE APP", fg='DeepPink4', font=("Arial",20)) #name a variable for the label and located in the root, and use label() function to do the label
label1.pack()#locate it 


lower_frame = tk.Frame(root, bd=10, bg='lightCyan2')#name a variable for the frame and located in the root, and use Frame() function to do the frame
lower_frame.place(relx=0.5, rely=0.25, relwidth=0.75, relheight=0.6, anchor='n')#locate it and size it



label2 = tk.Label(lower_frame, text="What would you like to do?" ,font=("Arial",21))#name a variable for the label and located in the root, and use label() function to do the label
label2.pack()#locate it 


button1 = tk.Button(lower_frame, text="Check Tickets Prices", bg='lightblue' , font=("Arial",15), command=ticket_window)#name a variable for the button and located in the root, and use Button() function to do the button
button1.place(relx=0.3, rely=0.4, relwidth=0.4, relheight=0.3, anchor='n')#locate it and size it


button2 = tk.Button(lower_frame, text="Currency Exchange", bg='lightblue', font=("Arial",15), command=currency_window)#name a variable for the button and located in the root, and use Button() function to do the button
button2.place(relx=0.75, rely=0.4, relwidth=0.4, relheight=0.3, anchor='n')#locate it and size it


root.mainloop()
