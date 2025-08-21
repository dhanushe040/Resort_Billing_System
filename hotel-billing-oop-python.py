class resort:
    def __init__(self,rno,name,charges,days):
        self.rno=rno
        self.name=name
        self.charges=charges
        self.days=days
    def compute(self):
        comp=self.days*self.charges
        if comp>11000:
            comp=self.days*self.charges*1.02
            print("Total amount :",comp)
            print("\n")
        else:
            print("Total amount :",comp)
            print()
    def getinfo(self):
        print("Room No :",self.rno)
        print("Name    :",self.name)
        print("Days    :",self.days)
        print("charges :",self.charges)
        print("\n")
    def dipinfo(self):
        print("Dhanush Resort")
        print("Room No      :",self.rno)
        print("Name         :",self.name)
        print("Days         :",self.days)
        print("charges      :",self.charges)
        self.compute()
        print("\n")
while True:
    print("1.read\n2.display  information\n3.Total amount\n4.Bill\n5.Exit\n\n")
    a=int(input("Enter what Do you want :"))
    print()
    if a==1:
        r=int(input("Enter the Room No :"))
        n=str(input("Enter the Customer Name :"))
        c=int(input("Enter the amount of Charges :"))
        d=int(input("Enter the No of  Days :"))
        print("\n")
        obj=resort(r,n,c,d)
    elif a==2:
        try:
            obj.getinfo()
        except NameError:
            print("Please read Go to Option 1\n" )
    elif a==3:
        try:
            obj.compute()
        except NameError:
            print("Please read Go to Option 1\n")
    elif a==4:
        try:
            obj.dipinfo()
        except NameError:
            print("Please read Go to Option 1\n")
    elif a==5:
        print("Thank You\n")
       
    else:
        print("Not Availabe your choice!!!")
        
        
        
           
