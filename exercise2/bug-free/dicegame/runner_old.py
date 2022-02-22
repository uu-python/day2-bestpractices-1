from .die import Die
from .utils import i_just_throw_an_exception

class GameRunner:

    def __init__(self):
        self.dice = Die.create_dice(5)
        self.reset()
        
    def reset_dice(self): # Created in order to reset the dice without everything else
        self.dice = Die.create_dice(5)
        return self.dice

    def reset(self):
        self.round = 1
        self.wins = 0
        self.loses = 0

    def answer(self):
        total = 0
        for die in self.dice:
            total += die.value # Changed from +1 to +die.value
        return total
    
    def try_again(self):
        prompt = input("Would you like to play again?[Y/n]: ")

        if prompt == 'y' or prompt == '':
            #continue
            pass # Changed continue for pass
        else:
            i_just_throw_an_exception()
            #break # There is no need for an exception, we can just exit the loop
            #pass

    @classmethod
    def run(cls):
        # Probably counts wins or something.
        # Great variable name, 10/10.
        c = 0
        
        runner = cls() # Moved from inside to outside the loop
        
        while True:

            print("Round {}\n".format(runner.round))

            for die in runner.reset_dice(): # Changed attribute call to method call
                print(die.show())

            guess = input("Sigh. What is your guess?: ")
            guess = int(guess)

            if guess == runner.answer():
                print("Congrats, you can add like a 5 year old...")
                c += 1
                runner.round += 1 # Since we are continuing we need to update the rounds
                continue # By inserting the continue here we avoid getting unnecessarily prompted after each correct guess
            else:
                print("Sorry that's wrong")
                print("The answer is: {}".format(runner.answer()))
                print("Like seriously, how could you mess that up")
                runner.loses += 1
                c = 0
                runner.try_again() # Calling try_again prompt in case of loss
            print("Wins: {} Loses {}".format(runner.wins, runner.loses))
            runner.round = 0 # The round shouldn't be incremented after a loss

            if c == 6:
                print("You won... Congrats...")
                print("The fact it took you so long is pretty sad")
                runner.wins += 1
                c = 0 # Reset consecutive wins counter in case of victory
                runner.try_again() # Calling try_again prompt in case of victory
                break
            prompt = input("Would you like to play again?[Y/n]: ")

            if prompt == 'y' or prompt == '':
                #continue
                pass # Changed continue for pass
            else:
                #i_just_throw_an_exception()
                break # There is no need for an exception, we can just exit the loop
            
