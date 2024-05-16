#if / else

#Treasure island app Game
print("                        .-""""-.
                       / j      \
                      :.d;       ;
                      $$P        :
           .m._       $$         :
          dSMMSSSss.__$$b.    __ :
         :MMSMMSSSMMMSS$$$b  $$P ;
         SMMMSMMSMMMSSS$$$$     :b
        dSMMMSMMMMMMSSMM$$$b.dP SSb.
       dSMMMMMMMMMMSSMMPT$$=-. /TSSSS.
      :SMMMSMMMMMMMSMMP  `$b_.'  MMMMSS.
      SMMMMMSMMMMMMMMM \  .'\    :SMMMSSS.
     dSMSSMMMSMMMMMMMM  \/\_/; .'SSMMMMSSSm
    dSMMMMSMMSMMMMMMMM    :.;'" :SSMMMMSSMM;
  .MMSSSSSMSSMMMMMMMM;    :.;   MMSMMMMSMMM;
 dMSSMMSSSSSSSMMMMMMM;    ;.;   MMMMMMMSMMM
:MMMSSSSMMMSSP^TMMMMM     ;.;   MMMMMMMMMMM
MMMSMMMMSSSSP   `MMMM     ;.;   :MMMMMMMMM;
"TMMMMMMMMMM      TM;    :`.:    MMMMMMMMM;
   )MMMMMMM;     _/\\    :`.:    :MMMMMMMM
  d$SS$$$MMMb.  |._\\\   :`.:     MMMMMMMM
  T$$S$$$$$$$$$$m;O\\\\"-;`.:_.-  MMMMMMM;
 :$$$$$$$$$$$$$$$b_l./\\ ;`.:    mMMSSMMM;
 :$$$$$$$$$$$$$$$$$$$./\\;`.:  .$$MSMMMMMM
  $$$$$$$$$$$$$$$$$$$$. \\`.:.$$$$SMSSSMMM;
  $$$$$$$$$$$$$$$$$$$$$. \\.:$$$$$SSMMMMMMM
  :$$$$$$$$$$$$$$$$$$$$$.//.:$$$$SSSSSSSMM;
  :$$$$$$$$$$$$$$$$$$$$$$.`.:$$SSSSSSSMMMP
   $$$$$$$$$;"^$J "^$$$$;.`.$$P  `SSSMMMM
   :$$$$$$$$$       :$$$;.`.P'..   TMMM$$b
   :$$$$$$$$$;      $$$$;.`/ c^'   d$$$$$S;
   $$$$$S$$$$;      '^^^:_d$g:___.$$$$$$SSS
   $$$$SS$$$$;            $$$$$$$$$$$$$$SSS;
  :$$$SSSS$$$$            : $$$$$$$$$$$$$SSS
  :$P"TSSSS$$$            ; $$$$$$$$$$$$$SSS;
  j    `SSSSS$           :  :$$$$$$$$$$$$$SS$
 :       "^S^'           :   $$$$$$$$$$$$$S$;
 ;.____.-;"               "--^$$$$$$$$$$$$$P
 '-....-"  bug                  ""^^T$$$$P""")
print("Welcome to Treasure Island. Your mission is to find the treasure.")

direction = input("Which way would you like to go? Type 'left' or 'right' \n").lower()
if direction == "left":
    print("You have come to a lake. There is an island in the middle of the lake. Type 'wait' to wait for a boat. Type 'swim' to swim across.\n")
    choice = input().lower()
    if choice == "wait":
        print("You arrive at the island unharmed. There is a house with 3 doors. One red, one yellow and one blue. Which colour do you choose?\n")
        door = input().lower()
        if door == "red":
            print("It's a room full of fire. Game Over.")
        elif door == "yellow":
            print("You found the treasure! You Win!")
        elif door == "blue":
            print("You enter a room of beasts. Game Over.")
        else:
            print("You chose a door that doesn't exist. Game Over.")
    else:
        print("You get attacked by an angry trout. Game Over.")
else:
    print("You fell into a hole. Game Over.")



#Love calculator haha
'''
print("The love Calculator is calculation your score ...")
name1 = input("What is your name? \n")
name2 = input("What is their name? \n")

together = name1 + name2
together = together.lower()
occurence1 = together.count("t") + together.count("r") + together.count("u") + together.count("e")
occurence2 = together.count("l") + together.count("o") + together.count("v") + together.count("e")
rating = int(str(occurence1) + str(occurence2))
print(f"Your score is {rating}")

if rating < 10 or rating > 90:
    print(f"Your score is {rating}, you go together like coke and mentos.")
elif rating >= 40 and rating <= 50:
    print(f"Your score is {rating}, you are alright together.")
else:
    print(f"Your score is {rating}.")
'''

'''
#Pizza order

print("Thank you for choosing Python Pizza Deliveries!")
size = input("What size pizza do you want? S, M, or L ")
add_pepperoni = input("Do you want pepperoni? Y or N ")
extra_cheese = input("Do you want extra cheese? Y or N ")
if size == "S":
    bill = 15
    if add_pepperoni == "Y":
        bill += 2
    if extra_cheese == "Y":
        bill += 1
elif size == "M":
    bill = 20
    if add_pepperoni == "Y":
        bill += 3
    if extra_cheese == "Y":
        bill += 1
elif size == "L":
    bill = 25
    if add_pepperoni == "Y":
        bill += 3
    if extra_cheese == "Y":
        bill += 1
print(f"Your final bill is: ${bill}")
'''

'''
number = int(input("Enter a number "))
if number // 2 == 0:
    print("The number is even")
else:
    print("The number is odd")

elif (BMI 2.0)
'''

'''
height = float(input("Enter your height in m: "))
weight = float(input("Enter your weight in kg: "))
bmi = float(weight / (height ** 2))
bmi = round(bmi, 2)
if bmi < 18.5:  #if bmi < 18.5
    print("You are underweight")
elif bmi >= 18.5 and bmi < 25: # elif bmi < 25
    print("You are normal")
elif bmi >= 25 and bmi < 30:
    print("You are overweight")
elif bmi >= 30 and bmi < 35:
    print("You are obese")
else:
    print("You are clinically obese")
print(bmi)
'''
'''
# Leap year checker app (nested if's)
year = int(input("Which year do you want to check? "))
if year % 4 == 0:
    if year % 100 == 0:
        if year % 400 == 0:
            print("Leap year.")
        else:
            print("Not leap year.")
    else:
        print("Leap year.")
else:
    print("Not leap year.")
'''
'''
# Multiple if in succession
print("Welcome to the rollercoaster!")
height = int(input("What is your height in cm? "))
bill = 0

if height >= 120:
    print("You can ride the rollercoaster!")
    age = int(input("What is your age? "))
    if age < 12:
        bill = 5
        print("Please pay $5.")
    elif age <= 18:
        bill = 7
        print("Please pay $7.")
    else:
        bill = 12
        print("Please pay $12.")

    wants_photo = input("Do you want a photo taken? Y or N. ")
    if wants_photo == "Y":
        bill += 3
    print(f"Your total bill is ${bill}")
else:
    print("Sorry, you have to grow taller before you can ride.")
'''