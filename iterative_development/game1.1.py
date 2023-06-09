#version 1.1:
#the player can now pick up things
#the item will be removed from the pos and then added to the inventory.

WIDTH = 3
STARTING_POS = 0

inventory = []
############################
#map size: 3x3, so 0 to 8 pos
#        N
#      W-+-E
#        S
############################

#the map. "desc" is the description of the place,
#"pos" is the player position in numbers,
#and "directions" is the available directions that the player can go

map = [{"desc":"You are in A1. This is the starting position.", "pos":0, "directions":"S/E"}, 
{"desc":"You are in A2.", "pos":1, "directions":"S/E/W"},
{"desc":"You are in A3.", "pos":2, "directions": "S/W", "items":["KNIFE"]},
{"desc":"You are in B1.", "pos":3, "directions": "N/S/E"},
{"desc":"You are in B2.", "pos":4, "directions": "N/S/E/W"},
{"desc":"You are in B3.", "pos":5, "directions": "N/S/W"},
{"desc":"You are in C1.", "pos":6, "directions": "N/E"},
{"desc":"You are in C2", "pos":7, "directions": "N/E/W"},
{"desc":"You are in C3", "pos":8, "directions": "N/W"},]

def move(pos, direction, map):
    """Takes the player position and the direction to move to (N, S, E, or W).
        Returns the new pos of the player after moving."""

    #finds the available directions for this pos
    available_directions = map[pos]["directions"]
    
    direction=direction.upper()
    
    #if the direction entered is available,
    if direction[0] in available_directions: 
        if direction == "E" or direction == "EAST":
            pos += 1
        elif direction == "W" or direction == "WEST":
            pos -= 1
        elif direction == "N" or direction == "NORTH":
            pos -= WIDTH
        elif direction == "S" or direction == "SOUTH":
            pos += WIDTH

        #prints the new place description
        print(map[pos]["desc"])

        new_directions = map[pos]["directions"]
        print(f"You can go {new_directions}.")

    #if they enter anything else,
    else:
        print("You can't go that way...")
        
    return pos
 
def cantake(pos, item):
    """checks if the item that the user entered is actually there"""
    if item in map[pos]["items"]:
        return True
    else:
        return False   
    
def take(pos, item):
    """Take an item, and see if it is in the list of items.
    If it is there, add the item to player's inventory."""
    
    #if what they write matches the item 
    if cantake(pos, item) is True:
        #add item to their inventory
        inventory.append(item)
            
        #remove item from pos so they can't get it again
        map[pos]["items"].remove(item)
                
    #shows them their inventory
    print("Your inventory: "+ str(inventory))
    
#main loop
def game():
    """Main loop for the game"""
    
    #starting position in A1
    pos=STARTING_POS
    print(map[pos]["desc"])
    print("You can go S/E.")
    
    while True:
        #asks player what they want to do
        user_input = input("What do you want to do? ").upper()

        #if they want to go somewhere..
        if user_input.startswith("GO"):
            
            #direction is the direction that they want to go
            direction = user_input.split(" ")[1]
            #move them to new position
            pos = move(pos, direction, map)
            
            #if there are items in the new position, and if the key is not null,
            #print the items
            if "items" in map[pos] and map[pos]["items"]:
                print("There is: " + ', '.join(map[pos]["items"]))
    
        #if they want to take/pick up something
        elif user_input.startswith("TAKE"):

            item = user_input.split(" ")[1]
            
            take(pos, item)

        #if they type something different
        else:
            print("I don't understand that command.")

game()


