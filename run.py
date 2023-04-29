import time


def intro_scene():
    """
    This is the function for my first scene, it introduces the player to the
    'starting position'.
    The general structure of the intro scene might recur through further scenes.
    """

    print("""Welcome to the Lost Island!!
        Let's dive into the tropical adventure!!

        The sun is scorching your beaten body as you wake to the sound of waves rolling in. 
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

intro_scene()