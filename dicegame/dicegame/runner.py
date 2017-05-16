# FIXED: in addition to ahe Die class, we also want to import the roll function from the die module
from .die import Die, roll
from .utils import i_just_throw_an_exception

class GameRunner:

    def __init__(self):
        self.dice = Die.create_dice(5)
        self.reset()

    def reset(self):
        self.round = 1
        self.wins = 0
        self.loses = 0

    def answer(self):
        total = 0
        for die in self.dice:
            # FIXED: We actually want to sum up the value of each dice (not just increment by one)
            total += die.value
        return total

    @classmethod
    def run(cls):
        # Probably counts wins or something.
        # Great variable name, 10/10.
        c = 0

        # FIXED: This runner object should be created outside the while loop
        # (Otherwise all the history is lost once we go to the next roung)
        runner = cls()
        
        while True:

            print("Round {}\n".format(runner.round))

            # FIXED: We should actually roll the dices, before we do anything else
            # (therefore we needed to import the roll function)
            roll(runner.dice)
            
            for die in runner.dice:
                print(die.show())

            guess = input("Sigh. What is your guess?: ")
            guess = int(guess)

            if guess == runner.answer():
                print("Congrats, you can add like a 5 year old...")
                runner.wins += 1
                c += 1
            else:
                print("Sorry that's wrong")
                print("The answer is: {}".format(runner.answer))
                print("Like seriously, how could you mess that up")
                runner.loses += 1
                c = 0
            print("Wins: {} Loses {}".format(runner.wins, runner.loses))
            runner.round += 1

            if c == 6:
                print("You won... Congrats...")
                print("The fact it took you so long is pretty sad")
                break

            # FIXED: For backwards-compatibilty with Python 2, we should use raw_input
            import sys
            if sys.version_info[0] >= 3:
                get_input = input
            else:
                get_input = raw_input
            
            prompt = get_input("Would you like to play again?[Y/n]: ")

            # FIXED: We should use the lower function to accept both Y and y as valid input
            if prompt.lower() == 'y' or prompt == '':
                continue
            else:
                break
