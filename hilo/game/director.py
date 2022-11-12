from game.card import Card


class Director:
    """A person who directs the game. 
    
    The responsibility of a Director is to control the sequence of play.

    Attributes:
        dice (List[Die]): A list of Die instances.
        is_playing (boolean): Whether or not the game is being played.
        score (int): The score for one round of play.
        total_score (int): The score for the entire game.
    """

    def __init__(self):
        """Constructs a new Director.
        
        Args:
            self (Director): an instance of Director.
        """
        self.card = []
        self.is_playing = True
        self.score = 300

        for i in range(2):
            card = Card()
            self.card.append(card) #Saves 2 card objects in the self.card list the first torepresent the current card the second for the next card

    def start_game(self):
        """Starts the game by running the main game loop.
        
        Args:
            self (Director): an instance of Director.
        """
        while self.is_playing:
        
            self.do_updates()
            self.do_outputs()
            if (self.score > 0): #if player has more than 0 points get input for if they want to play again
                self.get_inputs()
            else: #otherwise tell the player they ran out of points and set self.is_playing to false, stopping game loop
                print("You are out of points. Goodbye.")
                self.is_playing = False

    def get_inputs(self):
        """Ask the user if they want to roll.

        Args:
            self (Director): An instance of Director.
        """
        roll_dice = input("Play again? [y/n] ")
        self.is_playing = (roll_dice == "y")
       
    def do_updates(self):
        """Updates the player's score.

        Args:
            self (Director): An instance of Director.
        """
        if not self.is_playing:
            return 

        print(f"\nThe card is: {self.card[0].value}")

        player_guess = input("Higher or lower? [h/l] ")

        print(f"The Next card was: {self.card[1].value}")

        if(player_guess =='h' and (self.card[0].value< self.card[1].value)):
            self.score += 100
        elif(player_guess =='l' and (self.card[0].value> self.card[1].value)):
            self.score += 100
        elif(player_guess =='h' and (self.card[0].value> self.card[1].value)):
            self.score -= 75
        elif(player_guess =='l' and (self.card[0].value< self.card[1].value)):
            self.score -= 75
        elif(self.card[0].value== self.card[1].value):
            pass

        print(f"Your score is: {self.score}")
        self.card[0]= self.card[1] # After doing all actions make the new card(self.card[1]) become the start card(self.card[0])
        self.card[1]= Card() #replace 2nd card object in list with a new card

        


    def do_outputs(self):
        """Displays the dice and the score. Also asks the player if they want to roll again. 

        Args:
            self (Director): An instance of Director.
        """
        if not self.is_playing:
            return
        