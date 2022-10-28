# 2 function banane hain and then proceed with the operations 
# input your choice
# call the functions 
def deposit():
    accountno=input("Enter your account number: ")
    d="D:/"+ accountno +".txt"
    file=open(d,"r")
    stray=file.read()
    print("The current balanace is", stray)
    file.close()
    new=input("Enter the new amount to be deposited to your account: ")
    print("The amount that has to be deposited is", new)
    sum=0
    file=open(d,"w")
    file.seek(0)
    sum=int(stray) + int(new) 
    print("The total amount now present is", sum)
    file.write(str(sum))
    file.close()

def withdrawl():
    accountno=input("Enter your account number: ")
    d="D:/"+ accountno +".txt"
    file=open(d,"r")
    amount=file.read()
    print("The current balance is ", amount)
    file.close()
    new=input("Enter the amount to be taken out: ")
    print("The withdrawl amount is: ", new)
    newamt=0
    file=open(d,"w")
    file.seek(0)
    newamt=int(amount) - int(new)
    print("The total amount present is: ", newamt)
    file.write(str(newamt))
    file.close()

print("Choose 1 for deposit ")
print("Choose 2 for withdrawl ")
choice=int(input("Enter your choice: "))
if choice==1:
    deposit()
if choice==2:
    withdrawl()



