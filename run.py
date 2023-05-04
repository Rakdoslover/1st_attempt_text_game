import time
import sys


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
    """\n The sun is scorching your beaten body as you wake to the sound of waves 
        \n rolling in. Slowly you open your eyes and find yourself laying in the sand. 

        \n Are you content with laying here for the rest 
        \n of the day or do you want to explore?

        \n Type your choice: Stay or Stand?
    """)
    c1 = input()
    time.sleep(1)
    ans = 'incorrect'
    while(ans == 'incorrect'):
        if(c1.upper()=='STAY'):
            print(
            """\n You feel content with where you are and your situation,
                \n the sun travels across the sky and disappears beyond the
                \n horizon. Night falls upon the island and then sleep finds you.
            """)
            ans = 'correct'
            sys.exit("The End")
        elif(c1.upper()=="STAND"):
            print(
            """\n As you stand up you look around and find that you are on a small island.
                \n You can't remember how you got there and you can't make out where you are.
                \n Behind you a path trails off into a dense and dark forest.
            """)
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
    """\n You peer into the dense forest infront of you but can't make 
        \n out anything particular. A small breeze caresses your arms and a 
        \n chill runs down your bones. What awaits you inside the darkness?
        \n Do you want to take the path through forest or stay on 
        \n the edge of the tree line?
        \n Type your choice: Path or Tree line?
    """)
    c1 = input()
    time.sleep(1)
    ans = 'incorrect'
    while(ans == 'incorrect'):
        if(c1.upper()=='PATH'):
            print(
            """\n As you step in under the shadowy boughs you find a lush greenery.
                \n The path slithers onwards like a snake, under roots and over stones 
                \n as far the eye can see.
            """)
            ans = 'correct'
            clearing_scene()
        elif(c1.upper()=="TREE LINE"):
            print(
            """\n You follow the edge of the tree line until you come across a small bay.
                \n From the small dune where you stand, you can see the outlines of a small boat
                \n half buried in the sand.
            """)
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
        \n Standing atop the small dune you see a new path lead off into the dense forest.
        \n On the other side of the bay a large cliffside stops you from 
        \n continuing along the tree line.
        \n You contemplate whether you should investigate the small boat or 
        \n take the path into the forest.

        \n Type your choice: Investigate or Path?
    """)
    c1 = input()
    time.sleep(1)
    ans = 'incorrect'
    while(ans == 'incorrect'):
        if(c1.upper()=='INVESTIGATE'):
            print(
            """\n You descend the dune and start investigating the boat, it's old and 
                \n badly damaged, you can't sail it.
                \n As you move the remains of what could once have been a sail, you find
                \n a water damaged notebook.
                \n Inside someone has scribbled '42 days' page up and page down.
                \n Beyond that nothing else cathes your eye and thus your return to the 
                \n top of the dune and take the path through the forest.
            """)
            ans = 'correct'
            gate_scene()
        elif(c1.upper()=='PATH'):
            print(
            """\n As you step in under the shadowy boughs you find a lush greenery.
                \n The path slithers onwards like a snake, under roots and over stones as far as
                \n the eye can see.
            """)
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
        \n You push a heavy branch to the side and suddenly find yourself in a clearing.
        \n Flowers painted by all the colors of the rainbow grows like a carpet on the ground.
        \n In the middle of the clearing stands a short but solid oak tree, the path that 
        \n you tread takes a right turn by it's foot.
        \n You contemplate whether you should investigate the tree or move on.

        \n Type your choice: Investigate or Move on?
    """)
    c1 = input()
    time.sleep(1)
    ans = 'incorrect'
    while(ans == 'incorrect'):
        if(c1.upper()=='INVESTIGATE'):
            print(
            """\n As you approach the tree you notice a cavity in it, curious as you are,
                \n you reach into it.
                \n It's empty say for one little object, you pick it up, it's small but 
                \n quite heavy.
                \n In your hand lays a golden acorn, it shimmers in the sunlight, 
                \n you put it in your pocket.
                \n You continue your journey into the deeper parts of the forest.
            """)
            player = True
            ans = 'correct'
            gate_scene()
            return player
        elif(c1.upper()=='MOVE ON'):
            print(
            """\n The lovely aroma of the flowers abruptly disappears as you pass
                \n under a large root.
                \n There is a sticky dampness that embraces you, you hear the 
                \n sound of animals in the distance.
            """)
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
        \n You zigzag your way around a couple of weird looking trees as 
        \n you come upon a rusty iron gate.
        \n It is large and it doesnt look like you can go around it.
        \n On the ground in front of it lies five equally large boulders, 
        \n each one with an inscription.
        \n The first one reads 'I', the second reads 'VI', the third reads 'IV',
        \n the fourth reads 'III' 
        \n and the last one reads 'VIII'.
        \n One the someone seems to carved the words 
        \n 'I AM THE LAST ONE, FIVE HAVE LEFT...'
        \n Nonsensicle words or a clue? 

        \n Type your choice: First, Second, Third, Fourth or Fifth?
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
            print(
            """\n When you press the second stone something clicks and the stone 
                \n slowly descends into the ground.
                \n On rusted hinges the large gate squeeks open.
                \n As you pass through, the sounds of the forest suddenly fall silent.
            """)
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
        \n On the other side of the gate a small area opens up 
        \n under the hanging branches.
        \n The greenery around you forms impenetrable walls, in the middle of the
        \n area stands a small stome pillar.
        \n The pillar bears a small engraving symbolizing an acorn, behind the pillar
        \n a tree alley forms a tunnel leading away from the small area.
        \n Would you like to investigate the pillar or move on ahead?

        \n Type your choice: Investigate or Move on?
    """)
    c1 = input()
    time.sleep(1)
    ans ='incorrect'
    while(ans == 'incorrect'):
        if(c1.upper()=='INVESTIGATE'):
            if(player==True):
                print(
                """\n On the top of the pillar is an acorn-shaped hole.
                \n You place the golden acorn in the hole and hear a rumbling sound.
                \nSlowly the pillar starts to spin, as it does a hidden staircase opens up,
                \n you descend down the stairs.
                """)
                ans = 'correct'
                cavern_scene()
            else:
                print(
                """\n On the top of the pillar is an acorn-shaped hole.
                    \n Something seems out of place, put you can't put your finger on what.
                    \n As you can't do more you move along through the tree alley.
                """)
                house_outer_scene()
        elif(c1.upper()=='MOVE ON'):
            print(
            """\n The trees forming the walls of the alley tunnel are so thick that you can't 
                \n see what's on the other side.
                \n As you move along, the alley suddenly becomes very steep, you notice that 
                \n you're climbing a hill.
                \n You climb and climb until you see a house.
            """)
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
        \n A small house, lined by large hedges, sits alone on the little hill
        \n you just finished climbing.
        \n From where you're standing it looks abandoned, the single window is broken
        \n and there are small pieces of glas on the ground.
        \n Do you enter the house or turn around and go back down?

        \n Type your choice: Enter or Return?
    """)
    c1 = input()
    time.sleep(1)
    ans = 'incorrect'
    while(ans == 'incorrect'):
        if(c1.upper()=='ENTER'):
            print(
            """\n You enter through the front door and find yourself in a small kitchen.
                \n The layer of dust indicates that nobody has been here for years.
            """)
            ans = 'correct'
            basket_scene()
        elif(c1.upper()=='RETURN'):
            print(
            """\n You don't want to enter the old house and instead you turn and walk 
                \n down the hill back to the pillar.
            """)
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
        \n You return to the lonely pillar with the engraving of an acorn.
        \n Here the sounds of the world around you falls silent as it did the 
        \n first time you passed through the gate.
        \n Speaking of the gate, it's shut, you try to open it, but it won't budge.
        \n What du you do now?

        \n Type you choice: Investigate or Move on?
    """)
    c1 = input()
    time.sleep(1)
    ans ='incorrect'
    while(ans == 'incorrect'):
        if(c1.upper()=='INVESTIGATE'):
            if(player==True):
                print(
                """\n On the top of the pillar is an acorn-shaped hole.
                    \n You place the golden acorn in the hole and hear a rumbling sound.
                    \n Slowly the pillar starts to spin, as it does a hidden staircase 
                    \n opens up, you descend down the stairs.
                """)
                ans = 'correct'
                cavern_scene()
            else:
                print(
                """\n On the top of the pillar is an acorn-shaped hole.
                    \n Something seems out of place, but you can't put your finger on what.
                    \n As you can't do more you move along through the tree alley.
                """)
                house_outer_scene()
        elif(c1.upper()=='MOVE ON'):
            print(
            """\n You turn around again as you making your way up the steep hill again.
                \n Soon enough you see the small house at the end of the tree alley.
            """)
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
        \n A light reaches you as take the final steps out into a large cave.
        \n Torches light the waste space as you gaze down upon a boat rocking 
        \n steadily on the underground river.
        \n You pick up one of the torches next to you and make your 
        \n down to the boat.
        \n It seems sturdy enough, you untie it and set off downstream.
        \n Again, light reaches you further down, this time though it is daylight.
        \n The wide ocean spreads out infront of you like a beautiful 
        \n carpet and it is yours for the taking.
        \n You raise the sails and leave this mysterious place behind 
        \n once and for all.

        \n Congratulation on escaping the Lost Island!
        \n Until next time stranger!
    """)
    sys.exit("The End")

def basket_scene():
    """
    This is the function defining the players choice by the basket.
    """
    print(
    """
        \n On a round table infront of the unlit fire place is a basket of golden 
        \n acorns, somehow the acorns triggers a memory.
        \n Just over the fire place rests a beautiful short sword, it catches 
        \n your eye as it seems out of place.
        \n Other than that nothing in the small house seems of interest.
        \n What do you do, will you take some acorns or investigate the sword?

        \n Type you choice: Acorns or Investigate?
    """)
    c1 = input()
    time.sleep(1)
    ans = 'incorrect'
    while(ans == 'incorrect'):
        if(c1.upper()=='ACORNS'):
            print(
            """\n You grab a handful of acorns and put them into your pocket.
                \n Something tells you that these might be useful by the 
                \n pillar you passed earlier.
                \n You leave the house and make your way down the tree alley 
                \n towards the lonely pillar.
            """)
            player = True
            ans = 'correct'
            pillar_two_scene()
            return player
        elif(c1.upper()=='INVESTIGATE'):
            print(
            """\n As you lift the sword off it's rest you hear a loud crack 
                \n and the sound of heavy movement.
                \n Instinctively, you take a step backwards, where the fire place 
                \n was just a second ago now stands a tunnel.
                \n It's dark inside but with your new sword you find courage, you get
                \n down on all four and crawl inside.
            """)
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
        \n The short crawl takes you to a secret room on the other 
        \n side of the fire place.
        \n It's a square shaped room with no color, everything is grey and it 
        \n seems as mold has crawled up parts of the walls.
        \n The only light source are two lit candles on the floor, they shine their
        \n light on the wall opposite the tunnel.
        \n Through the swaying light you can make out words and letters, 
        \n it says:
        \n 'Say my name and enter'
        \n Underneath are a bunch of letters:
        \n 'A', 'K', 'A', 'N', 'M', 'Y' and 'D'
        \n What does it mean, you stop to think about it.

        \n Type your answer: 
    """)
    c1 = input()
    time.sleep(1)
    ans = 'incorrect'
    while(ans == 'incorrect'):
        if(c1.upper()=='ADAM'):
            print(
            """\n As you speak the name ADAM a trapdoor suddenly opens up under
                \n you feet and you fall.
                \nThe fall is short as you quickly land on a chute and your 
                \n descent speeds up.
                \n When the chute later comes to an end you find yourself in an 
                \n underground cavern, someone seems to have been here before you 
                \n as there are torches lit all across the spacious area.
                \n Another tunnel seems to be the only way forward, you pick a 
                \n torch off the wall and make your way forward.
            """)
            ans = 'correct'
            ship_scene()
        elif(c1.upper()=='MAYA'):
            print(
            """\n As you speak the name MAYA a trapdoor suddenly opens up under 
                \n your feet and you fall.
                \n The fall is short but devastating, you find yourself at the 
                \n bottom of pit you can't get out of.
                \n As you come to the sad realization you contemplate whether it 
                \n was ever a good idea leave the beach.
            """)
            ans = 'correct'
            sys.exit("The End")
        elif(c1.upper()=='NADYA'):
            print(
            """\n As you speak the name NADYA a hidden door in the wall in front 
                \n of you opens up, it leads downward into the darkness.
                \n Your grip around the short sword tightens as you move deeper 
                \n into the darkness.
                \n A minute passes as you clumsily make your way downward, but 
                \n suddenly you see a strong light.
                \n You step out into a gigantic cavernous space filled to the brim 
                \n with all the treasure you could aver imagine.
                \n On the other side of the enormous space you see pirate ship, you 
                \n think to yourself that this must be some kind of underground hideout.
            """)
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
        \n With your torch in hand you slowly move through the tunnel  
        \n until you end up in another cavern, this one a little bigger.
        \n What you see makes you happy, in the light from the torch you 
        \n can clearly make out an underground river and a boat tied 
        \n around a large rock.
        \n You make your way down to the boat, untie it and sail out of here.
        \n It doesn't take long before the river leads you to 
        \n the ocean, with wind 
        \n in your sail you leave the mysterious island 
        \n behind you, never to return.


        \n Congratulation on escaping the Lost Island!
        \n Until next time stranger!
    """)
    ans = 'correct'
    sys.exit("The End")
    

def gold_scene():
    """
    This is the function leading the player to the gold ending.
    """
    print(
    """
        \n With a hysterical glee you run around like an idiot picking
        \n jewels and gemstones from off the floor and into your pockets.
        \n When at last your pockets are full you start to investigate 
        \n the pirate ship, it's a little older but seems rigid enough 
        \n to make take you off the island.
        \n With both a ship and a treasure at your disposal you feel
        \n content and happy.
        \n It doesn't take long until the ship is filled to the brim with 
        \n all treasure that you could carry.
        \n As you untie the ropes holding the ship you hear a groaning 
        \n sound behind you, you turn around and come face to
        \n face with a roughneck.
        \n 'Oy! Who be you then!?'
        \n 'Takin me gold, ay?'
        \n 'En Garde, YAH!'
        \n You draw you sword and get ready to fight.

        \n Type your action: Slash, Thrust or Parry?
    """)
    c1 = input()
    time.sleep(1)
    ans = 'incorrect'
    while(ans == 'incorrect'):
        if(c1.upper()=='SLASH'):
            print(
            """\n You slash at the pirate, he parries your slash and slashes 
                \n back at you.
                \n A fierce fight erupts, swords clashing against one another.
                \n After a long while you both fall down exhausted 
                \n and panting.
                \n 'Oy! You wanna call it a Tie, mate?'
                \n You agree with the pirate, as you shake it out you both
                \n laugh wholeheartedly, it seems you fought an enemy 
                \n but found a friend instead.
                \n Together you sail off into the sunset, and from that 
                \n day forward you spent the remainder of your 
                \n days pirating the seven seas.
            """)
            ans = 'correct'
            print(
            """\n Congratulation on escaping the Lost Island! 
                \n Until next time stranger!
            """)
            sys.exit("The End")
        elif(c1.upper()=='THRUST'):
            print(
            """\n You thrust your sword towards the roughneck and it plunges 
                \n into his belly, he lets out a roar of pain and falls 
                \n to the deck.
                \n 'Oh the pain, mate! Oh and Eh!'
                \n Victorious you set sail with your treasure-filled ship, 
                \n as you leave this mysterious island behind you, a feeling
                \n of relief fills your body.
            """)
            ans = 'correct'
            print(
            """\n Congratulation on escaping the Lost Island!
                \n Until next time stranger!
            """)
            sys.exit("The End")
        elif(c1.upper()=='PARRY'):
            print(
            """\n You parry and parry the swift slashes thrown at you and 
                \n after fierce moment of fighting the old roughneck suddenly 
                \n lets out a grunt and falls over.
                \n 'Nay! My back! Oh and Eh, it hurts.' 
                \n 'Aye, stranger! I forfeit!'
                \n You pity the man and helps him back to his feet again, 
                \n he thanks you and shakes your hand.
                \n In that moment you both reach an agreement 
                \n and becomes friends.
                \n Together you sail off into the sunset, and from that day 
                \n forward you spent the remainder of your days 
                \n pirating the seven seas.
            """)
            ans = 'correct'
            print(
            """\n Congratulation on escaping the Lost Island! 
                \n Until next time stranger!
            """)
            sys.exit("The End")
        else:
            print("ENTER THE CORRECT OPTION! Slash, Thrust or Parry.")
            c1 = input()


def main():
    """
    Run all program functions
    """
    
    start()

    


print(
    """\n Welcome to the Lost Island!!
        \n Let's dive into the tropical adventure!!
    """)
main()
