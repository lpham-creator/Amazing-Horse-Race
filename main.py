 #**Team Name**: The Amazing Horse Race
#**Team Members**: Linh Pham and Anna Christen
#references: https://replit.com/@csc111s22s0304/Homework-Assignment-7-csc111s22s0304-17#distributor.py
import csv
import random
from graphics import*
import unittest

def instructions()-> None:
  """This function prints the instructions for the Amazing Horse Race. Asks player if they'd like to continue to stop viewing the instructions.
 :return: (None) print of instructions
 >>> instructions()
          Each horse has distinct base stats,
          Speed, Stamina and Strength. Before each
          race you will have a chance to split 10
          point across your horse's stats. You 
          will then find out which horse you will
          be competing against! The winning horse
          is the horse who has the highest 
          combined stats. Pay Attention though! 
          There is a special priority bonus you 
          can earn! After the race, the game will 
          choose a stat randomly to prioritize.
          If, for your horse, the chosen stat is 
          greater than 80, your horse will gain an
          additional 20 points! This can make or 
          break a game! You will have two chances 
          to race against different horses before you race             against Secretariat. Choose your base horse 
          wisely and try to get priorities!
"""
  Continue = None
  while Continue != 'DONE':
    instruction = """
          Each horse has distinct base stats,
          Speed, Stamina and Strength. Before each
          race you will have a chance to split 10
          point across your horse's stats. You 
          will then find out which horse you will
          be competing against! The winning horse
          is the horse who has the highest 
          combined stats. Pay Attention though! 
          There is a special priority bonus you 
          can earn! After the race, the game will 
          choose a stat randomly to prioritize.
          If, for your horse, the chosen stat is 
          greater than 80, your horse will gain an
          additional 20 points! This can make or 
          break a game! You will have two chances 
          to race different horses before you race
          Secretariat. Choose your base horse 
          wisely and try to get priorities!"""
    print(instruction)
    Continue = input("Enter DONE to continue:")
def HorseTrack():
         
  """This function draws a window for the horse race with width 600 and height 400, using an image for a background.
  :return:None graphics window"""
  width = 600
  height = 400
  win = GraphWin("HorseTrack", width, height)
  win.setBackground('black')
  
  b = Image(Point(300, 150),"sprites/game title.png")
  c = Image(Point(300, 200),"sprites/game title 2.png")
  Image.draw(b, win)
  Image.draw(c, win)
  
  while win.checkMouse() == None:
          pass


  # d = Image(Point(290,200),"sprites/game title 2.png")
  # Image.draw(d, win)
def ChooseHorse():
  print ("Click on the screen to continue!")
  
  width = 600
  height = 400
  win = GraphWin("HorseTrack", width, height)
  win.setBackground("pink")
  # Image.draw(a, win)

  b = Image(Point(290, 250),"sprites/horse_2.png")
  d = Image(Point(300, 100),"sprites/choose.png")
  e = Image(Point(478, 252), "sprites/horse 4.png")
  g = Image(Point(130, 251), "sprites/horse 5.png")
  
  Image.draw(b, win)
  Image.draw(d, win)
  Image.draw(e, win)
  Image.draw(g, win)
  while win.checkMouse() == None:
          pass

###https://replit.com/@csc111s22s0304/Homework-Assignment-7-csc111s22s0304-17#distributor.py
def readhorsedata()-> list:
  """This function pulls all horse   
stats from the file horsedata2 and returns a list of lists containing this information.
  :return: (List) List of horse information from horsedata.csv
  >>>print(readhorsedata())
  [['1', 'Glory', 'Speed', '86', 'Strength', '102', 'Stamina', '57'], ['2', 'Niike', 'Speed', '96', 'Strength', '102', 'Stamina', '47'], ['3', 'Sparkle', 'Speed', '66', 'Strength', '76', 'Stamina', '110']...(continues)"""
  horselist=[]
  with open('horsedata2.csv') as csv_file:
    csv_reader=csv.reader(csv_file,delimiter=',')
    for row in csv_reader:
      horselist.append(row)#this code is modeled from code written by Prof. Alicia Grubb, in Homework Assignment #7: Neilson Library, in /distributor.py, line 26 function name readDatabase()
  return horselist
###https://replit.com/@csc111s22s0304/Homework-Assignment-7-csc111s22s0304-17#distributor.py 
def horseracelist(racenumber:int)-> list:
  """This function puts together the list of possible  horses that player can pick from, and which possible horses could be the player's opponent, increasing in difficulty as the racenumber increases.
  :param: racenumber: (int) the number indicating which race the player is on
  :return: (List): list of horses based on racenumber
  >>>print(horseracelist(2))
  [['7', 'SeaBiscuit', 'Speed', '100', 'Strength', '70', 'Stamina', '70'], ['8', 'Kelso', 'Speed', '65', 'Strength', '99', 'Stamina', '70'], ['9', 'Count Fleet', 'Speed', '70', 'Strength', '80', 'Stamina', '75'], ['10', 'Black Caviar', 'Speed', '75', 'Strength', '50', 'Stamina', '90'], ['11', 'Eclipse', 'Speed', '90', 'Strength', '60', 'Stamina', '50'], ['12', 'American Pharoah', 'Speed', '80', 'Strength', '80', 'Stamina', '80'], ['13', 'Phar Lap', 'Speed', '55', 'Strength', '89', 'Stamina', '90'], ['14', 'Holy Bull', 'Speed', '30', 'Strength', '105', 'Stamina', '70'], ['15', 'Winx', 'Speed', '85', 'Strength', '75', 'Stamina', '80'], ['16', 'War Admiral', 'Speed', '99', 'Strength', '70', 'Stamina', '65'], ['17', 'Ruffian', 'Speed', '88', 'Strength', '78', 'Stamina', '66'], ['18', 'Zenyatta', 'Speed', '75', 'Strength', '88', 'Stamina', '50']]"""
  horselist=readhorsedata()#original list of horses
  finalhorselist=[]
  if racenumber==1:
    #number indicating race position
    for i in range(0,6):
      finalhorselist.append(horselist[i])
      #appends the first six horses on the list to a new list
  if racenumber==2:
    for i in range(6,18):
      finalhorselist.append(horselist[i])
      #following 12 horses
  if racenumber==3:
     finalhorselist.append(horselist[19])
    #only the final horse
  return finalhorselist
  #returns the horse list based on racenumber
class Horses:
  """This class establishes horse objects"""
  def __init__(horse, name, speed, strength, stamina):
    """method constructs horse object, with attributes name, speed, strength, stamina"""
    horse.name = name
    horse.speed = speed
    horse.strength = strength
    horse.stamina = stamina
    horse.stats = None

  def getName(horse):
    return horse.name

  def getSpeed(horse):
    return horse.speed

  def getStrength(horse):
    return horse.strength

  def getStamina(horse):
    return horse.stamina

class PlayerHorse(Horses):
  """Sets up player horse object"""
  def __init__(horse, name, speed, strength, stamina):
    horse.stats = None
    super().__init__(name,speed,strength,stamina)
    #PlayerHorse class inherits all attributes and methods from horse class
    def getStats(playerhorse):#defines new method
      return playerhorse.stats
 
def setuphorseobjects(racenumber)-> object:
  """This function uses the list of possible horses to create class objects for each horse.
  :param: racenumber: (int) number indicating which race the player is on
  :return: List: list of horse objects
  >>>print(setuphorseobjects(3))
  [<__main__.Horses object at 0x7f9a3e8c4520>]"""
  horselist=horseracelist(racenumber)#horselist based on race number
  horseobjects=[]
  for horse in horselist:
    name= horse[1].lower()#pulls horse attributes from the list
    speed= horse[3]
    strength=horse[5]
    stamina=horse[7]
    name= Horses(horse[1],speed,strength,stamina)#assigns each horse an object under the Horse Class
    horseobjects.append(name)
  return horseobjects 
def horsenames(horselist)->list:
    """This function takes in the list of horse     
    information inputted(from randhorseoptions() ) and returns a list of the horse names. 
  :param: horselist: (list) list of horses based on racenumber
  :return: (List): list of horse names 
  >>>print(horsenames(horselist))
    ['Sunny', 'Joy', 'Glory']"""
    horsenames= []
    for horse in horselist:
      horsenames.append(horse.getName())
    return horsenames

def randhorseoptions(racenumber)->list:
  """This function returns a list of three random horse objects from the setuphorseobects function.
  :param: racenumber: (int) number indicating which race the player is on.
  :return: (list) list of horse objects the player can choose from
  >>>print(randhorseoptions(1))
  [<__main__.Horses object at 0x7f53e99e5d90>, <__main__.Horses object at 0x7f54040da430>, <__main__.Horses object at 0x7f53e99e5dc0>]"""
  chosenhorseoptions = []
  horseoptions=setuphorseobjects(racenumber)#horse list based on race number
  for i in range(0,3):
    choice = random.choice(horseoptions)#chooses random horse from available horses
    if i == 0:
      chosenhorseoptions.append(choice)
    else:
      while len(chosenhorseoptions) < 3:#sets list max length to 3
        if choice in chosenhorseoptions:#checks that horse hasn't already been added to list
              choice=random.choice(horseoptions)
        else:
          chosenhorseoptions.append(choice)
  return chosenhorseoptions

def viewStats(horselist):
  """This function allows the player to view the stats of horses given by the randhorseoptions function.
  :param: racenumber: (list) number indicating which race the player is on.
  :return: (None) print list of horse stats depending on input from player
  >>>viewStats(horselist)
  Now you need to choose a horse to race with,       here are your options:
  Glory
  Niike
  Joy
  Would you like to view a horse's stats?(yes/no)yes
  Enter the name of the horse you would like to      view or DONE : Niike
  Niike stats are 96 102 47
  Enter the name of the horse you would like to      view or DONE to stop:DONE"""
  print("Now you need to choose a horse to race with, here are your options:")
  validinput=False
  while validinput == False:#checks for typing errors
    for horse in horselist:
      print(horse.getName())
    statsbool=input("Would you like to view a horse's stats?(yes/no)")
    if statsbool.upper()=='YES':
      validinput=True
      horsechoice=input("Enter the name of the horse you would like to view or DONE :")
      while horsechoice != "DONE":
        for horse in horselist:
          if horsechoice.title() == horse.getName():#looks for horse that player inputted
            print (horse.getName(), "stats are", horse.getSpeed(), horse.getStrength(), horse.getStamina())#prints chosen horse stats
        horsechoice = input("Enter the name of the horse you would like to view or DONE to stop:")
    elif statsbool.upper()=='NO': 
        print ("Let's choose a horse to race with!")
        validinput= True
    else:#error case
      print('Invalid Input, Please try again:')

def changestats(horselist,playerhorse,racenumber):
 """This function allows the player to add up to ten 
  points to any stat.
  :param: horselist:(list) list defined in main, list of horse objects produced by randhorseoptions function
  :param: playerhorse:(object) PlayerHorse object containing the player's horse stats from race one
  :param: racenumber:(int) number indicating which race the player is on
  :return: playerchoice: (dict) dictionary containing the player's stats with attributes changed by the loop.
  >>>changestats(horselist,playerhorse,1)
  Would you like to change your horses stats?yes
  You have 10 points left to distribute.
  Which stat would you like to change?speed
  How many points would you like to add to Speed?5
  You have 5 points left to distribute.
  Which stat would you like to change?Strength
  How many points would you like to add to           Strength?5"""
 incorrectstat=True
 firstinput=True
 toomanypoints=False
 while firstinput==True:#error case for first input(changebool)
   if racenumber==1:#if it's the first race, takes the dictionary directly outputted by the playerchoice function
     playerchoice = PlayerChoice(horselist,racenumber)
   else:#otherwise, takes the updated playerchoice stats from the playerchoice class
     playerchoice={}
     playerchoice['Name']=playerhorse.getName()
     playerchoice['Speed']=playerhorse.getSpeed()
     playerchoice['Strength']=playerhorse.getStrength()
     playerchoice['Stamina']=playerhorse.getStamina()#assigns stats to a dictionary
   currentnumber='10'#total points to distribute
   changebool = input('Would you like to change your horses stats?')
   if changebool.lower()=='yes':
     while int(currentnumber) > 0:#makes sure the player doesn't enter more than 10 points total
       firstinput=False
       incorrectstat=True
       toomanypoints=False
       print('You have',currentnumber, 'points left to distribute.')
       statchoice = input('Which stat would you like to change?')
       while incorrectstat==True:#error case for stat name
         if statchoice.lower() == 'speed' or  statchoice.lower()=='strength' or statchoice.lower()== 'stamina':
           incorrectstat=False
         else:
           print('Oops! Try typing that again!')
           statchoice = input('Which stat would you like to change?')
         while toomanypoints==False:#error case for entering too many points
           numberchoice = input('How many points would you like to add to'+' '+statchoice.title()+'?')
           nextnumber = int(currentnumber)-int(numberchoice)
           if nextnumber < 0:#checks if the amount of points the player entered is more than the amount they have left
             print('You don\'t have that many points! Please try again!')
             print('You have',currentnumber, 'points left to distribute.')
           else:
             toomanypoints = True   
       for att in playerchoice:
          if att == statchoice.title():
            newstat = int(playerchoice[att])+int(numberchoice)#replaces entry in player choice dictionary with new points added
            playerchoice[att]= newstat
            currentnumber = int(currentnumber)-int(numberchoice)#adjusts current point toal
   elif changebool.lower()=='no':
      firstinput=False
      return playerchoice
   else:
     print('Oops, try typing that again!')
 return playerchoice#returns updated dictionary

def PlayerChoice(randhorse, racenumber):
  """This function creates a dictionary containing the stats for the player's chosen horse.
  :param: randhorse: (list) list of horse objects produced by randhorseoptions function
  :param: racenumber: (int) number indicating which race the player is on
  :return: horse_att: (list) a list containing the stats of the player's chosen horse, with keys titled name, speed, strength, and stamina
  >>>print(PlayerChoice(randhorse,1))
  Which's your favourite horse?Honey
  Your horse of choice is Honey!
  {'Name': 'Honey', 'Speed': '74', 'Strength': '107', 'Stamina': '75'}
  """
  randhorselist=[]
  randhorselistobject= randhorse#randhorse options object list
  for randhorse in randhorselistobject:
    randhorselist.append(randhorse.getName())#appends names of random horse options
  horselist = setuphorseobjects(racenumber)
  choice = input("Which's your favourite horse?")
  correct = True
  while correct == True:
   for horse in horselist:
    if choice in randhorselist:#checks if the player's choice horse is in the list of random options presented
      if horse.getName()==choice:
        horse_att = {}
        horse_att['Name'] = horse.getName()
        horse_att['Speed'] = horse.getSpeed()
        horse_att['Strength'] = horse.getStrength()
        horse_att['Stamina'] = horse.getStamina()
        correct = False
    else:
      print ("Oops, try that again!")
      choice = input("Which's your favourite horse?")
  print ("Your horse of choice is", horse_att['Name'] + "!")
  return horse_att
  print ("Let's Race!")
def OpponentHorse(horse_att:dict,racenumber)->object:
  """This function creates a dictionary containing the stats of the random opponent horse.
  :param: horse_att: (dict) the current attributes of the player's horse produced by the changestats function
  :param: racenumber: (int) number indicating which race the player is on
  :return: (object) random horse object chosen from the setuphorseobjects function, excluding the horse already chosen by the player
  >>>print(OpponentHorse(horse_att,1))
  You're racing against Sparkle.
<__main__.Horses object at 0x7f7d5628b1c0>"""
  horselist = setuphorseobjects(racenumber) #this calls back to the list of horses for players
  my_horse = horse_att
  for horse in horselist:
    opponent_horse = random.choice(horselist) #randomly chooses an opponent horse for the player from the list
    if opponent_horse.getName() != my_horse['Name']:
      print ("You're racing against", opponent_horse.getName()+".")
      return opponent_horse
    else:
      pass

def HorseRun():
  """This function sets up the graphics for the horse objects."""
  width = 600
  height = 400
  win = GraphWin("HorseTrack", width, height)
  b = Image(Point(300, 200),"sprites/grasss.png")
  Image.draw(b, win)

  img1 = Image(Point(100, 200), "sprites/horse_2.png")
  horse1 = Image.draw(img1, win)
  dx = 2
  dy = 0
  img2 = Image(Point(150, 300), "sprites/horsetwo.png")
  horse2 = Image.draw(img2, win)

  c = Image(Point(530, 430),"sprites/finish line.png")
  Image.draw(c, win)

  d = Image(Point(50, 200),"sprites/yourhorsearrow.png")
  Image.draw(d, win)

def randomInjuries(horse_att:dict)->int:
  """This function produces random injuries on the horse's way.
  :param horse_att:(dict) the player's current horse stats from the changestats function
  :return :(int) the new number for the randomly chosen stat with the injury subtracted from it's original value
  >>>print(randomInjuries(horse_att))
  Let's Race!!!
  Your horse is running fine!
  Click on the screen to view the results!
  None
  >>>print(randomInjuries(horse_att))
  Let's Race!!!
  Your Horse has been diagnosed with Grabbed         Quarter!
  Minus ten speed point!
  Click on the screen to view the results!
  85
  """
  print ("Let's Race!!!")
  speed_injuries = ['Bone Chip', "Splint", "Bucked Shins", "Curb", "Grabbed Quarter"]
  stamina_injuries = ["Condylar Fracture", "Hyroma"]
  strength_injuries = ["Osselets", "Windpuffs"]
  num = random.randint(0, 80)
  if num%6 == 0:
    horse_injury = random.choice(speed_injuries) #randomly chooses a speed injury that affects speed point
    print ("Your Horse has been diagnosed with",  horse_injury + "!")
    print ("Minus ten speed point!")
    print ("Click on the screen to view the results!")
    for key in horse_att.items():
      speed = horse_att["Speed"]
      speed2 = int(speed) - 10 #subtracts 10 points from the speed point
      horse_att["Speed"] = speed2
      return speed2
  elif num%3 == 0:
    horse_injury = random.choice(stamina_injuries) #randomly chooses a stamina injury that affects stamina points
    print ("Your Horse has been diagnosed with",  horse_injury + "!")
    print ("Minus ten stamina point!")
    print ("Click on the screen to view the results!")
    for key in horse_att.items():
      stamina = horse_att["Stamina"]
      stamina2 = int(stamina) - 10 #subtracts 10 points from stamina points
      horse_att["Stamina"] = stamina2
      return stamina2
  elif num%5 == 0:
    horse_injury = random.choice(strength_injuries) #randomly chooses a strength injury that affects strength points
    print ("Your Horse has been diagnosed with",  horse_injury + "!")
    print ("Minus ten strength point!")
    print ("Click on the screen to view the results!")
    for key in horse_att.items():
      strength = horse_att["Strength"]
      strength2 = int(strength) - 10 #subtract 10 points from strength points
      horse_att["Strength"] = strength2
      return strength2
  if num == 30:
    print ("!!Fatal Injury!!") #a random fatal injury that subtracts 150 points from the original horse
    print ("Click on the screen to view the results!")
    speed = horse_att["Speed"]
    speed2 = int(speed) - 50
    horse_att["Speed"] = speed2
    stamina = horse_att["Stamina"]
    stamina2 = int(stamina) - 50
    horse_att["Stamina"] = stamina2
    strength = horse_att["Strength"]
    strength2 = int(strength) - 50
    horse_att["Strength"] = strength2
    print ("Minus 150 points!")
  else:
    print ("Your horse is running fine!")
    print ("Click on the screen to view the results!")
   
def calculatePoints(horse_att:dict, opponent_horse:object)->list:
  """This function takes in the stats of both the player horse and the opponent horse and adds up their points.
  :param: horse_att: (dict) current horse attributes for the player's horse based on the changestats function
  :param: opponent_horse: (object) object with the attributes for the opponents horse
  :return: (list) list containing the total points of both players
  >>>print(calculatePoints(horse_att, oppononent_horse)
  Priority Speed!
  Your total points are 265 Honey's total points     are 256
  [265, 256]
  """
  totalpoints=[]
  priority= random.randint(1,4)
  if priority==1:
    if int(horse_att['Speed'])>=80:#checks if stat is over 80
      print('Priority Speed!')
      speed1=int(horse_att["Speed"])+20#adds twenty to that stat temporarily
    else:
      speed1=int(horse_att["Speed"])
  else:
    speed1=int(horse_att["Speed"])
  if priority==2:
    if int(horse_att['Strength'])>=80:
      print('Priority Strength!')
      strength1 = int(horse_att["Strength"])+20
    else:
      strength1 = int(horse_att["Strength"])
  else:
    strength1 = int(horse_att["Strength"])
  if priority==3:
    if int(horse_att['Stamina'])>=80:
      print('Priority Stamina!')
      stamina1 = int(horse_att["Stamina"])+20
    else:
     stamina1 = int(horse_att["Stamina"]) 
  else:
    stamina1 = int(horse_att["Stamina"])
  if priority==4:
    print('No Priority!')
  total_points1 = speed1 + strength1 + stamina1 #calculates the player's horse's total points
  speed2 = int(opponent_horse.getSpeed())
  strength2 = int(opponent_horse.getStrength())
  stamina2 = int(opponent_horse.getStamina())
  total_points2 = speed2 + strength2 + stamina2 #calculates the opponent's horse's total points
  print ("Your total points are", str(total_points1), opponent_horse.getName()+"'s", "total points are", str(total_points2))
  totalpoints.append(total_points1) #add the points to the list
  totalpoints.append(total_points2) #add the points to the list
  return totalpoints

def assignplayerobject(horse_att):
  """This function assigns the player's choice horse attributes to the subclass PlayerHorse to store it over different races.
  :param: horse_att:(dict) dictionary containing the current horse attributes from the player's choice horse from the changestats function
  :return: (object) stats attribute of the PlayerHorse object, containing all of the player's horse's stats
  >>>print(assignplayerobject(horse_att)
  <__main__.PlayerHorse object at 0x7f993d9f3040>
  """
  name = horse_att['Name']
  speed = horse_att['Speed']
  strength = horse_att['Strength']
  stamina = horse_att['Stamina']
  playerhorse=PlayerHorse(name,speed,strength,stamina)
  playerhorse.stats=playerhorse
  return playerhorse.stats 

def HorseRunning(): #this is a graphic screen
  """This function animates the running motion of the horses."""
  width = 600
  height = 400
  win = GraphWin("HorseTrack", width, height)
  b = Image(Point(300, 200),"sprites/grasss.png")
  Image.draw(b, win)
  c = Image(Point(530, 430),"sprites/finish line.png")
  Image.draw(c, win)
  d = Image(Point(300, 90),"sprites/let's race.png")
  Image.draw(d, win)

  img1 = Image(Point(100, 200), "sprites/horse_2.png")
  horse1 = Image.draw(img1, win)
  bow = Image(Point(120, 180), "sprites/bow.png")
  Image.draw(bow, win)
  dx = 1
  dy = 0
  img2 = Image(Point(150, 300), "sprites/horsetwo.png")
  horse2 = Image.draw(img2, win)
  while (win.checkMouse() == None):
    bow.move(dx, dy)
    horse1.move(dx, dy)
    horse2.move(dx, dy)
    
def WhoWins(totalpoints)-> str:
  """This function takes in the calculated points and compares them to determine the winner.
  :param totalpoints:(list) list containing the total points of both horses from the calculatepoints function 
  :return :(str) A print statement to pass to the winscreen function
  >>>print(WhoWins(totalpoints))
  You Lose!
  not you
  """
  if totalpoints[0]>totalpoints[1]: #compare the opponent's horse's points and the player's horse's points
    print('You Win!')
    return 'you'
  elif totalpoints[0]<totalpoints[1]:
    print('You Lose!')
    return 'not you'
  else:
    print('It\'s a Draw!')
    return 'noone'

def WinScreen(racenumber,totalpoints):
 """This function draws a specific screen depending on the result of the race, given by the WhoWins function.
  :param: racenumber: (int) number indicating which race the player is on
  :param: totalpoints:(list) list containing the total points of both horses, given by the calculatepoints function.
  "return: (None) graphics screen with a message depending on the result of the WhoWins function
  """ #this is a graphic screen
 whowins=WhoWins(totalpoints)
 if whowins=='you':#win screen
   width = 600
   height = 400
   b=Image(Point(300, 200),"sprites/you win.png")
   win = GraphWin("HorseTrack", width, height)
   win.setBackground('black')
   a = Image(Point(300, 200),"sprites/confetti.png")
   Image.draw(a, win)
   Image.draw(b, win)
   while win.checkMouse() == None:
          pass#shows screen until player clicks
   if racenumber==3:#win screen if you beat secretariat
       horse = Image(Point(320,270),"sprites/horse_2.png")
       wreath = Image(Point(370,260),"sprites/wreathreallysmallsquishedcropped.png")
       win.setBackground('black')
       Image.draw(horse,win)
       Image.draw(wreath,win)
 elif whowins=='not you':#lose screen
    width = 600
    height = 400
    b=Image(Point(300, 200),"sprites/you lose red.png")
    win = GraphWin("HorseTrack", width, height)
    win.setBackground('black')
    Image.draw(b, win)
    while win.checkMouse() == None:
      pass
 elif whowins=='noone':#draw screen
    width = 600
    height = 400
    b=Image(Point(300, 200),"sprites/it's a draw.png")
    win = GraphWin("HorseTrack", width, height)
    win.setBackground('black')
    Image.draw(b, win)
    while win.checkMouse() == None:
      pass
    
def main():
 """This function runs The Amazing Horse Race game. It prompts the player to select whether or not they want to view the instructions. It sets up the race structure, running the code three times and in specific ways depending on the race number. It also prompts the player if they want to play again, and if they don't, quits the program. Returns a prints statement.
  >>>main()
  Welcome to The Amazing Horse Race! You can         choose your own
  horse and race him against other famous horses.
  After two rounds you get to combat Secretariet -
  a legendary racing horse.
  Good luck and have fun!
  Would you like to view the rules?no
  Alright, here we go!
  Time for Race 1!
  Click on the screen to continue!
  Now you need to choose a horse to race with,       here are your options:
  Sparkle
  Niike
  Sunny
  Would you like to view a horse's stats?(yes/no)no
  Let's choose a horse to race with!
  Which's your favourite horse?Sparkle
  Your horse of choice is Sparkle!
  Would you like to change your horses stats?no
  You're racing against Glory.
  Let's Race!!!
  Your Horse has been diagnosed with Windpuffs!
  Minus ten strength point!
  Click on the screen to view the results!
  Your total points are 242 Glory's total points     are 245
  You Lose!
  Time for Race 2!
  Click on the screen to continue!
  (quit program early for sake of length, program runs twice more)
 """
 print ("Welcome to The Amazing Horse Race! You can choose your own"+'\n' + "horse and race him against other famous horses."+'\n'+ "After two rounds you get to combat Secretariet -"+'\n'+"a legendary racing horse."+'\n'+ "Good luck and have fun!")
 rules = str(input("Would you like to view the rules?"))
 if rules.lower()=='yes':
   instructions()#displays instructions
 else:
   print("Alright, here we go!")
 playagain= 'yes'
 while playagain.lower()=='yes':
    for i in range(1,4):#number of races
      racenumber=i
      print('Time for Race'+' '+str(racenumber)+'!')
      print('Click on the screen to continue!')
      if racenumber==1:
        horselist = randhorseoptions(racenumber)
        #sets up current race horse list
        HorseTrack()
        ChooseHorse()
        #screens
        viewStats(horselist)#asks the player if they want to view stats
        playerhorse= None#starts playerhorse object
        horse_att = changestats(horselist,playerhorse,racenumber)#main player dictionary
        opponent_horse = OpponentHorse(horse_att,racenumber)#opponent dictionary
        HorseRun()#start race screen
        randomInjuries(horse_att)#injuries
        HorseRunning()#animation
        totalpoints = calculatePoints(horse_att, opponent_horse)#calculates points
        WinScreen(racenumber,totalpoints)#displays screen depending on result
        playerhorse = assignplayerobject(horse_att)#assigns the current player dictionary to the class to store it
      elif racenumber!=1:
        HorseTrack()
        horse_att = changestats(horselist,playerhorse,racenumber)
        opponent_horse = OpponentHorse(horse_att,racenumber)
        HorseRun()
        randomInjuries(horse_att)
        HorseRunning()
        totalpoints = calculatePoints(horse_att, opponent_horse)
        WinScreen(racenumber,totalpoints)
        playerhorse = assignplayerobject(horse_att)
    playagain = str(input("Would you like to play again(yes/no)?"))#play again?
 if playagain=='no':
   print('Thanks for Playing!')
  
  
  
  

main()
    
  
  
  


# def createHorseDictionary(name, speed, strength, stamina) -> dict:
#   horses_name = {}
#   horses_name['name'] = name
#   horses_name['speed'] = speed
#   horses_name['strength'] = strength
#   horses_name['stamina'] = stamina
#   return horses_name
  

