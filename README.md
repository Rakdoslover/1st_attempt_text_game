# Welcome to The Lost Island!

The Lost Island is a text-based adventure game involving you the player as "The Stranger".

You wake up on a sunny beach somewhere in time and space, you have no memory and no idea of where you are.
Can you somehow figure out a way to get off the island? We'll see about that!

![Responsive Screenshot](assets/images/responsive.jpg)
## Game Features

The main functions of the game is letting the player make decisions(up towards 5 choices) at each scene, that guides them off the island.
The decisions varies from simple prompts to writing or spelling names.
Depending on the players choices he/she gets a new scene defined byt their answer.

The game features multiple endings, both good and bad and can even be "cleared" at the very first stage.

Implemented a basic item pickups system where as if the player made a certain choice beforehand, they get a specific scenerio where there usually isn't one. This happens at least 3 times in story.

## Future Features

### Scrolling Text
I did experiment with scrolling text in the beginning of the project, it is something i'm still interested in and would like to implement.
Found a good link to a youtuber with easy instructions but didn't have time to implement it before deadline.

### Bigger Item System

From the very start I found the idea of making the endings different depending on the items you picked up/ used during the adventure.
It's a bigger assignement and I will continue to implement this idea further.

## Project Chart (Lucid Chart alternative)

![Photo of the chart](assets/images/chart.jpg)

## Testing
The project has been test manually by doing the following things:
- Responsive dimensions through the inspect function on Google Chrome.
- Checked Python syntax errors in ExtendsClass [ExtendsClass](https://extendsclass.com/python-tester.html). Found no problem with the code.
- Checked Python in [CI Python Linter](https://pep8ci.herokuapp.com/)
![CI Linter Python](assets/images/no-errors.jpg)
- Tried all scene with different commands that's not supposed to work and got the correct responses, the program wouldn't break.

| Scene | Should do | Errors | Works |
|-------|-----------|--------|-------|
| start | Start the game | No error | Yes |
| intro scene | First choice | No error | Yes |
| beach scene | Second choice | No error | Yes |
| shipwreck scene | Give a hint | No error | Yes |
| clearing scene | Item pickup | No error | Yes |
| gate scene | Question | No error | Yes |
| pillar scene | Item give away | No error | Yes |
| house outer scene | Back and forth point | No error | Yes |
| pillar two scen | Item give away | No error | Yes |
| cavern scene | Ending part | No error | Yes |
| basket scene | Item pickup | No error | Yes |
| secret room scene | Question | No error | Yes |
| ship scene | Ending part | No error | Yes |
| gold scene | Ending part | No error | Yes |


### Screenshots screens
Laptop size
![Screenshot of laptop](assets/images/laptop-size.jpg)

Ipad size
![Screenshot of Ipad](assets/images/ipad-size.jpg)

Phone size
![Screenshot of Phone](assets/images/phone-standing.jpg)

### Bugs

Have a had a problem with the item system. It won't react to the players choice after picking up the right item.
For now it is not implemented into the final version of the game.

## Deployment

The project was deployed using Code Institutes's mock terminal for Heroku.

Steps for deployment:
    1. Made the repository link for GitHub.
    2. Created a new app on Heroku.
    3. Set the buildbacks to Python and NodeJS, in that order.
    4. Link the Heroku app to the repository.
    5. Clicked on the "Deploy".



## Credits
- Code Institute for for the deployment terminal.
- AskPython for the idea of the main functions in the game.
- All the help of my mentor for guiding me through the process.