import os, time

health = 100
grapplingHook = False
gun = False

def startGame():
  os.system('clear') # clear the screen for the player
  print("Welcome Agent 862! You are being sent on a super secret mission to retrieve a stolen diamond.")
  print()
  print()
  print("Time is running out!")
  time.sleep(5) # wait 3 seconds before moving on
  building1() # runs to send the player to building #1

def building1():
  global grapplingHook # use the grapplingHook variable from the top
  os.system('clear')
  if grapplingHook:
    print("You are in the first building. Would you like to use the grappling hook and go up the side of the building?")
  else:
    print("You are in the first building. There is a grappling hook on the ground, a nearby elevator, and an underground tunnel. What would you like to do?")
  decision = input(">>").strip().lower()
  if decision.find("grappling hook") > -1:
    print("Picking up the grappling hook.")
    grapplingHook = True
    time.sleep(3)
    building1()
  elif decision.find("elevator") > -1:
    print("You had to run out in the open to get to the elevator and got caught.")
    time.sleep(3)
    endGame()
  elif decision.find("tunnel") > -1:
    print("Oh no. The tunnel fell in and you're trapped!")
    time.sleep(3)
    endGame()
  elif decision.find("yes") > -1:
    print("Using the grappling hook.")
    time.sleep(3)
    rooftop()
  elif decision.find("no") > -1:
    print("You already have the grappling hook so you might as well use it. Try again.")
    time.sleep(3)
    building1()
  else:
    print("Sorry, that command is not found.")
    time.sleep(3)
    building1()

def rooftop():
  global grappling, gun
  os.system('clear')
  print("Welcome to the penthouse! Another agent hid a stash of weapons and gadgets on the roof. Would you like to sneak up there and collect them or continue into the penthouse?")
  decision = input(">>").strip().lower()
  if decision.find("collect") > -1:
    print("You found a gun! Let's go back to the penthouse.")
    gun = True
    time.sleep(3)
    penthouse()
  elif decision.find("penthouse") > -1:
    print("Entering penthouse.")
    time.sleep(3)
    penthouse()
  else:
    print("Sorry, that command is not found.")
    time.sleep(3)
    rooftop()

def penthouse():
  global gun
  os.system('clear')
  if not gun:
    print("You're now in the penthouse. There are two guards blocking the entrance to where the diamond is hidden. You didn't get the gadgets so you'll have to try to sneak by the guards.")
    time.sleep(3)
    print()
    print()
    print("Oh no! The guards caught you and tied you up in an adjoining room.")
    time.sleep(4)
    tiedUp()
  else:
    print("You're now in the penthouse. There are two guards blocking the entrance to where the diamond is hidden. Do you shoot them or try to sneak by?")
    decision = input(">>").strip().lower()
    if decision.find("shoot") > -1:
      print("The guards are out of the way and you can get in the hidden room!")
      time.sleep(3)
      diamond()
    elif decision.find("sneak") > -1:
      print("Oh no! The guards caught you and tied you up in an adjoining room.")
      time.sleep(3)
      tiedUp()
    else:
      print("Sorry, that command is not found.")
      time.sleep(3)
      penthouse()

def diamond():
  global grappling, gun
  os.system('clear')
  print("You can see the diamond! But there are traps hidden throughout the room. Do you want to use an explosive to blow up the traps, use a mirror to look for lasers, or walk straight through?")
  decision = input(">>").strip().lower()
  if decision.find("explosive") > -1:
    print("AHHH! The entire apartment exploded and you died!")
    time.sleep(3)
    endGame()
  elif decision.find("mirror") > -1:
    print("You use the mirror to find all the lasers and avoid them! You made it to the diamond and successfully escaped!")
    time.sleep(3)
    tiedUp()
  elif decision.find("walk") > -1:
    print("That wasn't a good idea... You set off the traps and died!")
    time.sleep(3)
    endGame()
  else:
    print("Sorry, that command is not found.")
    time.sleep(3)
    diamond()

def tiedUp():
  global grappling, gun
  os.system('clear')
  print("You're left alone in the room. Do you break out and attack the guards outside the door or sit and wait?")
  decision = input(">>").strip().lower()
  if decision.find("break") > -1:
    print("You knock out the guards and find the room with the diamond.")
    time.sleep(3)
    diamond()
  elif decision.find("wait") > -1:
    print("Oh no! The guards came back and killed you!")
    time.sleep(3)
    endGame()
  else:
    print("Sorry, that command is not found.")
    time.sleep(3)
    tiedUp()

def endGame():
  os.system("clear")
  print("Ha. You died.")
  pass

startGame()