def choose(user_response, user_name):
    #1.  you choose to abscond and run away.
    if (user_response == 1):
        print("He looks around and see you running suddenly he appears in front of you and sucker stabs you in the chest")
        user_response = int(input("1. He finishes off your last man and looks around"))
        choose(user_response, user_name)
        
    #2. You try to fight. 
    elif (user_response == 2):
        print('He gets tired of you trying to hurt him and he punches your jaw breaking your neck and sending your lifeless body flying',
        
        user_response = input("Choices TBD")

    #3. You choose to rise up and save somebody'
    elif (user_response == 3):
        print('JACK NOIR cracks the last neck of the person you were going to save "what do you think your doing?', user_name, 'your turn.')
        user_response = input("Choices TBD")
        
    else:
        error(user_response)
        
def error(user_response):
    if(user_response == 2017):
        print("easter egg :D")
    else:
        print("Nice try! Now comply with the rules!")
        #add code to repeat gather user input

begin_story()
def begin_story(): 
    user_name = input("Please enter your name")
    print('You watch as the visious arch agent JACK NOIR kills your squad of soldiers.','What do you do?')
    print('Enter the number that corresponds to your decision')
    user_response = int(input('1. You choose to abscond and run away \n2. You choose to agress and fight for yourself \n3. You choose to rise up and try and save somebody'))
    choose(user_response, user_name)

def choose(user_response, user_name):
    #1.  you choose to abscond and run away.
    if (user_response == 1):
        print("The arch agent doesnt notice you running")
        user_response = int(input("1. He finishes off your last man and looks around"))
        choose(user_response, user_name)
        
    #2. You try to fight. 
    elif (user_response == 2):
        print('He laughs at the pityful slashes of your sword',
        '"Good try but Look,', user_name, ', Im going to kill you like the rest of them.')
        user_response = input("Choices TBD")

    #3. You choose to rise up and save somebody'
    elif (user_response == 3):
        print('JACK NOIR makes quick slash and you fall and bleed from your carapace "hm?', user_name, ' i  think the knew you.')
        user_response = input("Choices TBD")
        
    else:
        error(user_response)
        
def error(user_response):
    if(user_response == 2017):
        print("easter egg :D")
    else:
        print("Nice try! Now comply with the rules!")
        #add code to repeat gather user input

begin_story()
