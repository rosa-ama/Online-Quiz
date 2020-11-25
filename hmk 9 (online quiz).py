print("ONLINE QUIZ")

print('''

*****************************************
WELCOME TO MY ONLONE QUIZ
_____________________________________

MADE BY ROSA-AMA FREMPONG
_____________________________________

SCORE SO FAR:0
4SCORE TO PASS:100


GOOD LUCK ON THIS QUIZ!!
******************************************

''')
print("\n")

score = 0

score = int(score)

firstName = input("Please enter your first name:")

print("\n")

lastName = input("Please enter your last name:")

print("Welcome to the quiz " + firstName + " " + lastName)

print("\n")

email = input ("Do you want to stay logged in yes/no?")

print("\n")


if email == "yes":
    input("Please enter your email:")
    print("\n")
    input("Now please enter your password:")
    print("Saving.....")
    print("Lets get on with the quiz")
    
    
else:
    print("Ok then.. lets get on with teh quiz!!")



print("\n")


print("Question 1")
print("What is the capital of Russia?")

ans1 = ("Moscow")
ans1u = input("Please enter your answer:")

if ans1u == ans1:
     print("BING!")
     print("Right answer!!")
     score = score + 10

else:
     print("ERRHHH")
     print("Wrong answer!!")

print("\n")

print("Question 2")
print("What is 178 * 3?")

ans2 = 534
ans2= int(ans2)
ans2u = input("Please enter your answer:")
ans2u = int(ans2u)

if ans2u == ans2:
    print("Bing!")
    print("Right Answer")
    score = score + 10
else:
    print("ERHHH")
    print("Wrong Answer!")


print("\n")


print("Question 3")
print("Who is the president of the United States?")

ans3 = ("Donalad Trump")
ans3u = input("Please enter your answer:")

if ans3u == ans3:
     print("BING!")
     print("Right answer!!")
     score = score + 10

else:
     print("ERRHHH")
     print("Wrong answer!!")


print("\n")


print("Question 4")
print("Who is the author of the book Harry Potter?")

ans4 = ("J.K Rowling")
ans4u = input("Please enter your answer:")

if ans4u == ans4:
     print("BING!")
     print("Right answer!!")
     score = score + 10

else:
     print("ERRHHH")
     print("Wrong answer!!")


print("\n")


print("Question 5")
print("When was Maya Angelou born?")

ans5 = ("4th April 1928")
ans5u = input("Please enter your answer:")

if ans5u == ans5:
     print("BING!")
     print("Right answer!!")
     score = score + 10

else:
     print("ERRHHH")
     print("Wrong answer!!")



print("\n")


print("Question 6")
print("Where was Simone Biles born ?")

ans6 = ("Columbus, Ohio, U.S")
ans6u = input("Please enter your answer:")

if ans6u == ans6:
     print("BING!")
     print("Right answer!!")
     score = score + 10
    

else:
     print("ERRHHH")
     print("Wrong answer!!")


print("\n")

print('''
*******************************************************
END                  OF                         QUIZ
_______________________________________________________
WELL DONE :)
*******************************************************
''')

print(firstName + " " + lastName + " Your overall score is.. " + str(score))

if (score < 60):
    print("Sorry you failed :(")
else:
    print("Well done you pased the quiz :))")


print("HOPE YOU ENJOYED!!")


     















