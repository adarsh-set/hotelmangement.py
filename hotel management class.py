import re
#import hotefun
class hotel:
    def __init__(self,u_name,p_w_d,add_s,che_in,che_out,day,fo_co,total,se_r,se_f):
        self.u_name=u_name
        self.p_w_d=p_w_d
        self.add_s=add_s
        self.che_in=che_in
        self.che_out=che_out
        self.day=day
        self.fo_co=fo_co
        self.total=total
        self.se_r=se_r
        self.se_f=se_f
    def useR(self):
        print(f"User name: {self.u_name} pass: {self.p_w_d}\nSuccessfully Login !")
    def che(self):
        print(f"address: {self.add_s}\nDate : {self.che_in}th to {self.che_out}th")
    def dayni(self):
        print(f"Total cost of Room :{self.day}\n\nFood Details\n            ")
    def fod(self):
        print(f"Total Amound of Food : Rs {self.fo_co}/-\n-_-_-_-_-_-_-_-\nTotal Amound :",self.day + self.fo_co)
    def deta(self):
        pss=re.sub("[\W+\w]","*",self.p_w_d)
        print(f" \nUser Details \n=================\nUser Name: {self.u_name}\nPassword: {pss}\nUser Address : {self.add_s}\nDuration : {self.che_in}th to {self.che_out}th\nRoom Type: {self.se_r}")
        print(f"Room Cost: {self.day}\nFood Type: {self.se_f}\nFood Cost: {self.fo_co}\n================\nTotal   : Rs {self.total}/- \n!!!!!ThankYou!!!!!")
u,p=input("Enter the your name : "),input("Enter the password : ")
ob=hotel(u,p,None,None,None,None,None,None,None,None)
ob.useR()
a=input("Enter the Address : ")
ci,co=int(input("Enter the Starting date : ")),int(input("Closeing date : "))
ob1=hotel(None,None,a,ci,co,None,None,None,None,None)
ob1.che()
print(" Room Types\n================\nAc Room >> (Single : 950),(Family : 1450)\nNon-Ac Room >> (Single : 630),(Family : 930)")
dic={'Ac':{'Single':950,'Family':1450},'Non':{'Single':630,'Family':930}}
n=input("Enter the room Type (Ac/Non) : ")
if n in dic:
    for i in dic[n]:
        print(f"{i} : Rs {dic[n][i]}/-")
    s=input("Single or Famliy  (Single/Family) : ")
    if s in dic[n]:
        print(f"Rs {dic[n][s]} /-")
        d=int(input("How Many Nights : "))
        da,ro=d*dic[n][s],f"{n}/{s}/{d} Nights"
    else:
        da,ro=0,"N/A"
else:
    da,ro=0,"N/A"    
ob3=hotel(None,None,None,None,None,da,None,None,None,None)
ob3.dayni()
print("Food Categories : BreakFast , Lunch , Dessert , AnySoftDrik")
dicn={'BreakFast':{'Dosha':8,'Appam':9,'Chappathi':7},'Lunch':{'Meals':90,'Biriyani':120,'vegM':70},'Dessert':{'icecream':45,'Candy':5,'Cake':18},'SoftDrik':{'Tea':12,'Coffe':10,'Juice':25}}
fd=input("Select Menu : (BreakFast / Lunch / Dessert / SoftDrik : ")
if fd in dicn:
    for i in dicn[fd]:
        print(f"{i} : Rs {dicn[fd][i]}/-")    
    fc=input("Which : ")
    if fc in dicn[fd]:
        pd=int(input("How Many : "))
        pr,fos=pd*dicn[fd][fc],f"{fd}/{fc}/Quantity : {pd}"
    else:
        pr,fos=0,"N/A"       
else:
    fos,pr="N/A",0
ob4=hotel(None,None,None,None,None,da,pr,None,None,None)
ob4.fod()
ht=input(f"Print your Bill  type (Yes) / Cancelled press any key... : ")
if ht == "Yes":
    ob6=hotel(u,p,a,ci,co,da,pr,pr+da,ro,fos)
    ob6.deta()
else:
    print("You Cancelled your Bill")



        



      
