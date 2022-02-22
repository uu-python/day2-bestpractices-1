from .die import Die
from .utils import i_just_throw_an_exception

class GameRunner:

    def __init__(self):
        self.dice = Die.create_dice(5)
        self.reset()

    def reset(self):
        self.round = 1
        self.wins = 0
        self.loses = 0
        
    def reset_dice(self):
        self.dice = Die.create_dice(5)
        return self.dice

    def answer(self):
        total = 0
        for die in self.dice:
            total += die.value # Changed value updated
        return total

    @classmethod
    def run(cls):
        # Probably counts wins or something.
        # Great variable name, 10/10.
        c = 0
        runner = cls() # Moved outside loop
        while True:

            print("Round {}\n".format(runner.round))

            for die in runner.reset_dice(): # Changed from attribute to method call
                print(die.show())

            guess = input("Sigh. What is your guess?: ")
            guess = int(guess)

            if guess == runner.answer():
                print("Congrats, you can add like a 5 year old...")
                c += 1
                runner.round += 1 # Moved this here, round should only increase in case of correct guess
                if c!= 6: continue # moved continued here so player is not prompted to try again if they make correct guess, but haven't won yet
            else:
                print("Sorry that's wrong")
                print("The answer is: {}".format(runner.answer()))
                print("Like seriously, how could you mess that up")
                runner.loses += 1
                c = 0

            if c == 6: # Should have a reset c=0 inside
                print("You won... Congrats...")
                print("The fact it took you so long is pretty sad")
                runner.wins += 1 # Should be inside the c==6 conditional
                #break # No need to break here, player will be prompted

            print("Wins: {} Loses {}".format(runner.wins, runner.loses))
            prompt = input("Would you like to play again?[Y/n]: ")

            if prompt == 'y' or prompt == '':
                continue
            else:
                #i_just_throw_an_exception()
                break # no need for exception, just break the loop
