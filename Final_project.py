print("*********Welcome**********")
class Hotelmanage:
    hotel_data=list()
    def __init__(self,name,address,checkin,checkout,roomno):
        self.name=name
        self.address=address
        self.checkin=checkin
        self.checkout=checkout
        self.roomno=roomno
        

    def storedata(self):
        Hotelmanage.hotel_data.append(self) 

    def gethotellist(self):
        return Hotelmanage.hotel_data 

    def __str__(self):
        return"%s,%s,%d,%d,%d"%(self.name,address,checkin,checkout,roomno)    
    def showdetails(self):
        print ("******HOTEL BILL******")
        print ("Customer details:")
        print ("Customer name :",self.name)
        print ("Customer address :",self.address)
        print ("Check in date :",self.checkin)
        print ("Check out date :",self.checkout)
        print("Customer Room No :",self.roomno)
    
    def foodpurchased(self,r=0):
        self.r=r

        print("*****RESTAURANT MENU*****")

        print("1.Dessert=>100\n2.Drinks=>50\n3.Breakfast=>90\n4.Lunch=>110\n5.Dinner=>150\n6.Exit")

        choice=1
        while choice>=1 and choice<=6:
            

            c=int(input("Enter the number of your choice:"))


            if (c==1):
                d=int(input("Enter the quantity:"))
                self.r=self.r+100*d

            elif (c==2):
                 d=int(input("Enter the quantity:"))
                 self.r=self.r+50*d

            elif (c==3):
                 d=int(input("Enter the quantity:"))
                 self.r=self.r+90*d

            elif (c==4):
                 d=int(input("Enter the quantity:"))
                 self.r=self.r+110*d

            elif (c==5):
                 d=int(input("Enter the quantity:"))
                 self.r=self.r+150*d

            elif (c==6):
                break;
            else:
                print("You've Enter an Invalid Key")

        print ("Total food Cost=Rs",self.r,"\n")    



choice=1
HOTEL=Hotelmanage("","",0,0,1)
while choice>=1 and choice<=6:
    print("1.Customer data \n 2.Room rent \n 3.Food Purchasd\n 4.Total cost\n 5.Show Data \n 6.Exit")
    choice=int(input("Enter Choice :"))
    if choice==1:
        name=input("Enter name :")
        address=input("Enter Address :")
        checkin=int(input("Enter Check in date :"))
        checkout=int(input("Enter Check out date :"))
        roomno=int(input("Enter room no :"))
        hotel=Hotelmanage(name,address,checkin,checkout,roomno)
        hotel.storedata()

    elif choice==2:
        print("1.Class A=4000\n2.Class B=3000\n3.Class C=2000\n4.Class D=1000")
        choice=int(input("Enter Choice :"))
        if choice==1:
            stay=int(input("How long You'd Stay? :"))
            print("You Have choose Class A Room")
            print(4000*stay)

            
        elif choice==2:
            stay=int(input("Enter Day :"))
            print("You Have choose Class B Room")
            print(3000*stay)

        elif choice==3:
            stay=int(input("Enter Day :"))
            print("You Have choose Class C Room")
            print(2000*stay)

        elif choice==4:
            stay=int(input("Enter Day :"))
            print("You Have choose Class D Room")
            print(1000*stay)

        else:
            print("Invalid Choice ",choice)
            
    elif choice==3:
        A=Hotelmanage(name,address,checkin,checkout,roomno)
        A.foodpurchased()
                
    elif choice==4:
        a=Hotelmanage(name,address,checkin,checkout,roomno)
        a.showdetails()
        

        
    elif choice==5:
        for h in HOTEL.gethotellist():
            print(h)
    elif choice==6:
        break
print("** Thank You Visit Again **")











