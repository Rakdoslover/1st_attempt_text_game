import time

player = ""

def intro_scene():
    """
    This is the function for my first scene, it introduces the player to the
    'starting position'.
    The general structure of the intro scene might recur through further scenes.
    """

    print(
        """The sun is scorching your beaten body as you wake to the sound of waves rolling in. 
        Slowly you open your eyes and find yourself laying in the sand. 

        Are you content with laying here for the rest of the day or do you want to explore?

        Type your choice: Stay or Stand?
    """)

    c1 = input()
    time.sleep(1)
    ans = 'incorrect'
    while(ans == 'incorrect'):
        if(c1.upper()=='STAY'):
            print("\nYou feel content with where you are and your situation, the sun travels across the sky and disappears beyond the horizon.")
            print("\nNight falls upon the island and then sleep finds you.")
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
        if(c1.upper=='INVESTIGATE'):
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
        if(c1.upper=='INVESTIGATE'):
            print("\nAs you approach the tree you notice a cavity in it, curious as you are, you reach into it.")
            print("\nIt's empty say for one little object, you pick it up, it's small but quite heavy.")
            print("\nIn your hand lays a golden acorn, it shimmers in the sunlight, you put it in your pocket.")
            print("\nYou continue your journey into the deeper parts of the forest.")
            ans = 'correct'
            player = "Golden Acorn"
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
        if(c1.upper=='INVESTIGATE'):
            if(player=='Golden Acorn'):
                print("\nOn the top of the pillar is an acorn-shaped hole.")
                print("\nYou place the golden acorn in the hole and hear a rumbling sound.")
                print("\nSlowly the pillar starts to spin, as it does a hidden staircase opens up, you descend down the stairs.")
                ans = 'correct'
                cavern_scene()
            else:
                print("\nOn the top of the pillar is an acorn-shaped hole.")
                print("\nSomething seems out of place, put you can't put your finge ron what.")
                print("\nAs you can't do more you move aling through the tree alley.")
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


def main():
    """
    Run all program functions
    """
    intro_scene()

print(""""Welcome to the Lost Island!!
        Let's dive into the tropical adventure!!""")
main()