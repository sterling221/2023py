secret = 7

number = int(input("guess a number between 0 to 10>"))

if number == secret:
    print("Correct")

elif number > secret:
    print("Wrong! your number is a bit bigger.")

else:
    print( "Wrong! your number is a bit smaller.")





