import time

player = False

def start():
    """
    This is the function starting the game.
    """
    print(
    """
    \n Ready to get started?
    \n Type Start!
    """)
    c1 = input()
    time.sleep(1)
    ans = 'incorrect'
    while(ans == 'incorrect'):
        if(c1.upper()=='START'):
            intro_scene()
        else:
            print("Really.. Try typing Start")
            c1 = input()

        
def intro_scene():
    """
    This is the function for my first scene, it introduces the player to the
    'starting position'.
    The general structure of the intro scene might recur through further scenes.
    """

    print(
    """\n The sun is scorching your beaten body as you wake to the sound of waves rolling in. 
        \n Slowly you open your eyes and find yourself laying in the sand. 

        \n Are you content with laying here for the rest 
        \n of the day or do you want to explore?

        \n Type your choice: Stay or Stand?
    """)
    c1 = input()
    time.sleep(1)
    ans = 'incorrect'
    while(ans == 'incorrect'):
        if(c1.upper()=='STAY'):
            print("""\n You feel content with where you are and your situation,\n
                 the sun travels across the sky and disappears beyond the horizon.\n
                 Night falls upon the island and then sleep finds you.
                 """)
            ans = 'correct'
        elif(c1.upper()=="STAND"):
            print("\nAs you stand up you look around and find that you are on a small island.")
            print("\nYou can't remember how you got there and you can't make out where you are.")
            print("\nBehind you a path trails off into a dense and dark forest.")
            ans = 'correct'
            beach_scene()
        else:
            print("ENTER THE CORRECT CHOICE! Stay or Stand?")
            c1 = input()


def beach_scene():
    """
    This is the function defining the players choice on the beach.
    """

    print(
        """You peer into the dense forest infront of you but can't make out anything particular.
        A small breeze caresses your arms and a chill runs down your bones.
        What awaits you inside the darkness?
        Do you want to take the path through forest or stay on the edge of the tree line?

        Type your choice: Path or Tree line?
    """)
    c1 = input()
    time.sleep(1)
    ans = 'incorrect'
    while(ans == 'incorrect'):
        if(c1.upper()=='PATH'):
            print("\nAs you step in under the shadowy boughs you find a lush greenery.")
            print("\nThe path slithers onwards like a snake, under roots and over stones as far the eye can see.")
            ans = 'correct'
            clearing_scene()
        elif(c1.upper()=="TREE LINE"):
            print("\nYou follow the edge of the tree line until you come across a small bay.")
            print("\nFrom the small dune where you stand you can see the outlines of a small boat half buried in the sand.")
            ans = 'correct'
            shipwreck_scene()
        else:
            print("ENTER THE CORRECT CHOICE! Path or Tree line?")
            c1 = input()


def shipwreck_scene():
    """
    This is the function defining the players choice by the shipwreck.
    """

    print(
        """
        Standing atop the small dune you see a new path lead off into the dense forest.
        On the other side of the bay a large cliffside stops you from continuing along the tree line.
        You contemplate whether you should investigate the small boat or take the path into the forest.

        Type your choice: Investigate or Path?
    """)
    c1 = input()
    time.sleep(1)
    ans = 'incorrect'
    while(ans == 'incorrect'):
        if(c1.upper()=='INVESTIGATE'):
            print("\nYou descend the dune and start investigating the boat, it's old and badly damaged, you can't sail it.")
            print("\nAs you move the remains of what could once have been a sail, you find a water damaged notebook.")
            print("\nInside someone has scribbled '42 days' page up and page down.")
            print("\nBeyond that nothing else cathes your eye and thus your return to the top of the dune and take the path through the forest.")
            ans = 'correct'
            gate_scene()
        elif(c1.upper()=='PATH'):
            print("\nAs you step in under the shadowy boughs you find a lush greenery.")
            print("\nThe path slithers onwards like a snake, under roots and over stones as far the eye can see.")
            ans = 'correct'
            gate_scene()
        else:
            print("ENTER THE CORRECT CHOICE! Investigate or Path?")
            c1 = input()


def clearing_scene():
    """
    This is the function defining the players choice by the clearing.
    """

    print(
        """
        You push a heavy branch to the side and suddenly find yourself in a clearing.
        Flowers painted by all the colors of the rainbow grows like a carpet on the ground.
        In the middle of the clearing stands a short but solid oak tree, the path that you tread takes a right turn by it's foot.
        You contemplate whether you should investigate the tree or move on.

        Type your choice: Investigate or Move on?
    """)
    c1 = input()
    time.sleep(1)
    ans = 'incorrect'
    while(ans == 'incorrect'):
        if(c1.upper()=='INVESTIGATE'):
            print("\nAs you approach the tree you notice a cavity in it, curious as you are, you reach into it.")
            print("\nIt's empty say for one little object, you pick it up, it's small but quite heavy.")
            print("\nIn your hand lays a golden acorn, it shimmers in the sunlight, you put it in your pocket.")
            print("\nYou continue your journey into the deeper parts of the forest.")
            ans = 'correct'
            player = True
            return player
            gate_scene()
        elif(c1.upper()=='MOVE ON'):
            print("\nThe lovely aroma of the flowers abruptly disappears as you pass under a large root.")
            print("\nThere is a sticky dampness that embraces you, you hear the sound of animals in the distance.")
            ans = 'correct'
            gate_scene()
        else:
            print("ENTER THE CORRECT CHOICE! Investigate or Move on?")
            c1 = input()


def gate_scene():
    """
    This is the function defining the players choice by the gate.
    """
    print(
        """
        You zigzag your way around a couple of weird looking trees as you come upon a rusty iron gate.
        It is large and it doesnt look like you can go around it.
        On the ground in front of it lies five equally large boulders, each one with an inscription.
        The first one reads 'I', the second reads 'VI', the third reads 'IV', the fourth reads 'III' and the last one reads 'VIII'.
        One the someone seems to carved the words 'I AM THE LAST ONE, FIVE HAVE LEFT...'
        Nonsensicle words or a clue? 

        Type your choice: First, Second, Third, Fourth or Fifth?
    """)
    c1 = input()
    time.sleep(1)
    ans = 'incorrect'
    while(ans == 'incorrect'):
        if(c1.upper()=='FIRST'):
            print("""Nothing happens, you try again.
            Type your choice: First, Second, Third, Fourth or Fifth?""")
            c1 = input()
        elif(c1.upper()=='SECOND'):
            print("\nWhen you press the second stone something clicks and the stone slowly descends into the ground.")
            print("\nOn rusted hinges the large gate squeeks open.") 
            print("\nAs you pass through, the sounds of the forest suddenly fall silent.")
            ans = 'correct'
            pillar_scene()
        elif(c1.upper()=='THIRD'):
            print("""Nothing happens, you try again.
            Type your choice: First, Second, Third, Fourth or Fifth?""")
            c1 = input()
        elif(c1.upper()=='FOURTH'):
            print("""Nothing happens, you try again.
            Type your choice: First, Second, Third, Fourth or Fifth?""")
            c1 = input()
        elif(c1.upper()=='FIFTH'):
            print("""Nothing happens, you try again.
            Type your choice: First, Second, Third, Fourth or Fifth?""")
            c1 = input()
        else:
            print("TRY AGAIN: First, Second, Third, Fourth or Fifth?")
            c1 = input()


def pillar_scene():
    """
    This is the function defining the players choice by the pillar.
    """

    print(
        """
        On the other side of the gate a small area opens up under the hanging branches.
        The greenery around you forms impenetrable walls, in the middle of the area stands a small stome pillar.
        The pillar bears a small engraving symbolizing an acorn, behind the pillar a tree alley forms a tunnel leading away from the small area.
        Would you like to investigate the pillar or move on ahead?

        Type your choice: Investigate or Move on?
    """)
    c1 = input()
    time.sleep(1)
    ans ='incorrect'
    while(ans == 'incorrect'):
        if(c1.upper()=='INVESTIGATE'):
            if(player):
                print("\nOn the top of the pillar is an acorn-shaped hole.")
                print("\nYou place the golden acorn in the hole and hear a rumbling sound.")
                print("\nSlowly the pillar starts to spin, as it does a hidden staircase opens up, you descend down the stairs.")
                ans = 'correct'
                cavern_scene()
            else:
                print("\nOn the top of the pillar is an acorn-shaped hole.")
                print("\nSomething seems out of place, put you can't put your finger on what.")
                print("\nAs you can't do more you move along through the tree alley.")
                house_outer_scene()
        elif(c1.upper()=='MOVE ON'):
            print("\nThe trees forming the walls of the alley tunnel are so thick that you can't see what's on the other side.")
            print("\nAs you move along, the alley suddenly becomes very steep, you notice that you're climbing a hill.")
            print("\nYou climb and climb until you see a house.")
            ans = 'correct'
            house_outer_scene()
        else:
            print("ENTER THE CORRECT CHOICE! Investigate or Move on?")
            c1 = input()


def house_outer_scene():
    """
    This is the function defining the players choice outside the house.
    """

    print(
        """
        A small house, lined by large hedges, sits alone on the little hill you just finished climbing.
        From where you're standing it looks abandoned, the single window is broken and there are small pieces of glas on the ground.
        Do you enter the house or turn around and go back down?

        Type your choice: Enter or Return?
    """)
    c1 = input()
    time.sleep(1)
    ans = 'incorrect'
    while(ans == 'incorrect'):
        if(c1.upper()=='ENTER'):
            print("\nYou enter through the front door and find yourself in a small kitchen.")
            print("\nThe layer of dust indicates that nobody has been here for years.")
            ans = 'correct'
            basket_scene()
        elif(c1.upper()=='RETURN'):
            print("\nYou don't want to enter the old house and instead you turn and walk down the hill back to the pillar.")
            ans = 'correct'
            pillar_two_scene()
        else:
            print("ENTER THE CORRECT CHOICE! Enter or Return?")
            c1 = input()


def pillar_two_scene():
    """
    This the function defining the players choice back at the pillar
    """
    print(
        """
        You return to the lonely pillar with the engraving of an acorn.
        Here the sounds of the world around you falls silent as it did the first time you passed through the gate.
        Speaking of the gate, it's shut, you try to open it, but it won't budge.
        What du you do now?

        Type you choice: Investigate or Move on?
    """)
    c1 = input()
    time.sleep(1)
    ans ='incorrect'
    while(ans == 'incorrect'):
        if(c1.upper()=='INVESTIGATE'):
            if(player):
                print("\nOn the top of the pillar is an acorn-shaped hole.")
                print("\nYou place the golden acorn in the hole and hear a rumbling sound.")
                print("\nSlowly the pillar starts to spin, as it does a hidden staircase opens up, you descend down the stairs.")
                ans = 'correct'
                cavern_scene()
            else:
                print("\nOn the top of the pillar is an acorn-shaped hole.")
                print("\nSomething seems out of place, put you can't put your finger on what.")
                print("\nAs you can't do more you move along through the tree alley.")
                house_outer_scene()
        elif(c1.upper()=='MOVE ON'):
            print("\nYou turn around again as you making your way up the steep hill again.")
            print("\nSoon enough you see the small house at the end of the tree alley.")
            ans = 'correct'
            house_outer_scene()
        else:
            print("ENTER THE CORRECT CHOICE! Investigate or Move on?")
            c1 = input()


def cavern_scene():
    """
    This is the function leading the player through the cavern after the pillar.
    """
    print(
        """
        A light reaches you as take the final steps out into a large cave.
        Torches light the waste space as you gaze down upon a boat rocking steadily on the underground river.
        You pick up one of the torches next to you and make your down to the boat.
        It seems sturdy enough, you untie it and set off downstream.
        Again, light reaches you further down, this time though it is daylight.
        The wide ocean spreads out infront of you like a beautiful carpet and it is yours for the taking.
        You raise the sails and leave this mysterious place behind once and for all.

        Congratulation on escaping the Lost Island!
        Until next time stranger!
    """)


def basket_scene():
    """
    This is the function defining the players choice by the basket.
    """
    print(
        """
        On a round table infront of the unlit fire place is a basket of golden acorns, somehow the acorns triggers a memory.
        Just over the fire place rests a beautiful short sword, it catches your eye as it seems out of place.
        Other than that nothing in the small house seems of interest.
        What do you do, will you take some acorns or investigate the sword?

        Type you choice: Acorns or Investigate?
    """)
    c1 = input()
    time.sleep(1)
    ans = 'incorrect'
    while(ans == 'incorrect'):
        if(c1.upper()=='ACORNS'):
            print("\nYou grab a handful of acorns and put them into your pocket.")
            print("\nSomething tells you that these might be useful by the pillar you passed earlier.")
            print("\nYou leave the house and make your way down the tree alley towards the loenly pillar.")
            ans = 'correct'
            player = True
            return player
            pillar_two_scene()
        elif(c1.upper()=='INVESTIGATE'):
            print("\nAs you lift the sword off it's rest you hear a loud crack and the sound of heavy movement.")
            print("\ninstinctively, you take a step backwards, where the fire place was just a second ago now stands a tunnel.")
            print("\nIt's dark inside but with your new sword you find courage, you get down on all four and crawl inside.")
            ans = 'correct'
            secret_room_scene()
        else:
            print("ENTER THE CORRECT CHOICE! Acorns or Investigate?")
            c1 = input()


def secret_room_scene():
    """
    This is the function defining the players choice inside the secret room.
    """
    print(
        """
        The short crawl takes you to a secret room on the other side of the fire place.
        It's a square shaped room with no color, everything is grey and it seems as mold has crawled up parts of the walls.
        The only light source are two lit candles on the floor, they shine their light on the wall opposite the tunnel.
        Through the swaying light you can make out words and letters, it says:
        'Say my name and enter'
        Underneath are a bunch of letters:
        'A', 'K', 'A', 'N', 'M', 'Y' and 'D'
        What does it mean, you stop to think about it.

        Type your answer: 
    """)
    c1 = input()
    time.sleep(1)
    ans = 'incorrect'
    while(ans == 'incorrect'):
        if(c1.upper()=='ADAM'):
            print("\nAs you speak the name ADAM a trapdoor suddenly opens up under you feet and you fall.")
            print("\nThe fall is short as you quickly land on a chute and your descent speeds up.")
            print("\nWhen the chute later comes to an end you find yourself in an underground cavern, someone seems to have been here before you as there are torches lit all across the spacious area.")
            print("\nAnother tunnel seems to be the only way forward, you pick a torch off the wall and make your way forward.")
            ans = 'correct'
            ship_scene()
        elif(c1.upper()=='MAYA'):
            print("\nAs you speak the name MAYA a trapdoor suddenly opens up under your feet and you fall.")
            print("\nThe fall is short but devastating, you find yourself at the bottom of pit you can't get out of.")
            print("\nAs you come to the sad realization you contemplate whether it was ever a good idea leave the beach.")
            ans = 'correct'
        elif(c1.upper()=='NADYA'):
            print("\nAs you speak the name NADYA a hidden door in the wall in front of you opens up, it leads downward into the darkness.")
            print("\nYour grip around the short sword tightens as you move deeper into the darkness.")
            print("\nA minute passes as you clumsily make your way downward, but suddenly you see a strong light.")
            print("\nYou step out into a gigantic cavernous space filled to the brim with all the treasure you could aver imagine.")
            print("\nOn the other side of the enormous space you see pirate ship, you think to yourself that this must be some kind of underground hideout.")
            ans = 'correct'
            gold_scene()
        else:
            print("ENTER THE CORRECT NAME! Please try again.")
            c1 = input()


def ship_scene():
    """
    This is the function leading the player to the ship ending.
    """
    print(
        """
        With your torch in hand you slowly move through the tunnel until you end up in another cavern, this one a little bigger.
        What you see makes you happy, in the light from the torch you can clearly make out an underground river and a boat tied around a large rock.
        You make your way down to the boat, untie it and sail out of here.
        It doesn't take long before the river leads you to the ocean, with wind in your sail you leave the mysterious island behind you, never to return.


        Congratulation on escaping the Lost Island!
        Until next time stranger!
    """)
    ans = 'correct'
    

def gold_scene():
    """
    This is the function leading the player to the gold ending.
    """
    print(
        """
        With a hysterical glee you run around like an idiot picking jewels and gemstones from off the floor and into your pockets.
        When at last your pockets are full you start to investigate the pirate ship, it's a little older but seems rigid enough to make take you off the island.
        with both a ship and a treasure at your disposal you feel content and happy.
        It doesn't take long until the ship is filled to the brim with all treasure that you could carry.
        As you untie the ropes holding the ship you hear a groaning sound behind you, you turn around and come face to face with a roughneck.
        'Oy! Who be you then!?
        Takin me gold, ay?'
        En Garde, YAH!'
        You draw you sword and get ready to fight.

        Type your action: Slash, Thrust or Parry?
    """)
    c1 = input()
    time.sleep(1)
    ans = 'incorrect'
    while(ans == 'incorrect'):
        if(c1.upper()=='SLASH'):
            print("\nYou slash at the pirate, he parries your slash and slashes bakc at you.")
            print("\nA fierce fight erupts, swords clashing against one another.")
            print("\nAfter a long while you both fall down exhausted and panting.")
            print("\n'Oy! You wanna call it a Tie, mate?'")
            print("\nYou agree with the pirate, as you shake it out you both laugh wholeheartedly, it seems you fought an enemy but found a friend instead.")
            print("\nTogether you sail off into the sunset, and from that day forward you spent the remainder of your days pirating the seven seas.")
            ans = 'correct'
            print("\n Congratulation on escaping the Lost Island! Until next time stranger!")
        elif(c1.upper()=='THRUST'):
            print("\nYou thrust your sword towards the roughneck and it plunges into his belly, he lets out a roar of pain and falls to the deck.")
            print("\n'Oh the pain, mate! Oh and Eh!'")
            print("\nVictorious you set sail with your treasure-filled ship, as you leave this mysterious island behind you, a feeling of relief fills your body.")
            ans = 'correct'
            print("\n Congratulation on escaping the Lost Island! Until next time stranger!")
        elif(c1.upper()=='PARRY'):
            print("\nYou parry and parry the swift slashes thrown at you and after fierce moment of fighting the old roughneck suddenly lets out a grunt and falls over.")
            print("\n'Nay! My back! Oh and Eh, it hurts. Aye, stranger! I forfeit!'")
            print("\nYou pity the man and helps him back to his feet again, he thanks you and shakes your hand.")
            print("\nIn that moment you both reach an agreement and becomes friends.")
            print("\nTogether you sail off into the sunset, and from that day forward you spent the remainder of your days pirating the seven seas.")
            ans = 'correct'
            print("\n Congratulation on escaping the Lost Island! Until next time stranger!")
        else:
            print("ENTER THE CORRECT OPTION! Slash, Thrust or Parry.")
            c1 = input()


def main():
    """
    Run all program functions
    """
    start()


print(""" Welcome to the Lost Island!!\n
        \n Let's dive into the tropical adventure!!""")
main()
