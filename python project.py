# -*- coding: utf-8 -*-
"""
Created on Sun Dec 10 08:14:55 2023

@author: Lenovo
"""

import pandas as pd
import matplotlib.pyplot as plt

def menu():
    print()
    print("************************************************************************")
    print("              Welcome to Railways Managment System                      ")
    print("************************************************************************")
    print()
    print("          0.  About the Project                                    ")
    print("          1.  Show Train Deatils                                   ")
    print("          2.  Running Days of Train                                ")
    print("          3.  Sort on the basis of Destination                     ")                               
    print("          4.  Update Current Running Status of Train               ")
    print("          5.  Cancel Trains                                        ")
    print("          6.  Show Confirmed Resevation, Waiting list              ")
    print("          7.  Update Reservation Status                            ")
    print("          8.  Show the Fares of ticket                             ")
    print("          9.  Highest  Fare of ticket                              ")
    print("          10. Lowest   Fair of ticket                              ")
    print("          11. Average number of person boarding on train           ")
    print("          12. Line Plot between   Avg person Boarding vs Train     ")
    print("          13. Bar PLot between    Avg person Boarding vs Train     ")
    print("          14. Horizontal Bar PLot Avg person Boarding vs Train     ")
    print("          15. Exit                                                 ")
    print()
    print("************************************************************************")
    
menu()
def about():
    print("->The Project is based on Railways Management System.")
    print('''->This Software facilitates to enquire about the trains available on the basis of source and 
          destination,running status , Cancellation of trains, enquire about the status of the booked ticket, etc.''')
    print('''->The aim of case study is to design and develop a software maintaining the records of different trains, 
          train status, reservation status, fares of ticket etc,..''')
    print("->It contains 5 CSV Files :- train_info, running status, confirm_reserv, fare, avgperson")
    print("\n")

def train_detail():
    print("--------------------Showing Details of Trains-----------------------------")
    print()
    df=pd.read_csv("C:\\Users\\Lenovo\\OneDrive\\Documents\\hcbb ip project software\\train_info.csv",index_col=0)
    pd.set_option('display.max_columns', 5)
    print(df)
    print()
 
def rndays():
    print("-------------Running Days of Trains--------------")
    print()
    df=pd.read_csv("C:\\Users\\Lenovo\\OneDrive\\Documents\\hcbb ip project software\\train_info.csv",index_col=0)
    pd.set_option('display.max_columns', 5)
    print(df[['Train name','Running days']])
    print()
    
def sort():
    print("-------------Sorting Trains with respect to Destination--------------")
    print()
    df=pd.read_csv("C:\\Users\\Lenovo\\OneDrive\\Documents\\hcbb ip project software\\train_info.csv",index_col=0)
    pd.set_option('display.max_columns', 5)
    print(df.sort_values(['Destination']))
    print()
    
def rnstat():
    print("------------Updating Status of Trains------------")
    print()
    df=pd.read_csv("C:\\Users\\Lenovo\\OneDrive\\Documents\\hcbb ip project software\\current running status.csv",index_col=0)
    print(df)
    print()
    tno=int(input("Enter Train number       :"))
    cloc=(input("Enter Current location     :"))
    dely=(input("Delayed By                 :"))
    df.currenr_location[tno]= cloc
    df.delay[tno]= dely
    print()
    print(df)  
    print()
    print("Running Stauts of Train no:", tno, "has be updated")
    print()
    
def cancel():
    print("------------Cancel Trains------------")
    print()
    df=pd.read_csv("C:\\Users\\Lenovo\\OneDrive\\Documents\\hcbb ip project software\\train_info.csv",index_col=0)
    print(df)
    print()
    tno=int(input("Enter Train number to be cancelled    :"))
    df=df.drop(tno)
    print()
    print(df)
    print()
    print("Train no:", tno, "has been cancelled")
    print()
    
def reservstat():
    print("------------Showing Reservation Status-----------")
    df=pd.read_csv("C:\\Users\\Lenovo\\OneDrive\\Documents\\hcbb ip project software\\confirm_reserv.csv",index_col=0)
    print(df)
    print()


def pnrstat():
    print("------------Updating Reservation Status------------")
    print()
    df=pd.read_csv("C:\\Users\\Lenovo\\OneDrive\\Documents\\hcbb ip project software\\confirm_reserv.csv",index_col=0)
    print(df)
    print()
    pnr=int(input("Enter PNR        :"))
    stat=(input("Reservation status :"))
    df.Status[pnr]= stat
    print()
    print(df)    
    print()
    print("Reservation Stauts of PNR :", pnr, "has be updated to", stat)
    print()
    
def fare():
    print("------------Showing Fares of Ticket------------")
    print()
    df=pd.read_csv("C:\\Users\\Lenovo\\OneDrive\\Documents\\hcbb ip project software\\fares.csv")
    pd.set_option('display.max_columns',7)
    print(df)
    print()
    
def maxfare():
    df=pd.read_csv("C:\\Users\\Lenovo\\OneDrive\\Documents\\hcbb ip project software\\fares.csv")
    print("-----------------Fares of Ticket---------------")
    print(df)
    print("---------------Higest Fare of Ticket-----------")
    print()
    print(df.OneAC.max())
    print()
       
    
def minfare():
    df=pd.read_csv("C:\\Users\\Lenovo\\OneDrive\\Documents\\hcbb ip project software\\fares.csv")
    print("-----------------Fares of Ticket---------------")
    print(df)
    print()
    print("-------------lowest Fare of Ticket-------------")
    print()
    print(df.Sleeper.min()) 
    print()

def avgper():
    print("------------Showing Average Person Boarding on Different Trains-----------")
    df=pd.read_csv("C:\\Users\\Lenovo\\OneDrive\\Documents\\hcbb ip project software\\avgperson.csv")
    print(df)
    print()


def line_plot():
    print("------Line Plot between Average person Boarding In Different Trains------")
    df=pd.read_csv("C:\\Users\\Lenovo\\OneDrive\\Documents\\hcbb ip project software\\avgperson.csv")
    print(df) 
    x=df['tname']
    y=df['avg']
    plt.title('Avg Person Boarding in train')    
    plt.xlabel('Train Name')    
    plt.ylabel('Avg Person Boarding')    
    plt.plot(x,y, marker='d',markeredgecolor='k',linewidth=4,color="r") 
    plt.show()
    print()
    

    
def bar_plot():
    print("------Bar Plot between Average person Boarding In Different Trains------")
    print()
    
    df=pd.read_csv("C:\\Users\\Lenovo\\OneDrive\\Documents\\hcbb ip project software\\avgperson.csv")
    print(df)
    x=df['tname']
    y=df['avg']
    plt.title('Avg Person Boarding in train', fontsize=14)    
    plt.xlabel('Train Name', fontsize=14)    
    plt.ylabel('Avg Person Boarding' , fontsize=14)    
    plt.bar(x,y,color=["r",'b', 'k', 'silver', 'gold'], width=0.5) 
    plt.show()
    
    
def barh_plot():
    print("------Horizontal Bar Plot between Average person Boarding In Different Trains------")
    print()
    df=pd.read_csv("C:\\Users\\Lenovo\\OneDrive\\Documents\\hcbb ip project software\\avgperson.csv")
    print(df)
    x=df['tname']
    y=df['avg']
    plt.title('Avg Person Boarding in train', fontsize=14)    
    plt.ylabel('Train Name', fontsize=14)    
    plt.xlabel('Avg Person Boarding' , fontsize=14) 
    plt.barh(x,y,color='silver',edgecolor="r") 
    plt.show()
    print() 
    

while True:
 opt=int(input("Enter your choice:"))
 print("************************************************************************")
 print()
 if opt==0:
    about()
    menu()
 elif opt==1:
    train_detail() 
    menu()
 elif opt==2:
    rndays() 
    menu()
 elif opt==3:
    sort()
    menu()
 elif opt==4:
   rnstat() 
   menu()
 elif opt==5:
   cancel()
   menu()
 elif opt==6:
    reservstat() 
    menu()
 elif opt==7:
    pnrstat()
    menu()
 elif opt==8:
   fare() 
   menu()
 elif opt==9:
    maxfare() 
    menu()
 elif opt==10:
    minfare() 
    menu()
 elif opt==11:
    avgper() 
    menu()
 elif opt==12:
    line_plot() 
    menu()
 elif opt==13:
    bar_plot()
    menu()
 elif opt==14:
    barh_plot()
    menu()
 elif opt==15:
   print('Software is Terminated')
   break
 else:
    print('Invalid option!!!.Please enter options which are given in the Main Menu')