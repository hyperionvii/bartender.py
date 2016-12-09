import random 

questions = {
     "strong": "Do you like your drinks strong? ",
     "salty":  "Do you like your drinks salty? ",
     "bitter": "Do you like your drinks bitter? ",
     "sweet":  "Do you like your drinks sweet? ",
     "fruity": "Do you like your drinks fruity? ",
}

ingredients = {
     "strong": ["glug of rum", "slug of whisky", "splash of gin"],
     "salty":  ["olive on a stick", "salt-dusted rim", "rasher of bacon"],
     "bitter": ["shake of bitters", "splash of tonic", "twist of lemon peel"],
     "sweet":  ["sugar cube", "spoonful of honey", "splash of cola"],
     "fruity": ["slice of orange", "dash of cassis", "cherry on top"],
}



##function for talking bartender

def bartender():
    """bartender asks what you want and stores information"""
    dictionary = {}
    print("Ar land-lubber! I'll be yer {} today and be helping ye pick a drink. Respond with 'y' or 'n' ".format(bartender))
    
    my_input0 = input(questions["strong"])
    my_input1 = input(questions["salty"])
    my_input2 = input(questions["bitter"])
    my_input3 = input(questions["sweet"])
    my_input4 = input(questions["fruity"])

    if my_input0 == "y":
        dictionary["strong"] = True
    elif my_input0 == "n":
        dictionary["strong"] = False
    else:
        print ("Did ye not hear me? Enter 'y' or 'n'!")
            
    if my_input1 == "y":
        dictionary["salty"] = True
    elif my_input1 == "n":
        dictionary["salty"] = False
    else:
        print ("Did ye not hear me? Enter 'y' or 'n'!")
            
    if my_input2 == "y":
        dictionary["bitter"] = True
    elif my_input2 == "n":
        dictionary["bitter"] = False
    else:
        print ("Did ye not hear me? Enter 'y' or 'n'!")
            
    if my_input3 == "y":
        dictionary["sweet"] = True
    elif my_input3 == "n":
        dictionary["sweet"] = False
    else:
        print ("Did ye not hear me? Enter 'y' or 'n'!")
            
    if my_input4 == "y":
        dictionary["fruity"] = True
    elif my_input4 == "n":
        dictionary["fruity"] = False
    else:
        print ("Did ye not hear me? Enter 'y' or 'n'!")
    
    return dictionary

if __name__ == '__main__':
    dictionary = bartender()
    
    
##call dictionary (list of flavor preferences) and create a list of randomly chosen drink ingredeints
def drink_maker(dictionary):
    """uses ingredient preferences from the dictionary and creates a drink"""
    
    drink_ingredients = []
    
    for flavor in dictionary:
        if dictionary[flavor] == True:
            drink_ingredients.append(random.choice(ingredients[flavor]))
    
    print (drink_ingredients)
        
if __name__ == '__main__':
    print ("Looks like ye be havin'...")
    drink_maker(dictionary)

#come up with random names for the drinks

def drink_name(dictionary):
    """random names based on drink_ingredeints"""
    
    adjectives = {"strong": ["wretched", "rabid", "fresh"], "salty": ["briny", "repulsive"], "bitter": ["tart", "violent", "ugly"], "sweet": ["wicked", "sticky", "fabulous"],"fruity":["apple", "watermelon", "banana", "orange","mango"]
        
    } 
    
    nouns = ["sea snake", "parrot", "dog", "west wind", "starfish"]
    
    
    
    for flavor in dictionary:
        if dictionary[flavor] == True:
            print (random.choice(adjectives[flavor]))
    
    print (random.choice(nouns))

if __name__ == '__main__':
    print ("I call this the...")
    drink_name(dictionary)
    
    
    
    
            