import random

def Play_Num_game():
      RandNum = random.randint(1 , 100)
      print("\nWelcome! to the Number guessing game!! ")
      print("\nThe computer has generated a random number from 1 to 100 try to guess it under 10 attempts")

      guess = 0
      count = 1


      while guess != RandNum and count <= 10 :
    
         guess = int(input("Enter your guess:"))

         if( guess < 0 or guess > 100):
          print("Please enter a number between 0 to 100")
 
         elif (guess > RandNum):
           print("OOPS! Too high\nTry again")
           count += 1 
        
         elif(guess < RandNum):
           print("OOPS! Too low\nTry again")
           count += 1   

         

    

      if (guess == RandNum and count <= 10):
        print(f"Congratulations!! you have finally guessed the number in {count} tries") 

      else:
        print("Game over! the correct number was", RandNum)

      

Play_Num_game()

while True:
   again = str(input("Do you wanna play again (yes/no) : "))
   if(again.lower() == "yes" ):
      Play_Num_game()

   else:
      print("Thank you for playing!")
      break   




    