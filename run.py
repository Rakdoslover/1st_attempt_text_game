import time


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
            print("\nFrom where you stand you can see the outlines of something half buried in the sand.")
            ans = 'correct'
            shipwreck_scene()
        else:
            print("ENTER THE CORRECT CHOICE! Path or Tree line?")
            c1 = input()



def main():
    """
    Run all program functions
    """
    intro_scene()

print(""""Welcome to the Lost Island!!
        Let's dive into the tropical adventure!!""")
main()