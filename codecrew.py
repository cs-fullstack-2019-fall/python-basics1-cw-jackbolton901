namestr= "My name is "
myName= "Jack"
print( namestr + myName)

userCred = int(input("How much extra credit did you earn?"))
if userCred < 5:
    print("That's not enough credit!")
elif userCred > 20:
    print("That's too much credit!")
    
password = input("Enter Password")
repassword= input("Reenter Password")
if repassword == password:
    print("Correct")
else:
    print("wrong password")
cardNum = input("card number")
cardNum2 = input("card number")
sum = int(cardNum) + int(cardNum2)
if sum == 21:
    print("BLACKJACK!!!!")
elif sum > 21:
    print("BUST")
elif sum < 21:
    print("The total is " + str(sum))