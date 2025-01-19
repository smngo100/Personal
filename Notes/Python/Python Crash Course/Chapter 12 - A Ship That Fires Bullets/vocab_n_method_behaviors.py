##### Vocabulary #####
# A 'SURFACE' in Pygame is a part of the screen where a game elemnt can be displayed.
# An 'EVENT' is an action that the user performs while playing the game, such as pressing a key or moving the mouse. 
# A 'HELPER METHOD' does work inside a class but isn't meant to be used by code outside the class.
           # In Python, a single leading underscore indiciates a helper method.


##### Method behaviors #####
pygame.init() # initializes the background settings that Pygame needs to work properly 
pygame.display.set_mode() # creates a display window, on which we'll draw the game's graphical elements 
run_game() # method contains a while loop that runs continually
           # the loop contains an event loop and code that manages screen updates
pygame.event.get() # returns a list of events that have taken place since the last time this function was called
pygame.display.flip() # tells Pygame to make the most rectnyl drawn screen visible


##### Events #####
# KEYDOWN: When the player presses down on the key
# KEYUP: When the player releases the key


##### Keyboard Input #####
# K_RIGHT: Right arrow key
# K_LEFT: Left arrow key
