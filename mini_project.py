import random
import os

def main():
    name = input("Hi, what's your name?   ") # user enters name
    print(f"Hi {name}, welcome to the Magic Number Analyzer! \nChoose these options to continue:   ") # gives options

    inp = int(input("\n1- Generate Multiplication Table, \n2- Calculate Sum of Natural Numbers, \n3- Analyze Digits, \n4- Count Vowels, \n5- Play Guess the Number, \n6- Reverse Strings or Numbers\n\n")) # shows user options
    if inp == 1: #if option 1
        multi() #Generate Multiplication Table
    if inp == 2: #if option 2
        print(f"The sum of the natural number is {sumofN()}.") #Calculate Sum of Natural Numbers
    if inp == 3: #if option 3
        print(digilyze())
    if inp == 4: #if option 4
        print(f"Your vowel count is {countvowel()}.")
    if inp == 5: #if option 5
        guessnumber()
    if inp == 6: #if option 6
        print(f"Your word or number reversed is: {reverse()}.")

            
def multi(): #Generate Multiplication Table
    num1 = int(input("Enter number for multiplication table:   "))
    for i in range(1,11):
        print(f"{i} x {num1} = {i*num1}")
        i+=1

def sumofN():
    num = int(input("Enter number:    "))
    i=1
    sum = 0
    while i<num:
        sum=sum+i
        i+=1
    return sum

def digilyze():
    num = int(input("Enter number:    "))
    if num < 0:
        return "Your number is a negative number!" 
    if num % 2 == 0:
        return "Your number is a even number!"
    if num % 2 == 1:
        a = 'Your number is odd'
        for i in range(3, int(num**0.5)+ 1, 2):
            if num % i == 0:
                a = a + " and prime."
    return a

def countvowel():
    vowels = "AEIOUaeiou"
    countinput = input("Enter a word:   ")
    number = 0
    for i in countinput:
        if i in vowels:
            number+=1
    return number

def guessnumber():
    os.system('cls' if os.name == 'nt' else 'clear')
    random_num = random.randint(1, 50)
    tries = 0

    while True:
        try:
            ans = int(input("Guess the number between 1 to 50:   "))
        
            if ans > 50 or ans < 1:
                print("Higher or lower than requirements, please try again.")
                tries += 1
                continue

            elif ans == random_num:
                tries += 1
                print(f"You took {tries} tries!")
                Q = input("Great job, want to try again? (y/n)   ")

                if Q == "y":
                        random_num = random.randint(1, 50)
                        os.system('cls' if os.name == 'nt' else 'clear')
                        continue
                elif Q == "n":
                        os.system('cls' if os.name == 'nt' else 'clear')
                        break
                else:
                    print("I'll assume you want to try again. \U0001F610")
                    continue
            elif ans > random_num:
                print("Too high! Try again.")
                tries += 1
                continue
            elif ans < random_num:
                print("Too low! Try again.")
                tries += 1
                continue
            else:
                ""
                
        except ValueError:
            print("Invalid answer, please try again.")
            tries += 1
            continue

def reverse():
    rInput = input("Enter a number or a word:   ")
    WN = ""
    for i in rInput:
        WN = i + WN
    return WN
        

if __name__ == "__main__":
    main()