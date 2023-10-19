import csv
import datetime
import os


name=[]
address=[]
phoneno=[]
room=[]
price=[]
checkin=[]
checkout=[]

def customer_id():
    file=open(r"Hotel Bliss.csv","r",newline='')
    datareader=csv.reader(file)
    if (os.stat("Hotel Bliss.csv").st_size == 0):
        return 10000001
    else:
        for data in datareader:
            custid=data[0]
            c_id=int(custid)+1
        return c_id
    file.close()


maxPricePerNight=0
noOfGuests=0
flag=0


allRooms = [
        [101, "Single Bed Standard Non-AC Room     ", 1000, 1, True],
        [102, "Single Bed Standard Non-AC Room     ", 1000, 1, True],
        [103, "Single Bed Standard Non-AC Room     ", 1000, 1, True],
        [104, "Single Bed Standard AC Room         ", 1300, 1, True],
        [105, "Single Bed Standard AC Room         ", 1300, 1, True],
        [106, "Single Bed Standard AC Room         ", 1300, 1, True],
        [201, "Double Bed Standard Non-AC Room     ", 1600, 2, True],
        [202, "Double Bed Standard Non-AC Room     ", 1600, 2, True],
        [203, "Double Bed Standard Non-AC Room     ", 1600, 2, True],
        [204, "Double Bed Standard AC Room         ", 2000, 2, True],
        [205, "Double Bed Standard AC Room         ", 2000, 2, True],
        [206, "Double Bed Standard AC Room         ", 2000, 2, True],
        [301, "Double Bed First Class AC Room      ", 3700, 2, True],
        [302, "Double Bed First Class AC Room      ", 3700, 2, True],
        [303, "Double Bed First Class AC Room      ", 3700, 2, True],
        [304, "Two Double Beds Standard Non-AC Room", 4200, 4, True],
        [305, "Two Double Beds Standard Non-AC Room", 4200, 4, True],
        [306, "Triple Beds Standard Non-AC Room    ", 4500, 3, True],
        [401, "Triple Beds Standard AC Room        ", 4800, 3, True],
        [402, "Two Double Beds Standard AC Room    ", 5000, 4, True],
        [403, "Two Double Beds Standard AC Room    ", 5000, 4, True],
        [501, "Special Diamond Room                ", 5400, 2, True],
        [502, "Special Diamond Room                ", 5400, 2, True],
        [503, "Special Diamond Room                ", 5400, 4, True],
        [601, "Special Platinum Room               ", 6000, 2, True],
        [602, "Special Platinum Room               ", 6000, 4, True],
        [701, "The Elite Family Bliss Room         ", 9500, 6, True],
        [702, "The Elite Family Bliss Room         ", 9500, 6, True],
        [801, "The Elite Bliss Suite               ", 12500, 4, True]
    ]
RMfile=open("All Rooms.csv","a",newline='')
recwriter=csv.writer(RMfile)
if (os.stat("All Rooms.csv").st_size == 0):
    for i in range(0,29,1):
        rec=allRooms[i]
        recwriter.writerow(rec)
RMfile.close()

def home():
    print()
    print("\t\t\t\t\t Welcome to THE BLISS\n")
    print("\t\t\t 1 Information About All Rooms\n")
    print("\t\t\t 2 Book a Room\n")
    print("\t\t\t 3 Payments & Reciepts\n")
    print("\t\t\t 4 Detailed Booking Records\n")
    print("\t\t\t 0 Exit\n")
    
    print("What can I help you with?")
    userChoice=int(input("-->"))
    
    if(userChoice == 1):
        print("Information about All Rooms selected.")
        showAllRooms()
    
    elif(userChoice == 2):
        print("Book a Room selected.")
        bookRoom()
    
    elif(userChoice == 3):
        print("Payments & Receipts selected.")
        payment()
    
    elif(userChoice==4):
        print(" ")
        allRecords()
    
    elif(userChoice==0):
        exit()
    
    else:
        print("This option is not valid. Please select another.")
        home()


def exit():
    print("\t\t\t Thank You. Visit Again. Om Shanti.")
        
        
        
def showAllRooms():
    
    print("\t\t ALL ROOMS ")
    print("Room No.\tRoom Type and Description\t\tPrice per Night\t\tMax Guests\tAvailable\n")
    Rfile=open("All Rooms.csv","r",newline='')
    recreader=csv.reader(Rfile)
    for rec in recreader:
        print(rec[0],"\t\t",rec[1],"\t\t",rec[2],"\t\t",rec[3],"\t\t",rec[4])
    Rfile.close()
   
    
    inp=input("Press any key to go back to Home Page -> ")
    if(inp != ""):
        home()

def addFilters():
    global noOfGuests
    global maxPricePerNight
    noOfGuests=int(input("Enter the number of people you want to book rooms for: "))
    maxPricePerNight=int(input("Enter the maximum price per night budget: "))

    
        
def showAvailableRooms():
    global flag
    print("\t\t AVAILABLE ROOMS")
    print("Room No.\tRoom Type and Description\t\tPrice per Night\t\tMax Guests\tAvailable\n")
    Rfile=open("All Rooms.csv","r",newline='')
    recreader=csv.reader(Rfile)
    for rec in recreader:
        if (int(rec[3])>= noOfGuests and noOfGuests != 0):
            if (int(rec[2])<=maxPricePerNight):
                if(rec[4]=="True"):  
                    print(rec[0],"\t\t",rec[1],"\t\t",rec[2],"\t\t",rec[3],"\t\t",rec[4], "\t\t", end = " ")  
                print()
                flag=1
    Rfile.close()
    
    if(flag==0):
        print("No Rooms available with these filters")
                                        
    
    choice=input("Do you want to change your filters? Press ['y'] for \"Yes\"  and ['n'] for \"No\"  : ")
    if(choice=="y"):
        bookRoom()
    else:
        pass
        
                    
def getGuestDetails():
    nm=str(input("Under whose name the booking will be made? Enter the name of guest: "))
    phno=str(input("Enter phone number of the guest : "))
    adres=str(input("Enter your native city : "))        
    if(nm != "" and phno != "" and adres != ""):
            name.append(nm)
            address.append(adres)
            phoneno.append(phno)
    else:
        print("\tName, Phone no. or Address cannot be empty..!!")
    for i in range(1,noOfGuests,1):
        nm=str(input("Enter the name of other guests: "))
        if(nm != ""):
            name.append(nm)
            
        
    
def bookRoom():

    addFilters()
    showAvailableRooms()
    getGuestDetails()
    
    file=open(r"Hotel Bliss.csv","a",newline='')
    datawriter=csv.writer(file)
    
    an="y"
    Rfile=open("All Rooms.csv","r",newline='')
    recreader=csv.reader(Rfile)
    while(an=="y"):
        roomChoice=int(input("Enter Room Number of the room which you want to book : "))
        for rec in recreader:
            if(int(rec[0]) == roomChoice):
                if(rec[4]== "True"):
                    print("Room Type - ",rec[1])
                    room.append(rec[1].strip())
                    print("Price - ",int(rec[2]))
                    price.append(int(rec[2]))
                    global flag
                    flag=1
                else:
                    print("Room Not Available !")
                    an="y"
        
        if(flag==0):
            print("Invaid Room Number")
            an="y"
        else:
            an="n"
    Rfile.close()
   
    cor=1
    while(cor==1):
        entry=input("Enter the date of check-in (dd/mm/yyyy) : ")
        checkin.append(entry)
        entry=entry.split('/')
        ent=entry
        ent[0]=int(ent[0])
        ent[1]=int(ent[1])
        ent[2]=int(ent[2])
    
        exit=input("Enter the date of check-out (dd/mm/yyyy) : ")
        checkout.append(exit)
        exit=exit.split('/')
        exi=exit
        exi[0]=int(exi[0])
        exi[1]=int(exi[1])
        exi[2]=int(exi[2])
        
        if(exi[1]<ent[1] or exi[2]<ent[2]):
            print("....Date of Check-out must fall after Check-in....")
            checkin.pop()
            checkout.pop()
        elif(exi[1] == ent[1] and exi[2] >= ent[2] and exi[0] <= ent[0]):
            print("....Date of Check-out must fall after Check-in....")
            checkin.pop()
            checkout.pop()
        else:
            cor=0 
    
    din = datetime.datetime(ent[2],ent[1],ent[0])
    dout = datetime.datetime(exi[2],exi[1],exi[0])
    dstay = (dout - din).days
    
    
    customid=customer_id()

    
    
    paystat = "Unpaid"
    amount=price[0]*dstay
    
    Rfile=open("All Rooms.csv","r",newline='')
    recreader=csv.reader(Rfile)
    Rtempfile=open("Temp Rooms.csv","a",newline='')
    recwriter=csv.writer(Rtempfile)
    for rec in recreader:
        if(int(rec[0]) == roomChoice):
            rec[4]="False"
            recwriter.writerow(rec)
        else:
            recwriter.writerow(rec)
    Rfile.close()
    Rtempfile.close()
    os.remove(r"All Rooms.csv")
    os.rename(r"Temp Rooms.csv",r"All Rooms.csv")
    
    
    data=[customid,name,phoneno[0],address[0],room[0],roomChoice,checkin[0],checkout[0],dstay,price[0],amount,paystat]
    datawriter.writerow(data)
    file.close()
    
    
    name.clear()
    phoneno.clear()
    address.clear()
    room.clear()
    checkin.clear()
    checkout.clear()
    price.clear()

    
    c=1
    while (c==1):
        pask=input("Press ['Y'/'y'] to pay now or press ['0'] to go back to home page and pay later : ")
        if(pask=="y" or pask == "Y"):
            c=0
            print("")
            print("\t\t\t***ROOM BOOKED SUCCESSFULLY***\n")
            print("Customer Id - ",customid)
            print("Room no. - ",roomChoice)
            payment()
        elif(pask=="0"):
            c=0
            print("")
            print("\t\t\t***ROOM BOOKED SUCCESSFULLY***\n")
            print("Customer Id - ",customid)
            print("Room no. - ",roomChoice)
            home()   
        else:
            print("This option is not valid. Please select another. ")
            c=1
        
            
            
def payment():
    file=open(r"Hotel Bliss.csv","r",newline='')
    filetem=open(r"temp.csv","w",newline='')
    datareader=csv.reader(file)
    datawriter=csv.writer(filetem)
    cid=int(input("Enter your customer id : "))
    for data in datareader:
        if(cid == int(data[0])):
            if(data[11]=="Unpaid"):
                print(" Payment")
                print(" --------------------------------")
                print("  MODE OF PAYMENT")
                print("  1- Credit/Debit Card")
                print("  2- Using UPI")
                print("  3- Cash")
                x=int(input("Enter your choice -> "))
                print("\n  Amount: ",(data[10]))
                print("\n            Pay For Bliss")
                print("  (y/n)")
                ch=str(input("->"))
                if(ch=='y' or ch=='Y'):
                    print("\n\n --------------------------------")
                    print("           Hotel Bliss")
                    print(" --------------------------------")
                    print("              Bill")
                    print(" --------------------------------")
                    print(" Name: ",data[1],"\t\n Phone No.: ",data[2],"\t\n Address: ",data[3],"\t")
                    print("\n Check-In: ",data[6],"\t\n Check-Out: ",data[7],"\t")
                    print("\n Room Type: ",data[4],"\t\n Room Charges: ",data[9],"\t")
                    print(" --------------------------------")
                    print("\n Total Amount: ",data[10],"\t")
                    print(" --------------------------------")
                    print("          Thank You")
                    print("          Visit Again :)")
                    print(" --------------------------------\n")
                    data[11]="Paid"
                    datawriter.writerow(data)
                else:
                    print("Payment Incomplete")
                    datawriter.writerow(data)
            else:
                print("...Payment Already Done...")
            
        else:
            datawriter.writerow(data)
    file.close()
    filetem.close()
    os.remove(r"Hotel Bliss.csv")
    os.rename(r"temp.csv",r"Hotel Bliss.csv")
    c=int(input("Press 0 to go back to home page: "))
    if(c==0):
        home()
    else:
        exit()
            
        
def allRecords():
    global flag
    flag=0
    print()
    print(" 1 -> All Records ")
    print(" 2 -> Records sorted by Customer Id ")
    print(" 3 -> Records sorted by Customer Name ")
    print(" 4 -> Records sorted by Check-in date ")
    print(" 5 -> Records sorted by Check-out date ")
    print(" 6 -> Records sorted by Payment Status ")
    print(" 7 -> Records sorted by Room number ")
    print(" 0 -> Back to Home page ")
    uc=int(input("Pick your choice : "))
    if(uc == 1):
        file=open(r"Hotel Bliss.csv","r",newline='')
        datareader=csv.reader(file)
        print("        *** HOTEL RECORD ***\n")
        print("| Customer ID | Name                   | Phone No.  | Address   |Room No. | Check-In  | Check-Out | Nights Stayed | Price Per Night | Amount | Bill Status |")
        print("----------------------------------------------------------------------------------------------------------------------------------------------------------------")
        for data in datareader:
            print("|",data[0]," |",data[1],"|",data[2],"|",data[3],"|",data[5],"|",data[6],"|",data[7],"|",data[8],"|",data[9],"| ",data[10]," | ",data[11],"|")
        file.close()
        
        back=int(input("Press ['0'] to go back : "))
        if(back == 0):
            allRecords()
        else:
            exit()
            
    
    elif(uc == 2):
        file=open(r"Hotel Bliss.csv","r",newline='')
        datareader=csv.reader(file)
        idsearch=int(input("Enter customer id to search : "))
        for data in datareader:
            if(idsearch == int(data[0])):
                print("        *** HOTEL RECORD ***\n")
                print("| Customer ID | Name                 | Phone No.  | Address   |Room No. | Check-In  | Check-Out | Nights Stayed | Price Per Night | Amount | Bill Status |")
                print("----------------------------------------------------------------------------------------------------------------------------------------------------------------")
                print("|",data[0]," |",data[1],"|",data[2],"|",data[3],"|",data[5],"|",data[6],"|",data[7],"|",data[8],"|",data[9],"| ",data[10]," | ",data[11],"|")
                flag=1
            else:
                pass
        file.close()
        
        if(flag==0):
            print("Customer Id not found")
        else:
            pass
        
        back=int(input("Press ['0'] to go back : "))
        if(back == 0):
            allRecords()
        else:
            exit()
            
    
    elif(uc == 3):
        file=open(r"Hotel Bliss.csv","r",newline='')
        datareader=csv.reader(file)
        nmsearch=input("Enter Name of customer : ")
        for data in datareader:
            if(nmsearch in data[1]):
                print("        *** HOTEL RECORD ***\n")
                print("| Customer ID | Name                 | Phone No.  | Address   |Room No. | Check-In  | Check-Out | Nights Stayed | Price Per Night | Amount | Bill Status |")
                print("----------------------------------------------------------------------------------------------------------------------------------------------------------------")
                print("|",data[0]," |",data[1],"|",data[2],"|",data[3],"|",data[5],"|",data[6],"|",data[7],"|",data[8],"|",data[9],"| ",data[10]," | ",data[11],"|")
                flag=1
            else:
                pass
        file.close()
        
        if(flag==0):
            print("Customer Name not found")
        else:
            pass
        
        
        back=int(input("Press ['0'] to go back : "))
        if(back == 0):
            allRecords()
        else:
            exit()
            
    
    elif(uc == 4):
        file=open(r"Hotel Bliss.csv","r",newline='')
        datareader=csv.reader(file)
        ch_indate=input("Enter  date of Check-in [dd/mm/yyyy] : ")
        for data in datareader:
            if(ch_indate in data[6]):
                print("        *** HOTEL RECORD ***\n")
                print("| Customer ID | Name                 | Phone No.  | Address   |Room No. | Check-In  | Check-Out | Nights Stayed | Price Per Night | Amount | Bill Status |")
                print("----------------------------------------------------------------------------------------------------------------------------------------------------------------")
                print("|",data[0]," |",data[1],"|",data[2],"|",data[3],"|",data[5],"|",data[6],"|",data[7],"|",data[8],"|",data[9],"| ",data[10]," | ",data[11],"|")
                flag=1
            else:
                pass
        file.close()
        
        if(flag==0):
            print("Record not found")
        else:
            pass
        
        back=int(input("Press ['0'] to go back : "))
        if(back == 0):
            allRecords()
        else:
            exit()
            
        
    elif(uc == 5):
        file=open(r"Hotel Bliss.csv","r",newline='')
        datareader=csv.reader(file)
        ch_outdate=input("Enter  date of Check-in [dd/mm/yyyy] : ")
        for data in datareader:
            if(ch_outdate in data[7]):
                print("        *** HOTEL RECORD ***\n")
                print("| Customer ID | Name                 | Phone No.  | Address   |Room No. | Check-In  | Check-Out | Nights Stayed | Price Per Night | Amount | Bill Status |")
                print("----------------------------------------------------------------------------------------------------------------------------------------------------------------")
                print("|",data[0]," |",data[1],"|",data[2],"|",data[3],"|",data[5],"|",data[6],"|",data[7],"|",data[8],"|",data[9],"| ",data[10]," | ",data[11],"|")
                flag=1
            else:
                pass
        file.close()
        
        if(flag==0):
            print("Record not found")
        else:
            pass
        
        back=int(input("Press ['0'] to go back : "))
        if(back == 0):
            allRecords()
        else:
            exit()
            
    
    elif(uc == 6):
        print(" a -> Show all records which have their bill 'Paid' ")
        print(" b -> Show all records which have their bill 'Unpaid' ")
        ch=1
        while(ch==1):
            choice=input("Enter your choice [a/b]: ")
            if(choice == "a"):
                file=open(r"Hotel Bliss.csv","r",newline='')
                datareader=csv.reader(file)
                print("        *** HOTEL RECORD ***\n")
                print("| Customer ID | Name                   | Phone No.  | Address   |Room No. | Check-In  | Check-Out | Nights Stayed | Price Per Night | Amount | Bill Status |")
                print("----------------------------------------------------------------------------------------------------------------------------------------------------------------")
                for data in datareader:
                    if(data[11] == "Paid"):
                        print("|",data[0]," |",data[1],"|",data[2],"|",data[3],"|",data[5],"|",data[6],"|",data[7],"|",data[8],"|",data[9],"| ",data[10]," | ",data[11],"|")
                        flag=1
                    else:
                        pass
                file.close()
                
                if(flag==0):
                    print("Record not found")
                else:
                    pass
                
                ch=0
            
            elif(choice == "b"):
                file=open(r"Hotel Bliss.csv","r",newline='')
                datareader=csv.reader(file)
                print("        *** HOTEL RECORD ***\n")
                print("| Customer ID | Name                   | Phone No.  | Address   |Room No. | Check-In  | Check-Out | Nights Stayed | Price Per Night | Amount | Bill Status |")
                print("----------------------------------------------------------------------------------------------------------------------------------------------------------------")
                for data in datareader:
                    if(data[11] == "Unpaid"):
                        print("|",data[0]," |",data[1],"|",data[2],"|",data[3],"|",data[5],"|",data[6],"|",data[7],"|",data[8],"|",data[9],"| ",data[10]," | ",data[11],"|")
                        flag=1
                    else:
                        pass
                file.close()
                
                if(flag==0):
                    print("Record not found")
                else:
                    pass
                 
                ch=0
            
            else:
                print("Invalid Input")
                ch=1
            
        back=int(input("Press ['0'] to go back : "))
        if(back == 0):
            allRecords()
        else:
            exit()
            
            
    elif(uc == 7):
        file=open(r"Hotel Bliss.csv","r",newline='')
        datareader=csv.reader(file)
        rnumsearch=input("Enter Room number of customer : ")
        for data in datareader:
            if(rnumsearch == data[5]):
                print("        *** HOTEL RECORD ***\n")
                print("| Customer ID | Name                 | Phone No.  | Address   |Room No. | Check-In  | Check-Out | Nights Stayed | Price Per Night | Amount | Bill Status |")
                print("----------------------------------------------------------------------------------------------------------------------------------------------------------------")
                print("|",data[0]," |",data[1],"|",data[2],"|",data[3],"|",data[5],"|",data[6],"|",data[7],"|",data[8],"|",data[9],"| ",data[10]," | ",data[11],"|")
                flag=1
            else:
                pass
        file.close()
        
        if(flag==0):
            print("Room Number not found")
        else:
            pass
        
        back=int(input("Press ['0'] to go back : "))
        if(back == 0):
            allRecords()
        else:
            exit()
     
    elif(uc == 0):
        home()
    
    else:
        print("Invalid Input")
        allRecords()
        
                              
home()