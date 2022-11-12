import random



class Card:
    """This is a card, representing a number ranging from 1 to 13

    The responsibility of Card is to keep track of the Cards drawn and draw new cards
   
    Attributes:
        value (int): The number of the card
        
    """

    def __init__(self):
        """Constructs a new instance of Card with a value attribute.

        Args:
        self (Card): An instance of Card.
        """

        self.value = random.randint(1,13)

    def newCard(self):
        """Re-creates a new card Value.

        Args:
        self (Card): An instance of Card.
        """
        self.value = random.randint(1,13)



        
    

        

    
        
        

    

