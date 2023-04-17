#Currency Exchange widow 

import tkinter as tk #tk because it make it easire to use
from tkinter import Label  #importing the label 

#create a function for the currency exchange window

def currency_window():
    #window
    root = tk.Toplevel()  #use tkinter to build our window
    root.title('Currency Exchange') #the title of the window
    root.geometry('750x500') #geometry() is for measuring the window


    background_label = tk.Label(root, bg='turquoise4')#name a vatiable for the background label. and located in the root and choose the background color 
    background_label.place(relx=0, rely=0, relwidth=1 , relheight=1 ) #locate it and size it. 

    upper_frame = tk.Frame(root, bg='HotPink4') #name a variable for the frame and located in the root, and use Frame() function to do the frame
    upper_frame.place(relx=0.09, rely=0.02, relwidth=0.85, relheight=0.1)#locate it and size it.

    
    left_frame = tk.Frame(root,  bg='lightcyan2') #name a variable for the frame and located in the root, and use Frame() function to do the frame
    left_frame.place(relx=0.05, rely=0.13, relwidth=0.45, relheight=0.7)#locate it and size it.


    label0 = tk.Label(upper_frame, text='Currency Exchange', font=("Arial",30))#name a vatiable for the label. and located in the upper frame. And set its properties.
    label0.pack()#locate it 


    label2 = tk.Label(left_frame, text="""From the list below choose the number of 
    the currency you want to convert.""", font=("Arial",12), fg='Darkorchid4')#name a vatiable for the label. and located in the left frame. And set its properties.
    label2.place(relx=0.05, rely=0.04, relwidth=0.89, relheight=0.1)#locate it and size it.

   #now start do the currency list 

    label3 = tk.Label(left_frame, text="""Currency List :
 1.Saudi Riyal 
 2.Kuwaiti Dinar
 3.The UAE Dirham
 4.Omani Riyal
 5.Qatari Riyal
 6.Bahraini Dinar
 ..Other..
 7.American Dollar
 8.Euro""", font=("Arial",15), fg='OrangeRed2')#name a vatiable for the label. and located in the left frame. And set its properties.

    label3.place(relx=0.05, rely=0.15, relwidth=0.7, relheight=0.65)#locate it and size it.



    label4 = tk.Label(left_frame, text='Enter it here:-', font=("Arial",10))#name a vatiable for the label. and located in the left frame. And set its properties.
    label4.place(relx=0.05, rely=0.83, relwidth=0.3, relheight=0.1)#locate it and size it.



    entry1 = tk.Entry(left_frame, font=40)
    entry1.place(relx=0.39, rely=0.83, relwidth=0.25, relheight=0.1)#locate it and size it.
    

    next_button1 = tk.Button(left_frame, text='Next', bg='lightblue', command=lambda : counting_amount(entry1.get()))
    next_button1.place(relx=0.69, rely=0.89, relwidth=0.3, relheight=0.1)#locate it and size it.


    right_frame = tk.Frame(root, bg='lightcyan2') #name a variable for the frame and located in the root, and use Frame() function to do the frame
    right_frame.place(relx=0.53, rely=0.13, relwidth=0.45, relheight=0.7)#locate it and size it.


    lower_frame = tk.Frame(root, bg='HotPink4') #name a variable for the frame and located in the root, and use Frame() function to do the frame
    lower_frame.place(relx=0.09, rely=0.85, relwidth=0.85, relheight=0.13)#locate it and size it.
   

   #create a function that is gets what inside the entry1.. and then checks that is from the list or not.

    def counting_amount(entry1):#define the function
           
            k = entry1 #entry1 is the entry for the choice from the currency list
 
            if k=='1':
               label5 = tk.Label(right_frame, text='Enter the amount of money in Saudi Riyal..', font=("Arial",11))#name a vatiable for the label. and located in the right frame. And set its properties.
               label5.place(relx=0.02, rely=0.05, relwidth=0.83, relheight=0.1)#locate it and size it.

               entrySAR = tk.Entry(right_frame, font=40)
               entrySAR.place(relx=0.02, rely=0.16 ,relwidth=0.5, relheight=0.1)#locate it and size it.                           


               lower_frame1 = tk.Frame(root, bg='HotPink4') #name a variable for the frame and located in the root, and use Frame() function to do the frame
               lower_frame1.place(relx=0.09, rely=0.85, relwidth=0.85, relheight=0.13)#locate it and size it.
               
               next_button2 = tk.Button(right_frame, text='Next', bg='lightblue', command=lambda : money_entry(entrySAR.get()))
               next_button2.place(relx=0.65, rely=0.16 ,relwidth=0.3, relheight=0.1)#locate it and size it.
                
               #create a function that know if the user user entered numbers for the money or not .

               def money_entry(entrySAR):
                  y = entrySAR
                  try:
                     if int(y):
                        lower_frame00 = tk.Frame(root, bg='HotPink4')
                        lower_frame00.place(relx=0.09, rely=0.85, relwidth=0.85, relheight=0.13)#locate it and size it.
                     
                        label6 = tk.Label(right_frame, text="what you want to convert to", font=('Arial',13))#name a vatiable for the label. and located in the right frame. And set its properties.
                        label6.place(relx=0.1, rely=0.27 ,relwidth=0.65, relheight=0.1)#locate it and size it.

                        label7 = tk.Label(right_frame, text="""choice from the list: 
   AED,United Arab Emirates\n BHD,Bahraini Dinar\n QAR,Qatari Riyal\n KWD,Kuwaiti Dinar\n USD,United States of America\n EUR,Euro\n OMR,Omani Riyal\n""", font=('Arial',13))#name a vatiable for the label. and located in the right frame. And set its properties.
                        label7.place(relx=0.1, rely=0.38 ,relwidth=0.8, relheight=0.4)#locate it and size it.

                        label8 = tk.Label(right_frame, text='Enter it here:-', font=("Arial",10))#name a vatiable for the label. and located in the right frame. And set its properties.
                        label8.place(relx=0.05, rely=0.83, relwidth=0.3, relheight=0.1)#locate it and size it.

                        entry2 = tk.Entry(right_frame, font=40)
                        entry2.place(relx=0.39, rely=0.83, relwidth=0.25, relheight=0.1)#locate it and size it.

                        next_button3 = tk.Button(right_frame, text='Convert', bg='lightblue', command=lambda : convert_button(entry2.get()))
                        next_button3.place(relx=0.69, rely=0.89, relwidth=0.3, relheight=0.1)#locate it and size it.

                        #create a function thats knows the user choice in the second list 

                        def convert_button(entry2):
                           y = int(entrySAR)
                           x = entry2.upper()
                           lower_frame00lastelse = tk.Frame(root, bg='HotPink4') #name a variable for the frame and located in the root, and use Frame() function to do the frame
                           lower_frame00lastelse.place(relx=0.09, rely=0.85, relwidth=0.85, relheight=0.13)#locate it and size it.
                           entry3 = tk.Entry(lower_frame00lastelse, font=40)
                           entry3.place(relx=0.45, rely=0.15, relwidth=0.35, relheight=0.5)#locate it and size it.
                           
                           AED=y*0.98   
                           BHD=y*0.10   
                           QAR=y*0.97   
                           KWD=y*0.082  
                           USD=y*0.27   
                           EUR=y*0.23   
                           OMR=y*0.10

                           if x=="AED":
                              entry3.insert(0, round(AED,2))                        
                           elif x=="BHD":
                              entry3.insert(0, round(BHD,2)) 
                           elif x=="QAR":
                              entry3.insert(0, round(QAR,2)) 
                           elif x=="KWD":
                              entry3.insert(0, round(KWD,2))
                           elif x=="USD":
                              entry3.insert(0, round(USD,2))
                           elif x=="EUR":
                              entry3.insert(0, round(EUR,2))
                           elif x=="OMR":
                              entry3.insert(0, round(OMR,2))
                           else:
                              lower_frame3 = tk.Frame(root, bg='HotPink4') #name a variable for the frame and located in the root, and use Frame() function to do the frame
                              lower_frame3.place(relx=0.09, rely=0.85, relwidth=0.85, relheight=0.13)#locate it and size it.
                              entry_warning3 = tk.Entry(lower_frame3, font=('Arial',11))
                              entry_warning3.place(relx=0.1, rely=0.1, relwidth=0.8, relheight=0.6)#locate it and size it.
                              warning3 = "You have entered wrong value . - Please Enter currency's short form name - "
                              entry_warning3.insert(0, warning3)

                  except:
                     lower_frame2 = tk.Frame(root, bg='HotPink4') #name a variable for the frame and located in the root, and use Frame() function to do the frame
                     lower_frame2.place(relx=0.09, rely=0.85, relwidth=0.85, relheight=0.13)#locate it and size it.

                     entry_warning2 = tk.Entry(lower_frame2, font=('Arial',11))
                     entry_warning2.place(relx=0.1, rely=0.1, relwidth=0.8, relheight=0.6)#locate it and size it.
                     warning2 = "You have entered wrong value . Please try again . - Enter an integer number-"
                     entry_warning2.insert(0, warning2)






            elif k=='2':
               label21 = tk.Label(right_frame, text='Enter the amount of money in Kuwaiti Dinar..', font=("Arial",11))#name a vatiable for the label. and located in the right frame. And set its properties.
               label21.place(relx=0.02, rely=0.05, relwidth=0.85, relheight=0.1)#locate it and size it.

               entryKWD = tk.Entry(right_frame, font=40)
               entryKWD.place(relx=0.02, rely=0.16 ,relwidth=0.5, relheight=0.1) #locate it and size it.                            


               lower_frame21 = tk.Frame(root, bg='HotPink4') #name a variable for the frame and located in the root, and use Frame() function to do the frame
               lower_frame21.place(relx=0.09, rely=0.85, relwidth=0.85, relheight=0.13)#locate it and size it.
               
               next_button21 = tk.Button(right_frame, text='Next', bg='lightblue', command=lambda : money_entry(entryKWD.get()))
               next_button21.place(relx=0.65, rely=0.16 ,relwidth=0.3, relheight=0.1)#locate it and size it.

               def money_entry(entryKWD):
                  y = entryKWD
                  try:
                     if int(y):
                        lower_frame01 = tk.Frame(root, bg='HotPink4')#name a variable for the frame and located in the root, and use Frame() function to do the frame
                        lower_frame01.place(relx=0.09, rely=0.85, relwidth=0.85, relheight=0.13)#locate it and size it.

                        label22 = tk.Label(right_frame, text="what you want to convert to", font=('Arial',13))#name a vatiable for the label. and located in the right frame. And set its properties.
                        label22.place(relx=0.1, rely=0.27 ,relwidth=0.65, relheight=0.1)#locate it and size it.

                        label23 = tk.Label(right_frame, text="""choice from the list: 
  AED,United Arab Emirates\n BHD,Bahraini Dinar\n QAR,Qatari Riyal\n SAR,Saudi Riyal\n USD,United States of America\n EUR,Euro\n OMR,Omani Riyal\n""", font=('Arial',13))#name a vatiable for the label. and located in the right frame. And set its properties.
                        label23.place(relx=0.1, rely=0.38 ,relwidth=0.8, relheight=0.4)#locate it and size it.

                        label24 = tk.Label(right_frame, text='Enter it here:-', font=("Arial",10))#name a vatiable for the label. and located in the right frame. And set its properties.
                        label24.place(relx=0.05, rely=0.83, relwidth=0.3, relheight=0.1)#locate it and size it.

                        entry21 = tk.Entry(right_frame, font=40)
                        entry21.place(relx=0.39, rely=0.83, relwidth=0.25, relheight=0.1)#locate it and size it.

                        next_button22 = tk.Button(right_frame, text='Convert', bg='lightblue', command=lambda : convert_button(entry21.get()))
                        next_button22.place(relx=0.69, rely=0.89, relwidth=0.3, relheight=0.1)#locate it and size it.

                        def convert_button(entry21):
                           y = int(entryKWD)
                           x = entry21.upper()
                           lower_frame001lastelse = tk.Frame(root, bg='HotPink4')#name a variable for the frame and located in the root, and use Frame() function to do the frame
                           lower_frame001lastelse.place(relx=0.09, rely=0.85, relwidth=0.85, relheight=0.13)#locate it and size it.
                           entry31 = tk.Entry(lower_frame001lastelse, font=40)
                           entry31.place(relx=0.45, rely=0.15, relwidth=0.35, relheight=0.5)#locate it and size it.

                           SAR=y*12.27
                           AED=y*12.02
                           OMR=y*1.26
                           QAR=y*11.91
                           BHD=y*1.23
                           USD=y*3.27
                           EUR=y*2.77

                           if x=="AED":
                              entry31.insert(0, round(AED,2))                        
                           elif x=="BHD":
                              entry31.insert(0, round(BHD,2)) 
                           elif x=="QAR":
                              entry31.insert(0, round(QAR,2)) 
                           elif x=="SAR":
                              entry31.insert(0, round(SAR,2))
                           elif x=="USD":
                              entry31.insert(0, round(USD,2))
                           elif x=="EUR":
                              entry31.insert(0, round(EUR,2))
                           elif x=="OMR":
                              entry31.insert(0, round(OMR,2))
                           else:
                              lower_frame23 = tk.Frame(root, bg='HotPink4')#name a variable for the frame and located in the root, and use Frame() function to do the frame
                              lower_frame23.place(relx=0.09, rely=0.85, relwidth=0.85, relheight=0.13)#locate it and size it.

                              entry_warning4 = tk.Entry(lower_frame23, font=('Arial',11))
                              entry_warning4.place(relx=0.1, rely=0.1, relwidth=0.8, relheight=0.6)#locate it and size it.
                              warning4 = "You have entered wrong value . - Please Enter currency's short form name - "
                              entry_warning4.insert(0, warning4)

                  except:
                     lower_frame22 = tk.Frame(root, bg='HotPink4')#name a variable for the frame and located in the root, and use Frame() function to do the frame
                     lower_frame22.place(relx=0.09, rely=0.85, relwidth=0.85, relheight=0.13)#locate it and size it.

                     entry_warning5 = tk.Entry(lower_frame22, font=('Arial',11))
                     entry_warning5.place(relx=0.1, rely=0.1, relwidth=0.8, relheight=0.6)#locate it and size it.
                     warning5 = "You have entered wrong value . Please try again . - Enter an integer number-"
                     entry_warning5.insert(0, warning5)






            elif k=='3':
               label31 = tk.Label(right_frame, text='Enter the amount of money in UAE Dirham..', font=("Arial",11))#name a vatiable for the label. and located in the right frame. And set its properties.
               label31.place(relx=0.02, rely=0.05, relwidth=0.83, relheight=0.1)#locate it and size it.

               entryAED = tk.Entry(right_frame, font=40)
               entryAED.place(relx=0.02, rely=0.16 ,relwidth=0.5, relheight=0.1) #locate it and size it.                             


               lower_frame31 = tk.Frame(root, bg='HotPink4')#name a variable for the frame and located in the root, and use Frame() function to do the frame
               lower_frame31.place(relx=0.09, rely=0.85, relwidth=0.85, relheight=0.13)#locate it and size it.
               
               next_button31 = tk.Button(right_frame, text='Next', bg='lightblue', command=lambda : money_entry(entryAED.get()))
               next_button31.place(relx=0.65, rely=0.16 ,relwidth=0.3, relheight=0.1)#locate it and size it.

               def money_entry(entryAED):
                  y = entryAED
                  try:
                     if int(y):
                        lower_frame003 = tk.Frame(root, bg='HotPink4')#name a variable for the frame and located in the root, and use Frame() function to do the frame
                        lower_frame003.place(relx=0.09, rely=0.85, relwidth=0.85, relheight=0.13)#locate it and size it.
                     
                        label32 = tk.Label(right_frame, text="what you want to convert to", font=('Arial',13))#name a vatiable for the label. and located in the right frame. And set its properties.
                        label32.place(relx=0.1, rely=0.27 ,relwidth=0.65, relheight=0.1)#locate it and size it.

                        label33 = tk.Label(right_frame, text="""choice from the list: 
   SAR,Saudi Riyal\n BHD,Bahraini Dinar\n QAR,Qatari Riyal\n KWD,Kuwaiti Dinar\n USD,United States of America\n EUR,Euro\n OMR,Omani Riyal\n""", font=('Arial',13))
                        label33.place(relx=0.1, rely=0.38 ,relwidth=0.8, relheight=0.4)#locate it and size it.

                        label34 = tk.Label(right_frame, text='Enter it here:-', font=("Arial",10))
                        label34.place(relx=0.05, rely=0.83, relwidth=0.3, relheight=0.1)#locate it and size it.

                        entry32 = tk.Entry(right_frame, font=40)
                        entry32.place(relx=0.39, rely=0.83, relwidth=0.25, relheight=0.1)#locate it and size it.

                        next_button32 = tk.Button(right_frame, text='Convert', bg='lightblue', command=lambda : convert_button(entry32.get()))
                        next_button32.place(relx=0.69, rely=0.89, relwidth=0.3, relheight=0.1)#locate it and size it.

                        def convert_button(entry32):
                           y = int(entryAED)
                           x = entry32.upper()
                           lower_frame002lastelse = tk.Frame(root, bg='HotPink4')#name a variable for the frame and located in the root, and use Frame() function to do the frame
                           lower_frame002lastelse.place(relx=0.09, rely=0.85, relwidth=0.85, relheight=0.13)#locate it and size it.
                           entry33 = tk.Entry(lower_frame002lastelse, font=40)
                           entry33.place(relx=0.45, rely=0.15, relwidth=0.35, relheight=0.5)#locate it and size it.
                           
                           SAR=y*1.02
                           KWD=y*0.083
                           OMR=y*0.10
                           QAR=y*0.99
                           BHD=y*0.10
                           USD=y*0.27
                           EUR=y*0.23

                           if x=="KWD":
                              entry33.insert(0, round(KWD,2))                        
                           elif x=="BHD":
                              entry33.insert(0, round(BHD,2)) 
                           elif x=="QAR":
                              entry33.insert(0, round(QAR,2)) 
                           elif x=="SAR":
                              entry33.insert(0, round(SAR,2))
                           elif x=="USD":
                              entry33.insert(0, round(USD,2))
                           elif x=="EUR":
                              entry33.insert(0, round(EUR,2))
                           elif x=="OMR":
                              entry33.insert(0, round(OMR,2))
                           else:
                              lower_frame33 = tk.Frame(root, bg='HotPink4')#name a variable for the frame and located in the root, and use Frame() function to do the frame
                              lower_frame33.place(relx=0.09, rely=0.85, relwidth=0.85, relheight=0.13)#locate it and size it.

                              entry_warning6 = tk.Entry(lower_frame33, font=('Arial',11))
                              entry_warning6.place(relx=0.1, rely=0.1, relwidth=0.8, relheight=0.6)#locate it and size it.
                              warning6 = "You have entered wrong value . - Please Enter currency's short form name - "
                              entry_warning6.insert(0, warning6)

                  except:
                     lower_frame34 = tk.Frame(root, bg='HotPink4')#name a variable for the frame and located in the root, and use Frame() function to do the frame
                     lower_frame34.place(relx=0.09, rely=0.85, relwidth=0.85, relheight=0.13)#locate it and size it.

                     entry_warning7 = tk.Entry(lower_frame34, font=('Arial',11))
                     entry_warning7.place(relx=0.1, rely=0.1, relwidth=0.8, relheight=0.6)#locate it and size it.
                     warning7 = "You have entered wrong value . Please try again . - Enter an integer number-"
                     entry_warning7.insert(0, warning7)  





            elif k=='4':
               label41 = tk.Label(right_frame, text='Enter the amount of money in Omani Riyal..', font=("Arial",11))
               label41.place(relx=0.02, rely=0.05, relwidth=0.83, relheight=0.1)#locate it and size it.

               entryOMR = tk.Entry(right_frame, font=40)
               entryOMR.place(relx=0.02, rely=0.16 ,relwidth=0.5, relheight=0.1)  #locate it and size it.                            


               lower_frame41 = tk.Frame(root, bg='HotPink4')#name a variable for the frame and located in the root, and use Frame() function to do the frame
               lower_frame41.place(relx=0.09, rely=0.85, relwidth=0.85, relheight=0.13)#locate it and size it.
               
               next_button41 = tk.Button(right_frame, text='Next', bg='lightblue', command=lambda : money_entry(entryOMR.get()))
               next_button41.place(relx=0.65, rely=0.16 ,relwidth=0.3, relheight=0.1)#locate it and size it.

               def money_entry(entryOMR):
                  y = entryOMR
                  try:
                     if int(y):
                        lower_frame004 = tk.Frame(root, bg='HotPink4')#name a variable for the frame and located in the root, and use Frame() function to do the frame
                        lower_frame004.place(relx=0.09, rely=0.85, relwidth=0.85, relheight=0.13)#locate it and size it.
                     
                        label42 = tk.Label(right_frame, text="what you want to convert to", font=('Arial',13))
                        label42.place(relx=0.1, rely=0.27 ,relwidth=0.65, relheight=0.1)#locate it and size it.

                        label43 = tk.Label(right_frame, text="""choice from the list: 
   AED,United Arab Emirates\n BHD,Bahraini Dinar\n QAR,Qatari Riyal\n KWD,Kuwaiti Dinar\n USD,United States of America\n EUR,Euro\n SAR,Saudi Riyal\n""", font=('Arial',13))
                        label43.place(relx=0.1, rely=0.38 ,relwidth=0.8, relheight=0.4)#locate it and size it.

                        label44 = tk.Label(right_frame, text='Enter it here:-', font=("Arial",10))
                        label44.place(relx=0.05, rely=0.83, relwidth=0.3, relheight=0.1)#locate it and size it.

                        entry42 = tk.Entry(right_frame, font=40)
                        entry42.place(relx=0.39, rely=0.83, relwidth=0.25, relheight=0.1)#locate it and size it.

                        next_button42 = tk.Button(right_frame, text='Convert', bg='lightblue', command=lambda : convert_button(entry42.get()))
                        next_button42.place(relx=0.69, rely=0.89, relwidth=0.3, relheight=0.1)#locate it and size it.

                        def convert_button(entry42):
                           y = int(entryOMR)
                           x = entry42.upper()
                           lower_frame003lastelse = tk.Frame(root, bg='HotPink4')#name a variable for the frame and located in the root, and use Frame() function to do the frame
                           lower_frame003lastelse.place(relx=0.09, rely=0.85, relwidth=0.85, relheight=0.13)#locate it and size it.
                           entry43 = tk.Entry(lower_frame003lastelse, font=40)
                           entry43.place(relx=0.45, rely=0.15, relwidth=0.35, relheight=0.5)#locate it and size it.

                           SAR=y*9.74
                           KWD=y*0.79
                           AED=y*9.55
                           QAR=y*9.46
                           BHD=y*0.98
                           USD=y*2.60
                           EUR=y*2.20

                           if x=="AED":
                              entry43.insert(0, round(AED,2))                        
                           elif x=="BHD":
                              entry43.insert(0, round(BHD,2)) 
                           elif x=="QAR":
                              entry43.insert(0, round(QAR,2)) 
                           elif x=="KWD":
                              entry43.insert(0, round(KWD,2))
                           elif x=="USD":
                              entry43.insert(0, round(USD,2))
                           elif x=="EUR":
                              entry43.insert(0, round(EUR,2))
                           elif x=="SAR":
                              entry43.insert(0, round(SAR,2))
                           else:
                              lower_frame43 = tk.Frame(root, bg='HotPink4')#name a variable for the frame and located in the root, and use Frame() function to do the frame
                              lower_frame43.place(relx=0.09, rely=0.85, relwidth=0.85, relheight=0.13)#locate it and size it.

                              entry_warning8 = tk.Entry(lower_frame43, font=('Arial',11))
                              entry_warning8.place(relx=0.1, rely=0.1, relwidth=0.8, relheight=0.6)#locate it and size it.
                              warning8 = "You have entered wrong value . - Please Enter currency's short form name - "
                              entry_warning8.insert(0, warning8)

                  except:
                     lower_frame44 = tk.Frame(root, bg='HotPink4')#name a variable for the frame and located in the root, and use Frame() function to do the frame
                     lower_frame44.place(relx=0.09, rely=0.85, relwidth=0.85, relheight=0.13)#locate it and size it.

                     entry_warning9 = tk.Entry(lower_frame44, font=('Arial',11))
                     entry_warning9.place(relx=0.1, rely=0.1, relwidth=0.8, relheight=0.6)#locate it and size it.
                     warning9 = "You have entered wrong value . Please try again . - Enter an integer number-"
                     entry_warning9.insert(0, warning9)            





            elif k=='5':
               label51 = tk.Label(right_frame, text='Enter the amount of money in Qatari Riyal..', font=("Arial",11))
               label51.place(relx=0.02, rely=0.05, relwidth=0.85, relheight=0.1)#locate it and size it.

               entryQAR = tk.Entry(right_frame, font=40)
               entryQAR.place(relx=0.02, rely=0.16 ,relwidth=0.5, relheight=0.1) #locate it and size it.                             


               lower_frame51 = tk.Frame(root, bg='HotPink4')#name a variable for the frame and located in the root, and use Frame() function to do the frame
               lower_frame51.place(relx=0.09, rely=0.85, relwidth=0.85, relheight=0.13)#locate it and size it.
               
               next_button51 = tk.Button(right_frame, text='Next', bg='lightblue', command=lambda : money_entry(entryQAR.get()))
               next_button51.place(relx=0.65, rely=0.16 ,relwidth=0.3, relheight=0.1)#locate it and size it.

               def money_entry(entryQAR):
                  y = entryQAR
                  try:
                     if int(y):
                        lower_frame005 = tk.Frame(root, bg='HotPink4')#name a variable for the frame and located in the root, and use Frame() function to do the frame
                        lower_frame005.place(relx=0.09, rely=0.85, relwidth=0.85, relheight=0.13)#locate it and size it.
                     
                        label52 = tk.Label(right_frame, text="what you want to convert to", font=('Arial',13))#name a vatiable for the label. and located in the right frame. And set its properties.
                        label52.place(relx=0.1, rely=0.27 ,relwidth=0.65, relheight=0.1)#locate it and size it.

                        label53 = tk.Label(right_frame, text="""choice from the list: 
   AED,United Arab Emirates\n BHD,Bahraini Dinar\n SAR,Saudi Riyal\n KWD,Kuwaiti Dinar\n USD,United States of America\n EUR,Euro\n OMR,Omani Riyal\n""", font=('Arial',13))#name a vatiable for the label. and located in the right frame. And set its properties.
                        label53.place(relx=0.1, rely=0.38 ,relwidth=0.8, relheight=0.4)#locate it and size it.

                        label54 = tk.Label(right_frame, text='Enter it here:-', font=("Arial",10))
                        label54.place(relx=0.05, rely=0.83, relwidth=0.3, relheight=0.1)#locate it and size it.

                        entry52 = tk.Entry(right_frame, font=40)
                        entry52.place(relx=0.39, rely=0.83, relwidth=0.25, relheight=0.1)#locate it and size it.

                        next_button52 = tk.Button(right_frame, text='Convert', bg='lightblue', command=lambda : convert_button(entry52.get()))
                        next_button52.place(relx=0.69, rely=0.89, relwidth=0.3, relheight=0.1)#locate it and size it.

                        def convert_button(entry52):
                           y = int(entryQAR)
                           x = entry52.upper()
                           lower_frame004lastelse = tk.Frame(root, bg='HotPink4')#name a variable for the frame and located in the root, and use Frame() function to do the frame
                           lower_frame004lastelse.place(relx=0.09, rely=0.85, relwidth=0.85, relheight=0.13)#locate it and size it.
                           entry53 = tk.Entry(lower_frame004lastelse, font=40)
                           entry53.place(relx=0.45, rely=0.15, relwidth=0.35, relheight=0.5)#locate it and size it.

                           SAR=y*1.03
                           KWD=y*0.084
                           AED=y*1.01
                           OMR=y*0.11
                           BHD=y*0.10
                           USD=y*0.27
                           EUR=y*0.23

                           if x=="AED":
                              entry53.insert(0, round(AED,2))                        
                           elif x=="BHD":
                              entry53.insert(0, round(BHD,2)) 
                           elif x=="SAR":
                              entry53.insert(0, round(SAR,2)) 
                           elif x=="KWD":
                              entry53.insert(0, round(KWD,2))
                           elif x=="USD":
                              entry53.insert(0, round(USD,2))
                           elif x=="EUR":
                              entry53.insert(0, round(EUR,2))
                           elif x=="OMR":
                              entry53.insert(0, round(OMR,2))
                           else:
                              lower_frame53 = tk.Frame(root, bg='HotPink4')#name a variable for the frame and located in the root, and use Frame() function to do the frame
                              lower_frame53.place(relx=0.09, rely=0.85, relwidth=0.85, relheight=0.13)#locate it and size it.

                              entry_warning10 = tk.Entry(lower_frame53, font=('Arial',11))
                              entry_warning10.place(relx=0.1, rely=0.1, relwidth=0.8, relheight=0.6)#locate it and size it.
                              warning10 = "You have entered wrong value . - Please Enter currency's short form name - "
                              entry_warning10.insert(0, warning10)

                  except:
                     lower_frame54 = tk.Frame(root, bg='HotPink4')#name a variable for the frame and located in the root, and use Frame() function to do the frame
                     lower_frame54.place(relx=0.09, rely=0.85, relwidth=0.85, relheight=0.13)#locate it and size it.

                     entry_warning11 = tk.Entry(lower_frame54, font=('Arial',11))
                     entry_warning11.place(relx=0.1, rely=0.1, relwidth=0.8, relheight=0.6)#locate it and size it.
                     warning11 = "You have entered wrong value . Please try again . - Enter an integer number-"
                     entry_warning11.insert(0, warning11)      





            elif k=='6':
               label61 = tk.Label(right_frame, text='Enter the amount of money in Bahraini Dinar..', font=("Arial",11))
               label61.place(relx=0.02, rely=0.05, relwidth=0.85, relheight=0.1)#locate it and size it.

               entryBHD = tk.Entry(right_frame, font=40)
               entryBHD.place(relx=0.02, rely=0.16 ,relwidth=0.5, relheight=0.1)  #locate it and size it.                            


               lower_frame61 = tk.Frame(root, bg='HotPink4')#name a variable for the frame and located in the root, and use Frame() function to do the frame
               lower_frame61.place(relx=0.09, rely=0.85, relwidth=0.85, relheight=0.13)#locate it and size it.
               
               next_button61 = tk.Button(right_frame, text='Next', bg='lightblue', command=lambda : money_entry(entryBHD.get()))
               next_button61.place(relx=0.65, rely=0.16 ,relwidth=0.3, relheight=0.1)#locate it and size it.


               def money_entry(entryBHD):
                  y = entryBHD
                  try:
                     if int(y):
                        lower_frame006 = tk.Frame(root, bg='HotPink4')#name a variable for the frame and located in the root, and use Frame() function to do the frame
                        lower_frame006.place(relx=0.09, rely=0.85, relwidth=0.85, relheight=0.13)#locate it and size it.
                     
                        label62 = tk.Label(right_frame, text="what you want to convert to", font=('Arial',13))#name a vatiable for the label. and located in the right frame. And set its properties.
                        label62.place(relx=0.1, rely=0.27 ,relwidth=0.65, relheight=0.1)#locate it and size it.

                        label63 = tk.Label(right_frame, text="""choice from the list: 
   AED,United Arab Emirates\n SAR,Saudi Riyal\n QAR,Qatari Riyal\n KWD,Kuwaiti Dinar\n USD,United States of America\n EUR,Euro\n OMR,Omani Riyal\n""", font=('Arial',13))#name a vatiable for the label. and located in the right frame. And set its properties.
                        label63.place(relx=0.1, rely=0.38 ,relwidth=0.8, relheight=0.4)#locate it and size it.

                        label64 = tk.Label(right_frame, text='Enter it here:-', font=("Arial",10))#name a vatiable for the label. and located in the right frame. And set its properties.
                        label64.place(relx=0.05, rely=0.83, relwidth=0.3, relheight=0.1)#locate it and size it.

                        entry62 = tk.Entry(right_frame, font=40)
                        entry62.place(relx=0.39, rely=0.83, relwidth=0.25, relheight=0.1)#locate it and size it.

                        next_button62 = tk.Button(right_frame, text='Convert', bg='lightblue', command=lambda : convert_button(entry62.get()))
                        next_button62.place(relx=0.69, rely=0.89, relwidth=0.3, relheight=0.1)#locate it and size it.


                        def convert_button(entry62):
                           y = int(entryBHD)
                           x = entry62.upper()
                           lower_frame005lastelse = tk.Frame(root, bg='HotPink4')#name a variable for the frame and located in the root, and use Frame() function to do the frame
                           lower_frame005lastelse.place(relx=0.09, rely=0.85, relwidth=0.85, relheight=0.13)#locate it and size it.
                           entry63 = tk.Entry(lower_frame005lastelse, font=40)
                           entry63.place(relx=0.45, rely=0.15, relwidth=0.35, relheight=0.5)#locate it and size it.

                           SAR=y*9.95
                           KWD=y*0.81
                           AED=y*9.74
                           OMR=y*1.02
                           QAR=y*9.65
                           USD=y*2.56
                           EUR=y*2.24

                           if x=="AED":
                              entry63.insert(0, round(AED,2))                        
                           elif x=="SAR":
                              entry63.insert(0, round(SAR,2)) 
                           elif x=="QAR":
                              entry63.insert(0, round(QAR,2)) 
                           elif x=="KWD":
                              entry63.insert(0, round(KWD,2))
                           elif x=="USD":
                              entry63.insert(0, round(USD,2))
                           elif x=="EUR":
                              entry63.insert(0, round(EUR,2))
                           elif x=="OMR":
                              entry63.insert(0, round(OMR,2))
                           else:
                              lower_frame63 = tk.Frame(root, bg='HotPink4')#name a variable for the frame and located in the root, and use Frame() function to do the frame
                              lower_frame63.place(relx=0.09, rely=0.85, relwidth=0.85, relheight=0.13)#locate it and size it.

                              entry_warning12 = tk.Entry(lower_frame63, font=('Arial',11))
                              entry_warning12.place(relx=0.1, rely=0.1, relwidth=0.8, relheight=0.6)#locate it and size it.
                              warning12 = "You have entered wrong value . - Please Enter currency's short form name - "
                              entry_warning12.insert(0, warning12)


                  except:
                     lower_frame64 = tk.Frame(root, bg='HotPink4')#name a variable for the frame and located in the root, and use Frame() function to do the frame
                     lower_frame64.place(relx=0.09, rely=0.85, relwidth=0.85, relheight=0.13)#locate it and size it.

                     entry_warning13 = tk.Entry(lower_frame64, font=('Arial',11))
                     entry_warning13.place(relx=0.1, rely=0.1, relwidth=0.8, relheight=0.6)#locate it and size it.
                     warning13 = "You have entered wrong value . Please try again . - Enter an integer number-"
                     entry_warning13.insert(0, warning13) 





            elif k=='7':
               label71 = tk.Label(right_frame, text='Enter the amount of money in American Dollar..', font=("Arial",11))#name a vatiable for the label. and located in the right frame. And set its properties.
               label71.place(relx=0.02, rely=0.05, relwidth=0.87, relheight=0.1)#locate it and size it.

               entryUSD = tk.Entry(right_frame, font=40)
               entryUSD.place(relx=0.02, rely=0.16 ,relwidth=0.5, relheight=0.1) #locate it and size it.                             


               lower_frame71 = tk.Frame(root, bg='HotPink4')#name a variable for the frame and located in the root, and use Frame() function to do the frame
               lower_frame71.place(relx=0.09, rely=0.85, relwidth=0.85, relheight=0.13)#locate it and size it.
               
               next_button71 = tk.Button(right_frame, text='Next', bg='lightblue', command=lambda : money_entry(entryUSD.get()))
               next_button71.place(relx=0.65, rely=0.16 ,relwidth=0.3, relheight=0.1)#locate it and size it.


               def money_entry(entryUSD):
                  y = entryUSD
                  try:
                     if int(y):
                        lower_frame007 = tk.Frame(root, bg='HotPink4')#name a variable for the frame and located in the root, and use Frame() function to do the frame
                        lower_frame007.place(relx=0.09, rely=0.85, relwidth=0.85, relheight=0.13)#locate it and size it.
                     
                        label72 = tk.Label(right_frame, text="what you want to convert to", font=('Arial',13))#name a vatiable for the label. and located in the right frame. And set its properties.
                        label72.place(relx=0.1, rely=0.27 ,relwidth=0.65, relheight=0.1)#locate it and size it.

                        label73 = tk.Label(right_frame, text="""choice from the list: 
   AED,United Arab Emirates\n BHD,Bahraini Dinar\n QAR,Qatari Riyal\n KWD,Kuwaiti Dinar\n SAR,Saudi Riyal\n EUR,Euro\n OMR,Omani Riyal\n""", font=('Arial',13))#name a vatiable for the label. and located in the right frame. And set its properties.
                        label73.place(relx=0.1, rely=0.38 ,relwidth=0.8, relheight=0.4)#locate it and size it.

                        label74 = tk.Label(right_frame, text='Enter it here:-', font=("Arial",10))
                        label74.place(relx=0.05, rely=0.83, relwidth=0.3, relheight=0.1)#locate it and size it.

                        entry72 = tk.Entry(right_frame, font=40)
                        entry72.place(relx=0.39, rely=0.83, relwidth=0.25, relheight=0.1)#locate it and size it.

                        next_button72 = tk.Button(right_frame, text='Convert', bg='lightblue', command=lambda : convert_button(entry72.get()))
                        next_button72.place(relx=0.69, rely=0.89, relwidth=0.3, relheight=0.1)#locate it and size it.


                        def convert_button(entry72):
                           y = int(entryUSD)
                           x = entry72.upper()
                           lower_frame006lastelse = tk.Frame(root, bg='HotPink4')#name a variable for the frame and located in the root, and use Frame() function to do the frame
                           lower_frame006lastelse.place(relx=0.09, rely=0.85, relwidth=0.85, relheight=0.13)#locate it and size it.
                           entry73 = tk.Entry(lower_frame006lastelse, font=40)
                           entry73.place(relx=0.45, rely=0.15, relwidth=0.35, relheight=0.5)#locate it and size it.

                           SAR=y*3.75
                           KWD=y*0.31
                           AED=y*3.67
                           OMR=y*0.39
                           QAR=y*3.64
                           BHD=y*0.38
                           EUR=y*0.85

                           if x=="AED":
                              entry73.insert(0, round(AED,2))                        
                           elif x=="BHD":
                              entry73.insert(0, round(BHD,2)) 
                           elif x=="QAR":
                              entry73.insert(0, round(QAR,2)) 
                           elif x=="KWD":
                              entry73.insert(0, round(KWD,2))
                           elif x=="SAR":
                              entry73.insert(0, round(SAR,2))
                           elif x=="EUR":
                              entry73.insert(0, round(EUR,2))
                           elif x=="OMR":
                              entry73.insert(0, round(OMR,2))
                           else:
                              lower_frame73 = tk.Frame(root, bg='HotPink4')#name a variable for the frame and located in the root, and use Frame() function to do the frame
                              lower_frame73.place(relx=0.09, rely=0.85, relwidth=0.85, relheight=0.13)#locate it and size it.

                              entry_warning14 = tk.Entry(lower_frame73, font=('Arial',11))
                              entry_warning14.place(relx=0.1, rely=0.1, relwidth=0.8, relheight=0.6)#locate it and size it.
                              warning14 = "You have entered wrong value . - Please Enter currency's short form name - "
                              entry_warning14.insert(0, warning14)


                  except:
                     lower_frame74 = tk.Frame(root, bg='HotPink4')#name a variable for the frame and located in the root, and use Frame() function to do the frame
                     lower_frame74.place(relx=0.09, rely=0.85, relwidth=0.85, relheight=0.13)#locate it and size it.

                     entry_warning15 = tk.Entry(lower_frame74, font=('Arial',11))
                     entry_warning15.place(relx=0.1, rely=0.1, relwidth=0.8, relheight=0.6)#locate it and size it.
                     warning15 = "You have entered wrong value . Please try again . - Enter an integer number-"
                     entry_warning15.insert(0, warning15)   





            elif k=='8':
               label81 = tk.Label(right_frame, text='Enter the amount of money in Euro..', font=("Arial",11))#name a vatiable for the label. and located in the right frame. And set its properties.
               label81.place(relx=0.02, rely=0.05, relwidth=0.85, relheight=0.1)#locate it and size it.


               entryEUR = tk.Entry(right_frame, font=40)
               entryEUR.place(relx=0.02, rely=0.16 ,relwidth=0.5, relheight=0.1)   #locate it and size it.                           


               lower_frame81 = tk.Frame(root, bg='HotPink4')#name a variable for the frame and located in the root, and use Frame() function to do the frame
               lower_frame81.place(relx=0.09, rely=0.85, relwidth=0.85, relheight=0.13)#locate it and size it.
               

               next_button81 = tk.Button(right_frame, text='Next', bg='lightblue', command=lambda : money_entry(entryEUR.get()))
               next_button81.place(relx=0.65, rely=0.16 ,relwidth=0.3, relheight=0.1)#locate it and size it.

               def money_entry(entryEUR):
                  y = entryEUR
                  try:
                     if int(y):
                        lower_frame008 = tk.Frame(root, bg='HotPink4')#name a variable for the frame and located in the root, and use Frame() function to do the frame
                        lower_frame008.place(relx=0.09, rely=0.85, relwidth=0.85, relheight=0.13)#locate it and size it.
                     
                        label82 = tk.Label(right_frame, text="what you want to convert to", font=('Arial',13))#name a vatiable for the label. and located in the right frame. And set its properties.
                        label82.place(relx=0.1, rely=0.27 ,relwidth=0.65, relheight=0.1)#locate it and size it.

                        label83 = tk.Label(right_frame, text="""choice from the list: 
   AED,United Arab Emirates\n BHD,Bahraini Dinar\n QAR,Qatari Riyal\n KWD,Kuwaiti Dinar\n USD,United States of America\n SAR,Saudi Riyal\n OMR,Omani Riyal\n""", font=('Arial',13))#name a vatiable for the label. and located in the right frame. And set its properties.
                        label83.place(relx=0.1, rely=0.38 ,relwidth=0.8, relheight=0.4)#locate it and size it.

                        label84 = tk.Label(right_frame, text='Enter it here:-', font=("Arial",10))
                        label84.place(relx=0.05, rely=0.83, relwidth=0.3, relheight=0.1)#locate it and size it.

                        entry82 = tk.Entry(right_frame, font=40)
                        entry82.place(relx=0.39, rely=0.83, relwidth=0.25, relheight=0.1)#locate it and size it.

                        next_button82 = tk.Button(right_frame, text='Convert', bg='lightblue', command=lambda : convert_button(entry82.get()))
                        next_button82.place(relx=0.69, rely=0.89, relwidth=0.3, relheight=0.1)#locate it and size it.


                        def convert_button(entry82):
                           y = int(entryEUR)
                           x = entry82.upper()
                           lower_frame007lastelse = tk.Frame(root, bg='HotPink4')#name a variable for the frame and located in the root, and use Frame() function to do the frame
                           lower_frame007lastelse.place(relx=0.09, rely=0.85, relwidth=0.85, relheight=0.13)#locate it and size it.
                           entry83 = tk.Entry(lower_frame007lastelse, font=40)
                           entry83.place(relx=0.45, rely=0.15, relwidth=0.35, relheight=0.5)#locate it and size it.


                           SAR=y*4.44
                           KWD=y*0.36
                           AED=y*4.43
                           OMR=y*0.46
                           QAR=y*4.31
                           BHD=y*0.45
                           USD=y*1.18


                           if x=="AED":
                              entry83.insert(0, round(AED,2))                        
                           elif x=="BHD":
                              entry83.insert(0, round(BHD,2)) 
                           elif x=="QAR":
                              entry83.insert(0, round(QAR,2)) 
                           elif x=="KWD":
                              entry83.insert(0, round(KWD,2))
                           elif x=="USD":
                              entry83.insert(0, round(USD,2))
                           elif x=="SAR":
                              entry83.insert(0, round(SAR,2))
                           elif x=="OMR":
                              entry83.insert(0, round(OMR,2))
                           else:
                              lower_frame83 = tk.Frame(root, bg='HotPink4')#name a variable for the frame and located in the root, and use Frame() function to do the frame
                              lower_frame83.place(relx=0.09, rely=0.85, relwidth=0.85, relheight=0.13)#locate it and size it.
                              entry_warning16 = tk.Entry(lower_frame83, font=('Arial',11))
                              entry_warning16.place(relx=0.1, rely=0.1, relwidth=0.8, relheight=0.6)#locate it and size it.
                              warning16 = "You have entered wrong value . - Please Enter currency's short form name - "
                              entry_warning16.insert(0, warning16)


                  except:
                     lower_frame84 = tk.Frame(root, bg='HotPink4')#name a variable for the frame and located in the root, and use Frame() function to do the frame
                     lower_frame84.place(relx=0.09, rely=0.85, relwidth=0.85, relheight=0.13)#locate it and size it.

                     entry_warning17 = tk.Entry(lower_frame84, font=('Arial',11))
                     entry_warning17.place(relx=0.1, rely=0.1, relwidth=0.8, relheight=0.6)#locate it and size it.
                     warning17 = "You have entered wrong value . Please try again . - Enter an integer number-"
                     entry_warning17.insert(0, warning17)             


            else:
               entry_warning1 = tk.Entry(lower_frame, font=20)
               entry_warning1.place(relx=0.03, rely=0.1, relwidth=0.92, relheight=0.6)#locate it and size it.
               warning1 = "You have entered wrong value.-Please Enter number from the list-"
               entry_warning1.insert(0, warning1)
            
