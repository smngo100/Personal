pygame.init() # initializes the background settings that Pygame needs to work properly 
pygame.display.set_mode() # creates a display window, on which we'll draw the game's graphical elements 
run_game() # method contains a while loop that runs continually
           # the loop contains an event loop and code that manages screen updates
pygame.event.get() # returns a list of events that have taken place since the last time this function was called
pygame.display.flip() # tells Pygame to make the most rectnyl drawn screen visible
