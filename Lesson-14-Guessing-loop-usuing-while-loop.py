Actual_price = 10
Guessing_count = 0
Guessing_limit = 5  # Corrected the typo

while Guessing_count < Guessing_limit:
    Guess = int(input('Guess the price: '))
    Guessing_count += 1
    
    if Guess == Actual_price:
        print("You have won!")
        break
    else:
        print("You're Failed")
else :
   
    print("Game Over! You've used all your guesses.")

        
       
