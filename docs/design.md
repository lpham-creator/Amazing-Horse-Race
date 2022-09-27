# Project Design
**Team Name**: The Amazing Horse Race
**Team Members**:Linh Pham, Jeysi Guillen, Anna Christen

## Sprint Planning
### Prototype I
* Dictionary of horses that a player can choose from(linh)
  * random function for what options are chosen from list(three)
* Function to view horse base stats
* Above done before wednesday if possible
* Raising the horse
* 
  * three options- player can make two choices(two ability points)
  * Speed, strength, stamina, 
* Horse Racing Function:
  * player choice function-Anna
  * Random competitor horses(3) function-Anna
  * function for random chance injuries, effecting stats of all the horses-Linh
  * function that produces winner
    * conditionals based on stats of horses, both competitors and choice
  * print statement

### Prototype II

* print statement outlining instructions
* **Add more horses(figure out how to loop through a database if possible)Anna
* modify stats function(print statements, to make it a game)Anna
* random injuries more complex(what number of points and what stat)Linh
  * add more injuries to affect strength and stamina(chance of recovery after first race)
  * add a fatal injury!!
  * 
* **make basic graphics(after HW eight)Linh
* ** more opponents 
* add multiple race functionality

### Prototype III
_Note: We recommend completing your project, in its entirety, by Prototype III. Then using the extra time to fix bugs that you find during demo day and incorporate other ideas._
* race winner calculation more complicated(random function that pro\ioritizes a attribute, maybe adds extra points to the total, 10% of the persons's attribute to the total, etc)(very small chance of winning no matter what, 'underdog' chance, opposite of fatal injury)
* other..should basically be done.


## User Personas

*Valerie - 46 years old white woman who lives in suburban Portland, OR. Has one child, age eight.Speaks English and Spanish(high-school level). Single Mother. Works as a school secretary at her son's elementary school, takes him to school at 8:15 AM in the morning, and he waits in the office with her after school until 4:30 PM, when she clocks out and drives them both home. Cooks dinner every night, has pizza on Fridays. She is part of a knitting circle on the weekends and volunteers with the PTA regularly. Can operate a computer but is average with computer skills. Doesn't play video games, doesn't really know what they are. Wants to be president of the PTA, loves children and wants to advocate for more resources for the school. (advocates for education) Curious about video games since her kid plays games, but is wary of them and limits what games he can play.

*Christine - 16 years old, Asian American teenager who goes to highschool on the East Coast. English is not her first language. She loves boba and alcohol. She develops an inferiority complex to her mom, who is ex-pageant queen from New Jersey. She doesn't like video game that much but her crush Kevin does. She can use computer on a very advanced level, as she spends about 12 hours on her Macbook a day and even have her own secret TikTok account. She needs to be good at a video game to impress Kevin. She likes cute things and pink-ish settings.

*Pat - 65 Years old, white guy from Texas, OG horse racing fan, used to be a jockey for brief stint in his early twenties, but couldn't make it in the big leagues. Worked most of his life as a mechanic and volunteers at animal rescues. Doesn't understand computers, or video games that much. Can operate a TV remote. Likes sitting on the porch and drinking beer and/or coffee with Irish cream. Still watches horse racing reruns he has recorded on VCR. Has never won a big bet on Horse racing, but has big dreams. Sets aside a budget each month to bet on horse racing. Often buys lottery tickets from the grocery store. Has two children, who live far away but still call him on his landline. Aged 38 and 42. Has poor eyesight.


## Project Structure 

See current Final Project Structure PDF in /docs.



## Project Rubric

* Features:
- Game displays menu showing title, displays images of three horses under title 'Choose a Horse' when screen is clicked.
- Players are able to pick a horse of their choice from a list of three random horses(from a subset of beginning horses), by typing in their favorite horse's name.
- Players are able to view the respective stats of each of the horses on the random list before choosing their horse.
- Players are not able to view or choose a horse that is not on the random list(list of all horses can be viewed in horsedata2.csv).
- Players can modify the stats of their horses and assign their bonus 10 points total to any attributes they want (Speed, Strength, or Stamina). e.g. 2 Points for Speed, 5 Points for Strength, 3 Points for Stamina. They are prevented from assigning more than ten points total.
- Opponent horses are chosen randomly from our bank of horses, excluding the horse the player has chosen
- There are random chances of getting injured or getting bonus points at the end of the race.
- Each race has a specifc set of possible opponents, culminating in Secretariat.
- If the player has more than 80 points in a stat that is chosen randomly by the game to be prioritized, they get a temporary 20 point bonus to their total.
- Game displays simple horse running animation for each race, the player's horse is marked by a bow
- If the player beats the third race(i.e. secretariat) the game displays a unique victory screen with the player's horse wearing a floral garland
- All inputs have input error loops.
- The game runs in a loop, and will keep continuing unless the user chooses to stop the game.