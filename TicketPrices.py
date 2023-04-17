#Ticket Prices widow 

import tkinter as tk #tk because it make it easire to use
from tkinter import Label #importing the label

#create a function for the ticket prices window

def ticket_window():
    #window
    root = tk.Toplevel() #use tkinter to build our window
    root.title('Check Tickets Prices')  #the title of the window
    root.geometry('750x500') #geometry() is for measuring the window

    background_label = tk.Label(root, bg='turquoise4') #name a vatiable for the background label. and located in the root and choose the background color 
    background_label.place(relx=0, rely=0, relwidth=1 , relheight=1 ) #locate it and size it. 

    upper_frame = tk.Frame(root, bg='HotPink4')
    upper_frame.place(relx=0.09, rely=0.02, relwidth=0.85, relheight=0.1) #locate it and size it. 

    label0 = tk.Label(upper_frame, text='Check Ticket Prices', font=("Arial",30))#name a variable for the frame and located in the upper frame, and use Frame() function to do the frame
    label0.pack()

    left_frame = tk.Frame(root,  bg='lightcyan2')
    left_frame.place(relx=0.05, rely=0.13, relwidth=0.45, relheight=0.7) #locate it and size it. 


    label1 = tk.Label(left_frame, text="""From the list below choice the number of
    country that you are leaving from """, font=("Arial",13), fg='Darkorchid4')#name a variable for the frame and located in the left frame, and use Frame() function to do the frame
    label1.place(relx=0.05, rely=0.04, relwidth=0.89, relheight=0.1) #locate it and size it. 



    label2 = tk.Label(left_frame, text=""" 1.Saudi Arabia
 2.UAE United Arabs Emirets
 3.Kuwait
 4.Bahraini """, font=("Arial",15), fg='OrangeRed2')#name a variable for the frame and located in the left frame, and use Frame() function to do the frame.

    label2.place(relx=0.05, rely=0.15, relwidth=0.8, relheight=0.65) #locate it and size it. 


    label3 = tk.Label(left_frame, text='Enter it here:-', font=("Arial",10))#name a variable for the frame and located in the left frame, and use Frame() function to do the frame
    label3.place(relx=0.05, rely=0.83, relwidth=0.3, relheight=0.1) #locate it and size it. 


    entry1 = tk.Entry(left_frame, font=40)#name a variable for the frame and located in the left frame, and use Frame() function to do the frame
    entry1.place(relx=0.39, rely=0.83, relwidth=0.25, relheight=0.1) #locate it and size it. 

    next_button1 = tk.Button(left_frame, text='Next', bg='lightblue', command=lambda : counting_amount(entry1.get()))
    next_button1.place(relx=0.69, rely=0.89, relwidth=0.3, relheight=0.1) #locate it and size it. 


    right_frame = tk.Frame(root, bg='lightcyan2')
    right_frame.place(relx=0.53, rely=0.13, relwidth=0.45, relheight=0.7) #locate it and size it. 
    

    lower_frame = tk.Frame(root, bg='HotPink4')
    lower_frame.place(relx=0.09, rely=0.85, relwidth=0.85, relheight=0.13) #locate it and size it. 


    def counting_amount(entry1):
        t = entry1

        if t=='1':
            label5 = tk.Label(right_frame, text=' choice the number of country you want to go..', font=("Arial",11))#name a variable for the frame and located in the right frame, and use Frame() function to do the frame
            label5.place(relx=0.07, rely=0.05, relwidth=0.87, relheight=0.1) #locate it and size it. 

            label6 = tk.Label(right_frame, text="""1.UAE \n2.Kuwait \n3.Bahrain """, font=("Arial",15), fg='OrangeRed2')#name a variable for the frame and located in the right frame, and use Frame() function to do the frame
            label6.place(relx=0.07, rely=0.17, relwidth=0.8, relheight=0.4) #locate it and size it. 

            entrySA = tk.Entry(right_frame, font=40)
            entrySA.place(relx=0.08, rely=0.6 ,relwidth=0.5, relheight=0.1)  #locate it and size it.                              

            lower_frame1 = tk.Frame(root, bg='HotPink4')
            lower_frame1.place(relx=0.09, rely=0.85, relwidth=0.85, relheight=0.13) #locate it and size it. 

            next_button2 = tk.Button(right_frame, text='Next', bg='lightblue',command=lambda : des_entry(entrySA.get()))
            next_button2.place(relx=0.65, rely=0.6 ,relwidth=0.3, relheight=0.1) #locate it and size it. 


            def des_entry(entrySA):

                y = entrySA
                try:
                    if y=='1':
                        lower_frame00 = tk.Frame(root, bg='HotPink4')
                        lower_frame00.place(relx=0.09, rely=0.85, relwidth=0.85, relheight=0.13) #locate it and size it. 
                     
                        label7 = tk.Label(right_frame, text="would you like to travel by \n PLANE or BUS", font=('Arial',13))#name a variable for the frame and located in the right frame, and use Frame() function to do the frame
                        label7.place(relx=0.15, rely=0.72 ,relwidth=0.7, relheight=0.15) #locate it and size it. 

                        label8 = tk.Label(right_frame, text='Enter it here:-', font=("Arial",10))#name a variable for the frame and located in the right frame, and use Frame() function to do the frame
                        label8.place(relx=0.05, rely=0.89, relwidth=0.3, relheight=0.1) #locate it and size it. 

                        entry2 = tk.Entry(right_frame, font=40)
                        entry2.place(relx=0.39, rely=0.89, relwidth=0.25, relheight=0.1) #locate it and size it. 

                        next_button3 = tk.Button(right_frame, text='Check', bg='lightblue', command=lambda : checktrans_button(entry2.get()))
                        next_button3.place(relx=0.69, rely=0.89, relwidth=0.3, relheight=0.1) #locate it and size it. 
                        
                        
                        def checktrans_button(entry2):
                            x = entry2.upper()
                            lower_frame00lastelse = tk.Frame(root, bg='HotPink4')
                            lower_frame00lastelse.place(relx=0.09, rely=0.85, relwidth=0.85, relheight=0.13) #locate it and size it. 
                            entry3 = tk.Entry(lower_frame00lastelse, font=40)
                            entry3.place(relx=0.45, rely=0.15, relwidth=0.35, relheight=0.5) #locate it and size it. 
                            
                            plane_cost = "This will cost you 1500"
                            bus_cost = "This will cost you 600"

                            if x=='PLANE':
                                entry3.insert(0, plane_cost)
                            elif x=='BUS':
                                entry3.insert(0, bus_cost)
                            else:
                                lower_frame4 = tk.Frame(root, bg='HotPink4')
                                lower_frame4.place(relx=0.09, rely=0.85, relwidth=0.85, relheight=0.13) #locate it and size it. 
                                entry_warning4 = tk.Entry(lower_frame4, font=('Arial',11))
                                entry_warning4.place(relx=0.1, rely=0.1, relwidth=0.8, relheight=0.6) #locate it and size it. 
                                warning4 = "You have entered wrong value . -Please choose plane or bus- "
                                entry_warning4.insert(0, warning4)

                    elif y=='2':
                        lower_frame002 = tk.Frame(root, bg='HotPink4')
                        lower_frame002.place(relx=0.09, rely=0.85, relwidth=0.85, relheight=0.13) #locate it and size it. 
                     
                        label002 = tk.Label(right_frame, text="would you like to travel by \n PLANE or BUS", font=('Arial',13))#name a variable for the frame and located in the right frame, and use Frame() function to do the frame
                        label002.place(relx=0.15, rely=0.72 ,relwidth=0.7, relheight=0.15) #locate it and size it. 

                        label021 = tk.Label(right_frame, text='Enter it here:-', font=("Arial",10))#name a variable for the frame and located in the right frame, and use Frame() function to do the frame
                        label021.place(relx=0.05, rely=0.89, relwidth=0.3, relheight=0.1) #locate it and size it. 

                        entry002 = tk.Entry(right_frame, font=40)
                        entry002.place(relx=0.39, rely=0.89, relwidth=0.25, relheight=0.1) #locate it and size it. 

                        next_button002 = tk.Button(right_frame, text='Check', bg='lightblue', command=lambda : checktrans_button(entry002.get()))
                        next_button002.place(relx=0.69, rely=0.89, relwidth=0.3, relheight=0.1) #locate it and size it. 

                        def checktrans_button(entry002):
                            x = entry002.upper()
                            lower_frame002lastelse = tk.Frame(root, bg='HotPink4')
                            lower_frame002lastelse.place(relx=0.09, rely=0.85, relwidth=0.85, relheight=0.13) #locate it and size it. 
                            entry23 = tk.Entry(lower_frame002lastelse, font=40)
                            entry23.place(relx=0.45, rely=0.15, relwidth=0.35, relheight=0.5) #locate it and size it. 
                            
                            plane_cost = "This will cost you 1700"
                            bus_cost = "This will cost you 700"

                            if x=='PLANE':
                                entry23.insert(0, plane_cost)
                            elif x=='BUS':
                                entry23.insert(0, bus_cost)
                            else:
                                lower_frame5 = tk.Frame(root, bg='HotPink4')
                                lower_frame5.place(relx=0.09, rely=0.85, relwidth=0.85, relheight=0.13) #locate it and size it. 
                                entry_warning5 = tk.Entry(lower_frame5, font=('Arial',11))
                                entry_warning5.place(relx=0.1, rely=0.1, relwidth=0.8, relheight=0.6) #locate it and size it. 
                                warning5 = "You have entered wrong value . -Please choose plane or bus- "
                                entry_warning5.insert(0, warning5)
                        
                    elif y=='3':
                        lower_frame003 = tk.Frame(root, bg='HotPink4')
                        lower_frame003.place(relx=0.09, rely=0.85, relwidth=0.85, relheight=0.13) #locate it and size it. 
                     
                        label003 = tk.Label(right_frame, text="would you like to travel by \n PLANE or BUS", font=('Arial',13))#name a variable for the frame and located in the right frame, and use Frame() function to do the frame
                        label003.place(relx=0.15, rely=0.72 ,relwidth=0.7, relheight=0.15) #locate it and size it. 

                        label031 = tk.Label(right_frame, text='Enter it here:-', font=("Arial",10))#name a variable for the frame and located in the right frame, and use Frame() function to do the frame
                        label031.place(relx=0.05, rely=0.89, relwidth=0.3, relheight=0.1) #locate it and size it. 

                        entry003 = tk.Entry(right_frame, font=40)
                        entry003.place(relx=0.39, rely=0.89, relwidth=0.25, relheight=0.1) #locate it and size it. 

                        next_button003 = tk.Button(right_frame, text='Check', bg='lightblue', command=lambda : checktrans_button(entry003.get()))
                        next_button003.place(relx=0.69, rely=0.89, relwidth=0.3, relheight=0.1) #locate it and size it. 

                        def checktrans_button(entry003):
                            x = entry003.upper()
                            lower_frame003lastelse = tk.Frame(root, bg='HotPink4')
                            lower_frame003lastelse.place(relx=0.09, rely=0.85, relwidth=0.85, relheight=0.13) #locate it and size it. 
                            entry33 = tk.Entry(lower_frame003lastelse, font=40)
                            entry33.place(relx=0.45, rely=0.15, relwidth=0.35, relheight=0.5) #locate it and size it. 
                            
                            plane_cost = "This will cost you 2100"
                            bus_cost = "This will cost you 800"

                            if x=='PLANE':
                                entry33.insert(0, plane_cost)
                            elif x=='BUS':
                                entry33.insert(0, bus_cost)
                            else:
                                lower_frame6 = tk.Frame(root, bg='HotPink4')
                                lower_frame6.place(relx=0.09, rely=0.85, relwidth=0.85, relheight=0.13) #locate it and size it. 
                                entry_warning6 = tk.Entry(lower_frame6, font=('Arial',11))
                                entry_warning6.place(relx=0.1, rely=0.1, relwidth=0.8, relheight=0.6) #locate it and size it. 
                                warning6 = "You have entered wrong value . -Please choose plane or bus- "
                                entry_warning6.insert(0, warning6) 
                 

                    else:
                        lower_frame3 = tk.Frame(root, bg='HotPink4')
                        lower_frame3.place(relx=0.09, rely=0.85, relwidth=0.85, relheight=0.13)
                        entry_warning3 = tk.Entry(lower_frame3, font=('Arial',11))
                        entry_warning3.place(relx=0.1, rely=0.1, relwidth=0.8, relheight=0.6)
                        warning3 = "You have entered wrong value . -Please Enter number from the list- "
                        entry_warning3.insert(0, warning3)

                except:
                    lower_frame2 = tk.Frame(root, bg='HotPink4')
                    lower_frame2.place(relx=0.09, rely=0.85, relwidth=0.85, relheight=0.13)

                    entry_warning2 = tk.Entry(lower_frame2, font=('Arial',11))
                    entry_warning2.place(relx=0.1, rely=0.1, relwidth=0.8, relheight=0.6)
                    warning2 = "You have entered wrong value . Please try again . - Enter the number-"
                    entry_warning2.insert(0, warning2)






        elif t=='2':
            label7 = tk.Label(right_frame, text=' choice the number of country you want to go..', font=("Arial",11))#name a variable for the frame and located in the right frame, and use Frame() function to do the frame
            label7.place(relx=0.07, rely=0.05, relwidth=0.87, relheight=0.1)#locate it and size it. 

            label8 = tk.Label(right_frame, text="""1.Saudi Arabia \n2.Kuwait \n3.Bahrain """, font=("Arial",15), fg='OrangeRed2')#name a variable for the frame and located in the right frame, and use Frame() function to do the frame
            label8.place(relx=0.07, rely=0.17, relwidth=0.8, relheight=0.4)#locate it and size it. 

            entryUAE = tk.Entry(right_frame, font=40)
            entryUAE.place(relx=0.08, rely=0.6 ,relwidth=0.5, relheight=0.1)                              

            lower_frame21 = tk.Frame(root, bg='HotPink4')
            lower_frame21.place(relx=0.09, rely=0.85, relwidth=0.85, relheight=0.13)#locate it and size it. 

            next_button22 = tk.Button(right_frame, text='Next', bg='lightblue',command=lambda : des_entry(entryUAE.get()))
            next_button22.place(relx=0.65, rely=0.6 ,relwidth=0.3, relheight=0.1)#locate it and size it. 

            def des_entry(entryUAE):
                y = entryUAE

                try:
                    if y=='1':
                        lower_frame0021 = tk.Frame(root, bg='HotPink4')
                        lower_frame0021.place(relx=0.09, rely=0.85, relwidth=0.85, relheight=0.13)
                     
                        label0021 = tk.Label(right_frame, text="would you like to travel by \n PLANE or BUS", font=('Arial',13))#name a variable for the frame and located in the right frame, and use Frame() function to do the frame
                        label0021.place(relx=0.15, rely=0.72 ,relwidth=0.7, relheight=0.15)#locate it and size it. 

                        label0022 = tk.Label(right_frame, text='Enter it here:-', font=("Arial",10))#name a variable for the frame and located in the right frame, and use Frame() function to do the frame
                        label0022.place(relx=0.05, rely=0.89, relwidth=0.3, relheight=0.1)#locate it and size it. 

                        entry0021 = tk.Entry(right_frame, font=40)
                        entry0021.place(relx=0.39, rely=0.89, relwidth=0.25, relheight=0.1)

                        next_button0021 = tk.Button(right_frame, text='Check', bg='lightblue', command=lambda : checktrans_button(entry0021.get()))
                        next_button0021.place(relx=0.69, rely=0.89, relwidth=0.3, relheight=0.1)#locate it and size it. 

                        def checktrans_button(entry0021):
                            x = entry0021.upper()
                            lower_frame0021lastelse = tk.Frame(root, bg='HotPink4')
                            lower_frame0021lastelse.place(relx=0.09, rely=0.85, relwidth=0.85, relheight=0.13)
                            entry213 = tk.Entry(lower_frame0021lastelse, font=40)
                            entry213.place(relx=0.45, rely=0.15, relwidth=0.35, relheight=0.5)#locate it and size it. 
                            
                            plane_cost = "This will cost you 1590"
                            bus_cost = "This will cost you 750"

                            if x=='PLANE':
                                entry213.insert(0, plane_cost)
                            elif x=='BUS':
                                entry213.insert(0, bus_cost)
                            else:
                                lower_frame9 = tk.Frame(root, bg='HotPink4')
                                lower_frame9.place(relx=0.09, rely=0.85, relwidth=0.85, relheight=0.13)
                                entry_warning9 = tk.Entry(lower_frame9, font=('Arial',11))
                                entry_warning9.place(relx=0.1, rely=0.1, relwidth=0.8, relheight=0.6)#locate it and size it. 
                                warning9 = "You have entered wrong value . -Please choose plane or bus- "
                                entry_warning9.insert(0, warning9)

                    elif y=='2':
                        lower_frame0022 = tk.Frame(root, bg='HotPink4')
                        lower_frame0022.place(relx=0.09, rely=0.85, relwidth=0.85, relheight=0.13)#locate it and size it. 
                     
                        label0022 = tk.Label(right_frame, text="would you like to travel by \n PLANE or BUS", font=('Arial',13))#name a variable for the frame and located in the right frame, and use Frame() function to do the frame
                        label0022.place(relx=0.15, rely=0.72 ,relwidth=0.7, relheight=0.15)

                        label00221 = tk.Label(right_frame, text='Enter it here:-', font=("Arial",10))#name a variable for the frame and located in the right frame, and use Frame() function to do the frame
                        label00221.place(relx=0.05, rely=0.89, relwidth=0.3, relheight=0.1)#locate it and size it. 

                        entry0022 = tk.Entry(right_frame, font=40)
                        entry0022.place(relx=0.39, rely=0.89, relwidth=0.25, relheight=0.1)

                        next_button0022 = tk.Button(right_frame, text='Check', bg='lightblue', command=lambda : checktrans_button(entry0022.get()))
                        next_button0022.place(relx=0.69, rely=0.89, relwidth=0.3, relheight=0.1)

                        def checktrans_button(entry0022):
                            x = entry0022.upper()
                            lower_frame0022lastelse = tk.Frame(root, bg='HotPink4')
                            lower_frame0022lastelse.place(relx=0.09, rely=0.85, relwidth=0.85, relheight=0.13)
                            entry223 = tk.Entry(lower_frame0022lastelse, font=40)
                            entry223.place(relx=0.45, rely=0.15, relwidth=0.35, relheight=0.5)#locate it and size it. 
                            
                            plane_cost = "This will cost you 1390"
                            bus_cost = "This will cost you 620"

                            if x=='PLANE':
                                entry223.insert(0, plane_cost)
                            elif x=='BUS':
                                entry223.insert(0, bus_cost)
                            else:
                                lower_frame10 = tk.Frame(root, bg='HotPink4')
                                lower_frame10.place(relx=0.09, rely=0.85, relwidth=0.85, relheight=0.13)#locate it and size it. 
                                entry_warning10 = tk.Entry(lower_frame10, font=('Arial',11))
                                entry_warning10.place(relx=0.1, rely=0.1, relwidth=0.8, relheight=0.6)
                                warning10 = "You have entered wrong value . -Please choose plane or bus- "
                                entry_warning10.insert(0, warning10)

                    elif y=='3':
                        lower_frame0023 = tk.Frame(root, bg='HotPink4')
                        lower_frame0023.place(relx=0.09, rely=0.85, relwidth=0.85, relheight=0.13)
                     
                        label0023 = tk.Label(right_frame, text="would you like to travel by \n PLANE or BUS", font=('Arial',13))#name a variable for the frame and located in the right frame, and use Frame() function to do the frame
                        label0023.place(relx=0.15, rely=0.72 ,relwidth=0.7, relheight=0.15)

                        label00231 = tk.Label(right_frame, text='Enter it here:-', font=("Arial",10))#name a variable for the frame and located in the right frame, and use Frame() function to do the frame
                        label00231.place(relx=0.05, rely=0.89, relwidth=0.3, relheight=0.1)#locate it and size it. 

                        entry0023 = tk.Entry(right_frame, font=40)
                        entry0023.place(relx=0.39, rely=0.89, relwidth=0.25, relheight=0.1)

                        next_button0023 = tk.Button(right_frame, text='Check', bg='lightblue', command=lambda : checktrans_button(entry0023.get()))
                        next_button0023.place(relx=0.69, rely=0.89, relwidth=0.3, relheight=0.1)#locate it and size it. 

                        def checktrans_button(entry0023):
                            x = entry0023.upper()
                            lower_frame0023lastelse = tk.Frame(root, bg='HotPink4')
                            lower_frame0023lastelse.place(relx=0.09, rely=0.85, relwidth=0.85, relheight=0.13)#locate it and size it. 
                            entry233 = tk.Entry(lower_frame0023lastelse, font=40)
                            entry233.place(relx=0.45, rely=0.15, relwidth=0.35, relheight=0.5)
                            
                            plane_cost = "This will cost you 1790"
                            bus_cost = "This will cost you 650"

                            if x=='PLANE':
                                entry233.insert(0, plane_cost)
                            elif x=='BUS':
                                entry233.insert(0, bus_cost)
                            else:
                                lower_frame11 = tk.Frame(root, bg='HotPink4')
                                lower_frame11.place(relx=0.09, rely=0.85, relwidth=0.85, relheight=0.13)#locate it and size it. 
                                entry_warning11 = tk.Entry(lower_frame11, font=('Arial',11))
                                entry_warning11.place(relx=0.1, rely=0.1, relwidth=0.8, relheight=0.6)
                                warning11 = "You have entered wrong value . -Please choose plane or bus- "
                                entry_warning11.insert(0, warning11)
           

                    else:
                        lower_frame15 = tk.Frame(root, bg='HotPink4')
                        lower_frame15.place(relx=0.09, rely=0.85, relwidth=0.85, relheight=0.13)#locate it and size it. 
                        entry_warning15 = tk.Entry(lower_frame15, font=('Arial',11))
                        entry_warning15.place(relx=0.1, rely=0.1, relwidth=0.8, relheight=0.6)
                        warning15 = "You have entered wrong value . -Please Enter number from the list- "
                        entry_warning15.insert(0, warning15)

                except:
                    lower_frame14 = tk.Frame(root, bg='HotPink4')
                    lower_frame14.place(relx=0.09, rely=0.85, relwidth=0.85, relheight=0.13)#locate it and size it. 

                    entry_warning14 = tk.Entry(lower_frame14, font=('Arial',11))
                    entry_warning14.place(relx=0.1, rely=0.1, relwidth=0.8, relheight=0.6)
                    warning14 = "You have entered wrong value . Please try again . - Enter the number-"
                    entry_warning14.insert(0, warning14)







        elif t=='3':
            label9 = tk.Label(right_frame, text=' choice the number of country you want to go..', font=("Arial",11))
            label9.place(relx=0.07, rely=0.05, relwidth=0.87, relheight=0.1)#locate it and size it. 

            label10 = tk.Label(right_frame, text="""1.Saudi Arabia \n2.UAE \n3.Bahrain """, font=("Arial",15), fg='OrangeRed2')
            label10.place(relx=0.07, rely=0.17, relwidth=0.8, relheight=0.4)

            entryKWD = tk.Entry(right_frame, font=40)
            entryKWD.place(relx=0.08, rely=0.6 ,relwidth=0.5, relheight=0.1) #locate it and size it.                              

            lower_frame31 = tk.Frame(root, bg='HotPink4')
            lower_frame31.place(relx=0.09, rely=0.85, relwidth=0.85, relheight=0.13)#locate it and size it. 

            next_button32 = tk.Button(right_frame, text='Next', bg='lightblue',command=lambda : des_entry(entryKWD.get()))
            next_button32.place(relx=0.65, rely=0.6 ,relwidth=0.3, relheight=0.1)

            def des_entry(entryKWD):
                y = entryKWD

                try:
                    if y=='1':
                        lower_frame0031 = tk.Frame(root, bg='HotPink4')
                        lower_frame0031.place(relx=0.09, rely=0.85, relwidth=0.85, relheight=0.13)#locate it and size it. 
                     
                        label0031 = tk.Label(right_frame, text="would you like to travel by \n PLANE or BUS", font=('Arial',13))
                        label0031.place(relx=0.15, rely=0.72 ,relwidth=0.7, relheight=0.15)

                        label00311 = tk.Label(right_frame, text='Enter it here:-', font=("Arial",10))
                        label00311.place(relx=0.05, rely=0.89, relwidth=0.3, relheight=0.1)#locate it and size it. 

                        entry0031 = tk.Entry(right_frame, font=40)
                        entry0031.place(relx=0.39, rely=0.89, relwidth=0.25, relheight=0.1)

                        next_button0031 = tk.Button(right_frame, text='Check', bg='lightblue', command=lambda : checktrans_button(entry0031.get()))
                        next_button0031.place(relx=0.69, rely=0.89, relwidth=0.3, relheight=0.1)#locate it and size it. 

                        def checktrans_button(entry0031):
                            x = entry0031.upper()
                            lower_frame0031lastelse = tk.Frame(root, bg='HotPink4')
                            lower_frame0031lastelse.place(relx=0.09, rely=0.85, relwidth=0.85, relheight=0.13)
                            entry313 = tk.Entry(lower_frame0031lastelse, font=40)
                            entry313.place(relx=0.45, rely=0.15, relwidth=0.35, relheight=0.5)#locate it and size it. 
                            
                            plane_cost = "This will cost you 1220"
                            bus_cost = "This will cost you 651"

                            if x=='PLANE':
                                entry313.insert(0, plane_cost)
                            elif x=='BUS':
                                entry313.insert(0, bus_cost)
                            else:
                                lower_frame16 = tk.Frame(root, bg='HotPink4')
                                lower_frame16.place(relx=0.09, rely=0.85, relwidth=0.85, relheight=0.13)#locate it and size it. 
                                entry_warning16 = tk.Entry(lower_frame16, font=('Arial',11))
                                entry_warning16.place(relx=0.1, rely=0.1, relwidth=0.8, relheight=0.6)
                                warning16 = "You have entered wrong value . -Please choose plane or bus- "
                                entry_warning16.insert(0, warning16)

                    elif y=='2':
                        lower_frame0032 = tk.Frame(root, bg='HotPink4')
                        lower_frame0032.place(relx=0.09, rely=0.85, relwidth=0.85, relheight=0.13)#locate it and size it. 
                     
                        label0032 = tk.Label(right_frame, text="would you like to travel by \n PLANE or BUS", font=('Arial',13))
                        label0032.place(relx=0.15, rely=0.72 ,relwidth=0.7, relheight=0.15)

                        label00321 = tk.Label(right_frame, text='Enter it here:-', font=("Arial",10))
                        label00321.place(relx=0.05, rely=0.89, relwidth=0.3, relheight=0.1)#locate it and size it. 

                        entry0032 = tk.Entry(right_frame, font=40)
                        entry0032.place(relx=0.39, rely=0.89, relwidth=0.25, relheight=0.1)

                        next_button0032 = tk.Button(right_frame, text='Check', bg='lightblue', command=lambda : checktrans_button(entry0032.get()))
                        next_button0032.place(relx=0.69, rely=0.89, relwidth=0.3, relheight=0.1)#locate it and size it. 

                        def checktrans_button(entry0032):
                            x = entry0032.upper()
                            lower_frame0032lastelse = tk.Frame(root, bg='HotPink4')
                            lower_frame0032lastelse.place(relx=0.09, rely=0.85, relwidth=0.85, relheight=0.13)
                            entry323 = tk.Entry(lower_frame0032lastelse, font=40)
                            entry323.place(relx=0.45, rely=0.15, relwidth=0.35, relheight=0.5)#locate it and size it. 
                            
                            plane_cost = "This will cost you 1350"
                            bus_cost = "This will cost you 790"

                            if x=='PLANE':
                                entry323.insert(0, plane_cost)
                            elif x=='BUS':
                                entry323.insert(0, bus_cost)
                            else:
                                lower_frame17 = tk.Frame(root, bg='HotPink4')
                                lower_frame17.place(relx=0.09, rely=0.85, relwidth=0.85, relheight=0.13)#locate it and size it. 
                                entry_warning17 = tk.Entry(lower_frame17, font=('Arial',11))
                                entry_warning17.place(relx=0.1, rely=0.1, relwidth=0.8, relheight=0.6)
                                warning17 = "You have entered wrong value . -Please choose plane or bus- "
                                entry_warning17.insert(0, warning17)

                    elif y=='3':
                        lower_frame0033 = tk.Frame(root, bg='HotPink4')
                        lower_frame0033.place(relx=0.09, rely=0.85, relwidth=0.85, relheight=0.13)#locate it and size it. 
                     
                        label0033 = tk.Label(right_frame, text="would you like to travel by \n PLANE or BUS", font=('Arial',13))
                        label0033.place(relx=0.15, rely=0.72 ,relwidth=0.7, relheight=0.15)

                        label00331 = tk.Label(right_frame, text='Enter it here:-', font=("Arial",10))
                        label00331.place(relx=0.05, rely=0.89, relwidth=0.3, relheight=0.1)#locate it and size it. 

                        entry0033 = tk.Entry(right_frame, font=40)
                        entry0033.place(relx=0.39, rely=0.89, relwidth=0.25, relheight=0.1)

                        next_button0033 = tk.Button(right_frame, text='Check', bg='lightblue', command=lambda : checktrans_button(entry0033.get()))
                        next_button0033.place(relx=0.69, rely=0.89, relwidth=0.3, relheight=0.1)#locate it and size it. 

                        def checktrans_button(entry0033):
                            x = entry0033.upper()
                            lower_frame0033lastelse = tk.Frame(root, bg='HotPink4')
                            lower_frame0033lastelse.place(relx=0.09, rely=0.85, relwidth=0.85, relheight=0.13)#locate it and size it. 
                            entry333 = tk.Entry(lower_frame0033lastelse, font=40)
                            entry333.place(relx=0.45, rely=0.15, relwidth=0.35, relheight=0.5)#locate it and size it. 
                            
                            plane_cost = "This will cost you 1550"
                            bus_cost = "This will cost you 730"

                            if x=='PLANE':
                                entry333.insert(0, plane_cost)
                            elif x=='BUS':
                                entry333.insert(0, bus_cost)
                            else:
                                lower_frame18 = tk.Frame(root, bg='HotPink4')
                                lower_frame18.place(relx=0.09, rely=0.85, relwidth=0.85, relheight=0.13)#locate it and size it. 
                                entry_warning18 = tk.Entry(lower_frame18, font=('Arial',11))
                                entry_warning18.place(relx=0.1, rely=0.1, relwidth=0.8, relheight=0.6)
                                warning18 = "You have entered wrong value . -Please choose plane or bus- "
                                entry_warning18.insert(0, warning18)
              


                    else:
                        lower_frame211 = tk.Frame(root, bg='HotPink4')
                        lower_frame211.place(relx=0.09, rely=0.85, relwidth=0.85, relheight=0.13)
                        entry_warning211 = tk.Entry(lower_frame211, font=('Arial',11))
                        entry_warning211.place(relx=0.1, rely=0.1, relwidth=0.8, relheight=0.6)
                        warning211 = "You have entered wrong value . -Please Enter number from the list- "
                        entry_warning211.insert(0, warning211)

                except:
                    lower_frame22 = tk.Frame(root, bg='HotPink4')
                    lower_frame22.place(relx=0.09, rely=0.85, relwidth=0.85, relheight=0.13)

                    entry_warning22 = tk.Entry(lower_frame22, font=('Arial',11))
                    entry_warning22.place(relx=0.1, rely=0.1, relwidth=0.8, relheight=0.6)
                    warning22 = "You have entered wrong value . Please try again . - Enter the number-"
                    entry_warning22.insert(0, warning22)


        elif t=='4':
            label11 = tk.Label(right_frame, text=' choice the number of country you want to go..', font=("Arial",11))
            label11.place(relx=0.07, rely=0.05, relwidth=0.87, relheight=0.1)

            label12 = tk.Label(right_frame, text="""1.Saudi Arabia \n2.UAE \n3.Kuwait """, font=("Arial",15), fg='OrangeRed2')
            label12.place(relx=0.07, rely=0.17, relwidth=0.8, relheight=0.4)

            entryBHD = tk.Entry(right_frame, font=40)
            entryBHD.place(relx=0.08, rely=0.6 ,relwidth=0.5, relheight=0.1)                              

            lower_frame41 = tk.Frame(root, bg='HotPink4')
            lower_frame41.place(relx=0.09, rely=0.85, relwidth=0.85, relheight=0.13)

            next_button42 = tk.Button(right_frame, text='Next', bg='lightblue',command=lambda : des_entry(entryBHD.get()))
            next_button42.place(relx=0.65, rely=0.6 ,relwidth=0.3, relheight=0.1)

            def des_entry(entryBHD):
                y = entryBHD
                try:
                    if y=='1':
                        lower_frame0041 = tk.Frame(root, bg='HotPink4')
                        lower_frame0041.place(relx=0.09, rely=0.85, relwidth=0.85, relheight=0.13)
                     
                        label0041 = tk.Label(right_frame, text="would you like to travel by \n PLANE or BUS", font=('Arial',13))
                        label0041.place(relx=0.15, rely=0.72 ,relwidth=0.7, relheight=0.15)

                        label00411 = tk.Label(right_frame, text='Enter it here:-', font=("Arial",10))
                        label00411.place(relx=0.05, rely=0.89, relwidth=0.3, relheight=0.1)

                        entry0041 = tk.Entry(right_frame, font=40)
                        entry0041.place(relx=0.39, rely=0.89, relwidth=0.25, relheight=0.1)

                        next_button0041 = tk.Button(right_frame, text='Check', bg='lightblue', command=lambda : checktrans_button(entry0041.get()))
                        next_button0041.place(relx=0.69, rely=0.89, relwidth=0.3, relheight=0.1)

                        def checktrans_button(entry0041):
                            x = entry0041.upper()
                            lower_frame0041lastelse = tk.Frame(root, bg='HotPink4')
                            lower_frame0041lastelse.place(relx=0.09, rely=0.85, relwidth=0.85, relheight=0.13)
                            entry413 = tk.Entry(lower_frame0041lastelse, font=40)
                            entry413.place(relx=0.45, rely=0.15, relwidth=0.35, relheight=0.5)
                            
                            plane_cost = "This will cost you 2350"
                            bus_cost = "This will cost you 1150"

                            if x=='PLANE':
                                entry413.insert(0, plane_cost)
                            elif x=='BUS':
                                entry413.insert(0, bus_cost)
                            else:
                                lower_frame23 = tk.Frame(root, bg='HotPink4')
                                lower_frame23.place(relx=0.09, rely=0.85, relwidth=0.85, relheight=0.13)
                                entry_warning23 = tk.Entry(lower_frame23, font=('Arial',11))
                                entry_warning23.place(relx=0.1, rely=0.1, relwidth=0.8, relheight=0.6)
                                warning23 = "You have entered wrong value . -Please choose plane or bus- "
                                entry_warning23.insert(0, warning23)


                    elif y=='2':
                        lower_frame0042 = tk.Frame(root, bg='HotPink4')
                        lower_frame0042.place(relx=0.09, rely=0.85, relwidth=0.85, relheight=0.13)
                     
                        label0042 = tk.Label(right_frame, text="would you like to travel by \n PLANE or BUS", font=('Arial',13))
                        label0042.place(relx=0.15, rely=0.72 ,relwidth=0.7, relheight=0.15)

                        label00421 = tk.Label(right_frame, text='Enter it here:-', font=("Arial",10))
                        label00421.place(relx=0.05, rely=0.89, relwidth=0.3, relheight=0.1)

                        entry0042 = tk.Entry(right_frame, font=40)
                        entry0042.place(relx=0.39, rely=0.89, relwidth=0.25, relheight=0.1)

                        next_button0042 = tk.Button(right_frame, text='Check', bg='lightblue', command=lambda : checktrans_button(entry0042.get()))
                        next_button0042.place(relx=0.69, rely=0.89, relwidth=0.3, relheight=0.1)


                        def checktrans_button(entry0042):
                            x = entry0042.upper()
                            lower_frame0042lastelse = tk.Frame(root, bg='HotPink4')
                            lower_frame0042lastelse.place(relx=0.09, rely=0.85, relwidth=0.85, relheight=0.13)
                            entry423 = tk.Entry(lower_frame0042lastelse, font=40)
                            entry423.place(relx=0.45, rely=0.15, relwidth=0.35, relheight=0.5)
                            
                            plane_cost = "This will cost you 2350"
                            bus_cost = "This will cost you 1150"

                            if x=='PLANE':
                                entry423.insert(0, plane_cost)
                            elif x=='BUS':
                                entry423.insert(0, bus_cost)
                            else:
                                lower_frame24 = tk.Frame(root, bg='HotPink4')
                                lower_frame24.place(relx=0.09, rely=0.85, relwidth=0.85, relheight=0.13)
                                entry_warning24 = tk.Entry(lower_frame24, font=('Arial',11))
                                entry_warning24.place(relx=0.1, rely=0.1, relwidth=0.8, relheight=0.6)
                                warning24 = "You have entered wrong value . -Please choose plane or bus- "
                                entry_warning24.insert(0, warning24)



                    elif y=='3':
                        lower_frame0043 = tk.Frame(root, bg='HotPink4')
                        lower_frame0043.place(relx=0.09, rely=0.85, relwidth=0.85, relheight=0.13)
                     
                        label0043 = tk.Label(right_frame, text="would you like to travel by \n PLANE or BUS", font=('Arial',13))
                        label0043.place(relx=0.15, rely=0.72 ,relwidth=0.7, relheight=0.15)

                        label00431 = tk.Label(right_frame, text='Enter it here:-', font=("Arial",10))
                        label00431.place(relx=0.05, rely=0.89, relwidth=0.3, relheight=0.1)

                        entry0043 = tk.Entry(right_frame, font=40)
                        entry0043.place(relx=0.39, rely=0.89, relwidth=0.25, relheight=0.1)

                        next_button0043 = tk.Button(right_frame, text='Check', bg='lightblue', command=lambda : checktrans_button(entry0043.get()))
                        next_button0043.place(relx=0.69, rely=0.89, relwidth=0.3, relheight=0.1)


                        def checktrans_button(entry0043):
                            x = entry0043.upper()
                            lower_frame0043lastelse = tk.Frame(root, bg='HotPink4')
                            lower_frame0043lastelse.place(relx=0.09, rely=0.85, relwidth=0.85, relheight=0.13)
                            entry433 = tk.Entry(lower_frame0043lastelse, font=40)
                            entry433.place(relx=0.45, rely=0.15, relwidth=0.35, relheight=0.5)
                            
                            plane_cost = "This will cost you 2350"
                            bus_cost = "This will cost you 1150"

                            if x=='PLANE':
                                entry433.insert(0, plane_cost)
                            elif x=='BUS':
                                entry433.insert(0, bus_cost)
                            else:
                                lower_frame25 = tk.Frame(root, bg='HotPink4')
                                lower_frame25.place(relx=0.09, rely=0.85, relwidth=0.85, relheight=0.13)
                                entry_warning25 = tk.Entry(lower_frame25, font=('Arial',11))
                                entry_warning25.place(relx=0.1, rely=0.1, relwidth=0.8, relheight=0.6)
                                warning25 = "You have entered wrong value . -Please choose plane or bus- "
                                entry_warning25.insert(0, warning25)



                    else:
                        lower_frame28 = tk.Frame(root, bg='HotPink4')
                        lower_frame28.place(relx=0.09, rely=0.85, relwidth=0.85, relheight=0.13)
                        entry_warning28 = tk.Entry(lower_frame28, font=('Arial',11))
                        entry_warning28.place(relx=0.1, rely=0.1, relwidth=0.8, relheight=0.6)
                        warning28 = "You have entered wrong value . -Please Enter number from the list- "
                        entry_warning28.insert(0, warning28)

                except:
                    lower_frame29 = tk.Frame(root, bg='HotPink4')
                    lower_frame29.place(relx=0.09, rely=0.85, relwidth=0.85, relheight=0.13)

                    entry_warning29 = tk.Entry(lower_frame29, font=('Arial',11))
                    entry_warning29.place(relx=0.1, rely=0.1, relwidth=0.8, relheight=0.6)
                    warning29 = "You have entered wrong value . Please try again . - Enter the number-"
                    entry_warning29.insert(0, warning29)


        else:
            entry_warning1 = tk.Entry(lower_frame, font=40)
            entry_warning1.place(relx=0.1, rely=0.1, relwidth=0.8, relheight=0.6)
            warning1 = 'You have entered wrong value .. Please try again'
            entry_warning1.insert(0, warning1)


    root.mainloop()

