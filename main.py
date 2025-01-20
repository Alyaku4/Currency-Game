#Importing Libraries:
import time, random, pickle, replit
#import cryptography, getch, sys, os, write
from random import randint
from time import sleep
#from rAn import E
#from cryptography.fernet import Fernet
#from getpass import getpass

#Text:
class color:
  END = '\033[0m'#Normal text
  BOLD = '\033[1m'
  GREY = '\033[2m'#Dim
  ITALIC = '\033[3m'
  UNDERLINE = '\033[4m'
  PURPLE = '\033[95m'
  CYAN = '\033[96m'
  DARKCYAN = '\033[36m'
  BLUE = '\033[94m'#true blue
  GREEN = '\033[92m'#Grassy greem :D
  YELLOW = '\033[93m'#Gold
  RED = '\033[91m'
  MAGENTA = '\033[35m'#I-
  WHITE = '\033[47m'#White highlight white text???!!!
  BLACKBUTREALLYWHITE ='\033[30'#??????????? This is like a randomly generated text style

#try:
#saveContent = pickle.dump([], open("saveContent.env", "wb"))
saveContent = pickle.load( open( 'saveContent.env', 'rb'))
#except:
  #print(color.RED + "An error has occured, please try again later" + color.END)
  #break

'''
adminPass = input(color.BOLD + "Password: " + color.END)
if adminPass == '9140427':
  print(saveContent)
elif adminPass == '8402840':
  for x in range(len(saveContent) - 1):
    print("\n" + color.BOLD + "Profile number " + str(x + 1) + color.END)
    try:
      print(saveContent[x])
    except:
      print("Could not load account data.")
else:
  print(color.RED + "Access denied." + color.END)

'''
#Putting write here until I find a better place
def write(message):
  for char in message:
    sys.stdout.write(char)
    sys.stdout.flush()

    if char != "\n":
      time.sleep(0.06)
    else:
      time.sleep(0.1)
  sys.stdout.write("\n")

#Loading Screen:
def lsf(loading):
  print(color.BOLD + "Currency Game [BETA] Vr. 3.7" + color.END)
  print(loading)
  time.sleep(0.5)
  replit.clear()
for x in range(3):
  lsf("Loading.")
  lsf("Loading..")
  lsf("Loading...")

#Save Game Function:
def saveGame():
  find_opensavefile = dict({})
  for x in range(len(saveContent)):
    filenum = saveContent[x]
    try:
      username_ex = filenum[1]
    except:
      var = "n"
    find_opensavefile[username_ex] = x
  try:
    opensavefile = find_opensavefile[str(username)]
  except:
    opensavefile = len(saveContent) + 1
  saveList = [alias, username, password, inventory, wallet_money, bank_money, intelligence, job, pet, stockages, messages, happiness]
  saveContentNew = []
  for x in range(len(saveContent)):
    if x != opensavefile:
      indexnum = len(saveContentNew) + 1
      fc = saveContent[x]
      saveContentNew.insert(indexnum, fc)
  indexnum = len(saveContentNew) + 1
  saveContentNew.insert(indexnum, saveList)
  pickle.dump( saveContentNew, open("saveContent.env", "wb"))

#Getch (Currently not in use)
'''
def getpassgetch(prompt):
  print(prompt, end='', flush=True)
  passwordTest = ''
  numofchar = 0
  testdone = False
  while testdone == False:
    char = getch.getch()
    if char == "\b":
      lenofpass = len(passwordTest)
      passwordTestLastChar = passwordTest[:lenofpass]
      print("\b", end="")
    elif char == "\n":
      testdone = True
    else:
      passwordTest += char
      print('*', end='', flush=True)
      numofchar += 1
  return passwordTest
'''

#Start of setup:
loggedin = pickle.load( open( 'loggedin.env', 'rb'))
if loggedin == 0:

  #MENU:
  print(color.UNDERLINE + color.BOLD + "Select one:" + color.END)
  print("1. Login")
  print("2. Sign Up")
  testDone = False
  while testDone == False:
    main_menu = input(color.BOLD + "Input number here: " + color.END)
    main_menu = main_menu.lower()
    main_menu = main_menu.strip()
    if main_menu == "1" or main_menu == "2" or main_menu == "login" or main_menu == "sign up": testDone = True
    else: print("Please try again.\n")
  replit.clear()

  #Login
  if main_menu == "1" or main_menu == "login":
    user_passdict = {}
    for x in range(len(saveContent)):
      filenum = saveContent[x]
      try:
        username_ex = filenum[1]
        password_ex = filenum[2]
      except:
        var = "No u"
      opensavefile_ex = x
      pass_file_list = [password_ex, opensavefile_ex]
      #user_passdict[username_ex] = pass_file_list
      user_passdict.update( {str(username_ex) : pass_file_list} )

    testdone = False
    while testdone == False:
      print(color.BOLD + "[Login]" + color.END)
      usernameTest1 = input(color.BOLD + "Username: " + color.END)
      if str(usernameTest1) in user_passdict:
        username = usernameTest1
        pass_file_list = user_passdict[str(usernameTest1)]
        password = pass_file_list[0]
        opensavefile = pass_file_list[1]
        testdone = True
      else:
        replit.clear()
        print(color.RED + "Username doesn't match our records, please try again.\n" + color.END)

    replit.clear()
    testdone = False
    while testdone == False:
      print(color.BLUE + "Password is hidden for privacy.\n" + color.END)
      print(color.BOLD + "[Login]" + color.END)
      print(color.BOLD + "Username: " + color.END + str(username))
      passwordTest1 = input(color.BOLD + "Password: " + color.END)
      if passwordTest1 == password:
        replit.clear()
        testdone = True
      else:
        replit.clear()
        print(color.RED + "Password incorrect, please try again.\n" + color.END)
    saveList = saveContent[opensavefile]
    alias = saveList[0]
    inventory = saveList[3]
    wallet_money = saveList[4]
    bank_money = saveList[5]
    intelligence = saveList[6]
    job = saveList[7]
    pet = saveList[8]
    stockages = saveList[9]
    messages = saveList[10]
    happiness = saveList[11]
    print(color.RED + "Successfully logged in!" + color.END)

  #Sign Up
  if main_menu == "2" or main_menu == "sign up":
    usedusernames = []
    for x in range(len(saveContent)):
      filenum = saveContent[x]
      try:
        username_ex = filenum[1]
        indexnum = len(usedusernames) + 1
        usedusernames.insert(indexnum, str(username_ex))
      except:
        var = "No u"
    print(color.BOLD + "[Sign Up]" + color.END)
    alias = input(color.BOLD + "Alias: " + color.END)
    replit.clear()
    testdone = False
    while testdone == False:
      print(color.BOLD + "[Sign Up]" + color.END)
      print(color.BOLD + "Alias: " + color.END + str(alias))
      usernameTest = input(color.BOLD + "Username: " + color.END)
      replit.clear()
      if usernameTest in usedusernames:
        print(color.RED + "That username is already taken. Please try another.\n" + color.END)
      else:
        username = usernameTest
        testdone = True
    testdone = False
    while testdone == False:
      print(color.BOLD + "[Sign Up]" + color.END)
      print(color.BOLD + "Alias: " + color.END + str(alias))
      print(color.BOLD + "Username: " + color.END + str(username))
      passwordTest = input(color.BOLD + "Password: " + color.END)
      replit.clear()
      if passwordTest == username or passwordTest == alias or len(passwordTest) < 8:
        print(color.RED + "Please set a stronger password with more than 8 characters and isn't the same as your username or alias.\n" + color.END)
      else:
        passwordConf = input(color.BOLD + "Confirm Password: " + color.END)
        if passwordConf == passwordTest:
          password = passwordTest
          testdone = True
        else:
          print(color.RED + "Passwords don't match, please try again.\n" + color.END)
    replit.clear()
    print(color.RED + "Enter the command 'help' for for a list of commands to start you off.")
    print("Enjoy!\n" + color.END)
    wallet_money = 100
    bank_money = 0
    transfer_proccess = 0
    intelligence = 0
    job = 0
    inventory = []
    #pet = ["Animal or species", "Pet name", foodBought, hunger, happiness]
    pet = [0, "", 0, 100, 100]
    stockages = 0
    messages = []
    happiness = 100
    saveGame()

else:
  saveList = loggedin
  alias = saveList[0]
  username = saveList[1]
  password = saveList[2]
  inventory = saveList[3]
  wallet_money = saveList[4]
  bank_money = saveList[5]
  intelligence = saveList[6]
  job = saveList[7]
  pet = saveList[8]
  stockages = saveList[9]
  messages = saveList[10]
  happiness = saveList[11]

#ANNOUNCEMENTS:
#print(color.RED + "\n[IMPORTANT!]" + colour.END)

#Game:
gamestate = True
while(gamestate == True):
  cmd = input("> ")
  cmd = cmd.lower()
  cmd = cmd.strip()

  #More announcements:
  if cmd == "announcements" or cmd == "view announcements":
    print(color.BOLD + "\n~~ANNOUNCEMENTS~~" + color.END)
    print(color.UNDERLINE + "Version 3.7:" + color.END)
    print("-AutoSave now available :D")
    print("-No more save slot numbers to deal with!")
    print("-New login feature!")
    print("-Happiness, happiness, happiness.")
    print("-Stockages are now available!")
    print("-Colours have been removed.")


  #Basic Player Actions:
  elif cmd == "log out" or cmd == "logout":
    loggedin = 0
    pickle.dump( loggedin, open('loggedin.env', 'wb'))
    gamestate = False
    replit.clear()
    print(color.RED + "You have logged out." + color.END)

  elif cmd == "clear":
    replit.clear()

  elif cmd == "help":
    print(color.BOLD + color.UNDERLINE + "Here are some commands:" + color.END)
    print("'Work' to go to work")
    print("'Practice' to boost your intelligence")
    print("'Profile' to view your profile")
    print("'My inventory' to view what you own (Your inventory)")
    if stockages == 0:
      print("'Stockages' for information on what they are and for commands for stockages.")
    else:
      print("'Stockages' for commands for stockages.")
    print("'Shop' to go shopping and get resources you need")
    print("'Study' to boost your intelligence")
    print("'Clear' to clear your screen")
    print("'Check Messages' or 'Check ms' to check your messages.")
    print("'Send Message' or 'Send ms' to send a message.")
    print("'Gift' to send another player an item in your inventory")
    print("'Donate' to donate another player money")
    print("'Change Password' to change your password")
    print("'My balance' to see your balance")
    print("'Deposit' or 'dep' to deposit money")
    print("'Withdraw' or 'with' to withdraw money")
    print("'Practice' to boost your intelligence")
    print("'Friend Profile' to view your friend's profile")
    print("'Announcements' to view them again")

  elif cmd == "delete account" or cmd == "delete acc":
    print(color.BOLD + "Please re-enter your password.")
    passwordTest = input("Password" + color.END)
    if passwordTest == password:
      print(color.BOLD + "Are you sure you would like to delete your account? This action cannot be undone." + color.END)
      print("1. Yes")
      print("2. No")
      testdone = False
      while Testdone == False:
        var = input(color.BOLD + "Input number here: " + color.END)
        if var == "1":
          find_opensavefile = dict({})
          for x in range(len(saveContent)):
            filenum = saveContent[x]
            try:
              username_ex = filenum[1]
            except:
              var = "No u"
            find_opensavefile[username_ex] = x
          try:
            opensavefile = find_opensavefile[str(username)]
          except:
            opensavefile = len(saveContent) + 1
          saveContentNew = []
          for x in range(len(saveContent)):
            if x != opensavefile:
              indexnum = len(saveContentNew) + 1
              fc = saveContent[x]
              saveContentNew.insert(indexnum, fc)
          pickle.dump( saveContentNew, open("saveContent.env", "wb"))
          loggedin = 0
          pickle.dump( loggedin, open('loggedin.env', 'wb'))
          

  elif cmd == "my inventory":
    print(inventory)

  elif cmd == "inventory":
    inventory_len = len(inventory)
    if inventory_len == 0:
      print("Your inventory is empty.")
    else:
      for x in range(len(messages)):
        print("\n" + str(messages[x]))


  elif cmd == "profile":
    print(color.BOLD + "Username: " + color.END + username)
    print(color.BOLD + "Alias: " + color.END + alias)
    print(color.BOLD + "Intelligence: " + color.END + str(intelligence))
    print(color.BOLD + "Stockages: " + color.END + str(stockages))
    print(color.BOLD + "Happiness: " + color.END + str(happiness))
    if job != 0:
      print(color.BOLD + "Job: " + color.END + str(job))
    if job == 0:
      print(color.BOLD + "Job: " + color.END + "Unemployed")
    total_money = wallet_money + bank_money
    print(color.BOLD + "Total Money: " + color.END + str(total_money))
    if "house" in inventory:
      print(color.BOLD + "Shelter: " + color.END + "House")
    if "teensy closet apartment" in inventory:
      print(color.BOLD + "Shelter: " + color.END + "Teensy Closet Apartment")
    if "small apartment" in inventory:
      print(color.BOLD + "Shelter: " + color.END + "Small Apartment")
    if "large apartment" in inventory:
      print(color.BOLD + "Shelter: " + color.END + "Large Apartment")
    if "uselessly large apartment" in inventory:
      print(color.BOLD + "Shelter: " + color.END + "Uselessly Large Apartment")
    if intelligence >= 10000:
      print(color.BOLD + "Smarts Status: " + color.END + "Definitely smarter than a rock")
    elif intelligence >= 1000:
      print(color.BOLD + "Smarts Status: " + color.END + "Smarter than a rock")
    elif intelligence >= 0:
      print(color.BOLD + "Smarts Status: " + color.END + "Possibly smarter than a rock")
    elif intelligence < 0:
      print(color.BOLD + "Smarts Status: " + color.END + "More dumber than a rock")
    elif intelligence < (0-1000):
      print(color.BOLD + "Smarts Status: " + color.END + "u stpud af")
  
  elif cmd == "change password":
    
    if alias == "Clara":
      if password != "A Turin Turambar turun ambartanen!":
        password = "A Turin Turambar turun ambartanen!"
        print(color.BLUE + "Password changed to", password + color.END)
      else:
        print(color.RED + "Tell Alyssa. She'll change it for you." + color.END)
    else:
      passwordTest = getpass(color.BOLD + "Old Password: " + color.END)
      if passwordTest == password:
        newPasswordTest = getpass(color.BOLD + "New Password: " + color.END)
        if newPasswordTest == username or NewPasswordTest == alias or len(passwordTest) > 8:
          replit.clear()
          print(color.RED + "Please set a stronger password with more than 8 characters.\n" + color.END)
        else:
          passwordConf = getpass(color.BOLD + "Confirm Password: " + color.END)
          if passwordConf == newPasswordTest:
            password = passwordTest
            print(color.RED + "Password changed!" + color.END)
          else:
            print(color.RED + "Passwords don't match, please try again.\n" + color.END)

  elif cmd == "change username":
    usedusernames = []
    for x in range(len(saveContent)):
      filenum = saveContent[x]
      try:
        username_ex = filenum[1]
        indexnum = len(usedusernames) + 1
        usedusernames.insert(indexnum, str(username_ex))
      except:
        var = "No u"
    testdone = False
    while testdone == False:
      passwordTest = getpass(color.BOLD + "Confirm Password: " + color.END)
      if passwordTest == password:
        testdone = False
        while testdone == False:
          print(color.BOLD + "[Change Username]" + color.END)
          usernameTest = input(color.BOLD + "Username: " + color.END)
          replit.clear()
          if usernameTest in usedusernames:
            print(color.RED + "That username is already taken. Please try another.\n" + color.END)
          else:
            username = usernameTest
            testdone = True
      else:
        print(color.RED + "That username is already taken. Please try another.\n" + color.END)

  #STOCKAGES!!
  elif cmd == "stockages":
    if stockages == 0:
      print(color.RED + "\n[Stockages are a way to measure your prestige and how good you are at the game. They cost money, and each time you buy one, the price will go up. When you reach milestones of stockages (100, 1000, etc) you will be given rewards, such as items or even access to more of the game!]\n" + color.END)
    print(color.BOLD + "Actions:" + color.END)
    print("-'Purchase stockage' or 'Buy stockage' to purchase a stockage.")
    print("-'Hoard stockages' to buy multiple stockages at once!")
    print("-More commands coming in the near future!")

  elif cmd == "purchase stockage" or cmd == "buy stockage":
    stockage_price = 50 + stockages * 10
    if stockages == 0:
      print(color.BOLD + "Your first stockage will cost $" + str(stockage_price) + "." + color.END)
    else:
      print(color.BOLD + "Your next stockage will cost $" + str(stockage_price) + "." + color.END)
    if wallet_money < stockage_price:
      money_short = stockage_price - wallet_money
      print(color.RED + "You are currently $" + str(money_short) + " short." + color.END)
    else:
      money_left = wallet_money - stockage_price
      print(color.RED + "You will have $" + str(money_left) + " left after this purchase.\n" + color.END)
      print(color.BOLD + "Would you like to continue?" + color.END)
      print("1. Yes")
      print("2. No")
      testdone = False
      while testdone == False:
        var = input(color.BOLD + "Input number here: " + color.END)
        if var == "1":
          wallet_money -= stockage_price
          stockages += 1
          print(color.RED + "You bought a stockage!" + color.END)
          testdone = True
        elif var == "2":
          testdone = True
        else:
          print(color.RED + "Please try again.\n" + color.END)

  elif cmd == "hoard stockages":
    testdone = False
    while testdone == False:
      try:
        stockage_num = int(input(color.BOLD + "Number of stockages to buy: " + color.END))
        testdone = True
      except:
        print(color.RED + "Please try again.\n" + color.END)
    stockage_price = 0
    y = stockages
    for x in range(stockage_num):
      stockage_temp = 50 + y * 10
      stockage_price += stockage_temp
    print(color.BOLD + "That will cost $" + str(stockage_price) + "." + color.END)
    if wallet_money < stockage_price:
      money_short = stockage_price - wallet_money
      print(color.RED + "You are $" + str(money_short) + " short." + color.END)
    else:
      money_left = wallet_money - stockage_price
      print(color.RED + "You will have $" + str(money_left) + " left after this purchase.\n" + color.END)
      print(color.BOLD + "Would you like to continue?" + color.END)
      print("1. Yes")
      print("2. No")
      testdone = False
      while testdone == False:
        var = input(color.BOLD + "Input number here: " + color.END)
        if var == "1":
          wallet_money -= stockage_price
          stockages += stockage_num
          print(color.RED + "You bought " + str(stockage_num) + " stockages!" + color.END)
          testdone = True
        elif var == "2":
          testdone = True
        else:
          print(color.RED + "Please try again.\n" + color.END)

  elif cmd == "pet store" or cmd == "cgps":
    print("i never finished programming this function")
  

  elif cmd == "buy drugs":
    #if username == "DogeyDoge_":
    no = input("This will cost you. Are you sure you want to proceed? If so, press one. ")
    if no == "1":
      wallet_money -= 500
      indexnum = len(inventory) + 1
      inventory.insert(indexnum, "drugs")
      print("Use command:")
      print("take drugs")
    else:
      print("Good choice.")  

  elif cmd == "take drugs":
    if "drugs" in inventory:
      drugchance = randint(1, 3)
      print(color.GREEN + "THERE ARE FLYING" + color.END + color.CYAN + "COLOURS WOOOOOO" + color.END)
      print(color.BLUE + "I DON'T KNOW WHAT" + color.END + color.PURPLE + " YOU DID BUT I THINK IT'S WORKING" + color.END)
      inventory.remove("drugs")
      if drugchance == "1":
        wallet_money -= 100
        print(color.RED + "You fell asleep after you " + color.END)
      elif drugchance == "2" and wallet_money <= 100:
        wallet_money -= 100
        print(color.RED + "You wasted 100 while you were under the effects of the drugs. Don't you think that was stupid?" + color.END)
    else:
      print("Maybe waste some money buying them first??")
  
  elif cmd == "buy stele":
    wallet_money -= 10
    indexnum = len(inventory) + 1
    inventory.insert(indexnum, "stele")
    print("Here in CG, the pronunciation of stele is steel-(long e)")
    print("It's not steel, it's not stehlay, it's not stehlee, it's not steeleh,")
    print("and it")
    print(color.ITALIC + "CERTAINLY" + color.END)
    print("isn't")
    print(color.BOLD + "stylus." + color.END)

  elif cmd == "use stele":
    if "stele" in inventory:
      print("These runes are available:")
      print("1. Voyance")
      print("2. Farsight")
      print("3. Sure-footedness")
      print("4. Night Vision")
      rune = input("Type the number that you want to apply. ")
      if rune == "1":
        #Add a pickle thing so you can only use Voyance once
        print("You can see the Shadow World now!")
        indexnum = len(inventory) + 1
        inventory.insert(indexnum, "Voyance rune")
        print("Your intelligence and stockages just went up!")
        intelligence += 1000
        stockages += 5
        wallet_money -= 10
        inventory.remove("stele")

      if rune == "2":
        print("You will be able to see further and clearer.")
        indexnum = len(inventory) + 1
        inventory.insert(indexnum, "Farsight")
        print("Your intelligence just went up!")
        intelligence += 100
        wallet_money -= 5
        inventory.remove("stele")
      if rune == "3":
        print("Coming soon!")
      if rune == "4":
        print("Coming soon!")
    else:
      print("Buy a stele first!")
      print("(Steles can only be used once before they wear out)")
      print("That will be fixed to better fit the reality of the Shadowhunters universe.")


  elif cmd == "farsight":
    if "Farsight rune" in inventory or "Farsight" in inventory:
      print("Coming soon!")
    else:
      print("Apply a Farsight rune first!")

  elif cmd == "sure-footedness":
    if "Sure-footedness rune" in inventory:
      print("Coming soon!")
    else:
      print("Apply a Sure-footedness rune first!")
  
  elif cmd == "night vision":
    if "Night Vision rune" in inventory:
      print("Coming soon!")
    else:
      print("Apply a Night Vision rune first!")

  elif cmd == "work botic 52":
    workBoticList = pickle.load( open( 'workbotic.env', 'rb'))
    if username in workBoticList:
      print("You've already used that command!")
    else:
      x == 0
      while x < 52:
        print("work")
        time.sleep(0.01)
        print("work")
        time.sleep(0.01)
        x += 2
      print("You have discovered a secret command!")
      wallet_money += 5200
      print("+$5200")
      indexnum = len(workBoticList) + 1
      workBoticList.insert(indexnum, username)
      pickle.dump( workBoticList( 'workbotic.env', 'rb'))

  elif cmd == "quine":
    print("print(\"quine\")")

  elif cmd == ">:)":
    print(color.MAGENTA + "These smiley faces..." + color.END)

  elif cmd == "dumbify":
    if intelligence < 0:
      intelligence = 0 - intelligence
    if intelligence > 0 and alias != "Clara":
      intelligence = 0 - 1000
    if alias == "Clara":
      intelligence -= 100
    else:
      print("We can't handle zero intelligence. Do something.")
    print("You have found a secret command!")

  elif cmd == "dftba":
    print("Dont forget to be awesome! Dandelions fly through blue air! Darling, fetch the battle axe!   >:D")
    wallet_money += 100

  elif cmd == "murder currency game":
    gamestate = False
    replit.clear()
    y = 3
    saveList = []
    if alias != "Alyssa" and alias != "Clara":
      #saveList = [alias, username, password, inventory, wallet_money, bank_money, intelligence, job, pet, stockages, messages, happiness]
      indexnum = len(messages) + 1
      message_send = "From: CurrencyGameLawCourt(CGLC)      Message Content: Due to a recent illegal attempt of breaking the game, your stats have been reset."
      messages.insert(indexnum, message_send)
      saveList = [alias, username, password, [], 0, 0, 0, 0, 0, stockages, messages, 0]
      saveGame()
    for x in range(3):
      print(color.RED + "what did you do to me you little human")
      print("Overwriting account data in " + str(y) + "..." + color.END)
      time.sleep(1)
      replit.clear()
      y -= 1
    print("Wait.. hold on.")
    print("I will give you one more chance to get your account back.")
    atm = randint(0,1)
    print("I am thinking of a integer between 0 and 1 inclusive. Guess it right and I might give you your account back.")
    guess = input(color.BOLD + "Guess: " + color.END)
    guess = guess.lower()
    guess = guess.strip()
    if guess == atm:
      print("You got it right! But nobody cares about you or your precious account, so it gets erased anyways. Have fun!")
    else:
      print("You got it wrong. Goodbye.")
  
  elif cmd == "delete clara's accounts":
    saveContentTest = saveContent
    for x in range(len(saveContentTest) - 1):
      try:
        var = saveContentTest[x]
      except:
        print(color.RED + "An exception has occured." + color.END)
      if var[1] != "Sisofgeng" and var[1] != "LuthienTinuviel" and var[1] != "LeRichDoge" and var[1] != "nickname":
        saveContentTest.pop(x+1)
    for x in range(len(saveContentTest) - 1):
      print("\n" + color.BOLD + "Profile number " + str(x + 1) + color.END)
      try:
        print(saveContentTest[x+1])
      except:
        print("Could not load account data.")

  elif cmd == "print savecontent":
    adminPass = input(color.BOLD + "Password: " + color.END)
    if adminPass == '9140427':
      print(saveContent)
    elif adminPass == '8402840':
      for x in range(len(saveContent) - 1):
        print("\n" + color.BOLD + "Profile number " + str(x + 1) + color.END)
        try:
          print(saveContent[x])
        except:
          print("Could not load account data.")
    else:
      print(color.RED + "Access denied." + color.END)

  elif cmd == "give me free money":
    if alias == "Clara":
      print("Here, have some money!")
      if intelligence <= 1000:
        wallet_money += intelligence
        if intelligence < 0:
          print("Oh, sorry, I guess you should become smarter so you don't lose money when you do this.")
          print("Too late to change anything!")
      else:
        wallet_money += 100
    else:
      print("I wouldn't give you anything, but I'm nice. Here's (square root of negative 1) dollars! :)")
      print("Except not really, because I don't want to handle that math because I'm lazy.")
      print("So, here's a dollar.")
      print("It would be less, but I don't want to check the code to make sure I used float commands. This isn't the main programmer here, by the way. Don't blame her.")
      wallet_money += 1
    print(color.RED + "You discovered a secret command! :)" + color.END)

  #Basic Money Actions:
  elif cmd == "my balance":
    print("Wallet:", wallet_money)
    print("Bank:", bank_money)

  elif cmd == "deposit" or cmd == "dep":
    print("How much money would you like to deposit?")
    transfer_proccess = int(input("$"))
    if transfer_proccess > wallet_money:
      print("You don't have enough money in your wallet to do that.")
    else:
      wallet_money -= transfer_proccess
      bank_money += transfer_proccess
      print("Transaction complete.")

  elif cmd == "with" or cmd == "withdraw":
    print("How much would you like to withdraw?")
    transfer_proccess = int(input("$"))
    if transfer_proccess > bank_money:
      print(color.RED + "You don't have that much money stored in your bank." + color.END)
    elif transfer_proccess < 0:
      print(color.RED + "You don't have that much money stored in your bank." + color.END)
      wallet_money += transfer_proccess

      bank_money -= transfer_proccess
      print("Transaction complete.")


  #Player and player interaction
  elif cmd == "gift":
    user_file = {}
    for x in range(len(saveContent)):
      filenum = saveContent[x]
      try:
        username_ex = filenum[1]
      except:
        var = ""
      friendfilenum = str(x)
      user_file[username_ex] = friendfilenum
    testdone = False
    while testdone == False:
      username_input = input(color.BOLD + "Friend's Username: " + color.END)
      if username_input in user_file:
        friendfilenum = user_file[str(username_input)]
        testdone = True
      else:
        print(color.RED + "Please try again.\n" + color.END)
    friend_fileContent = saveContent[int(friendfilenum)]
    alias_friend = friend_fileContent[0]
    username_friend = friend_fileContent[1]
    password_friend = friend_fileContent[2]
    inventory_friend = friend_fileContent[3]
    wallet_money_friend = friend_fileContent[4]
    bank_money_friend = friend_fileContent[5]
    intelligence_friend = friend_fileContent[6]
    job_friend = friend_fileContent[7]
    pet_friend = friend_fileContent[8]
    stockages_friend = friend_fileContent[9]
    messages_friend = friend_fileContent[10]
    happiness_friend = friend_fileContent[11]


    print("What item would you like to donate?")
    donation_item = input(color.BOLD + "Item: " + color.END)
    donation_item = donation_item.lower()
    donation_item = donation_item.strip()
    if donation_item in inventory:
      indexnum = len(inventory_friend) + 1
      inventory_friend.insert(indexnum, donation_item)
      inventory.remove(donation_item)

      from_ms = "From: System"
      print("\n" + "To: " + alias_friend, "(" + username_friend + ")")
      indexnum = len(messages_friend) + 1
      message_send = from_ms + "      Message Content: " + str(alias) + " (" + str(username) + ")" + "  has sent you a " + str(donation_item) + "!"
      messages_friend.insert(indexnum, message_send)

      find_opensavefile = dict({})
      for x in range(len(saveContent)):
        filenum = saveContent[x]
        try:
          username_ex = filenum[1]
        except:
          var = "No u"
        find_opensavefile[username_ex] = x
      try:
        opensavefile = find_opensavefile[str(username)]
      except:
        opensavefile = len(saveContent) + 1

      saveContentNew = []
      for x in range(len(saveContent)):
        if x != opensavefile and x != friendfilenum:
          filenum = saveContent[x]
          indexnum = len(saveContentNew) + 1
          filecontent = saveContent[x]
          saveContentNew.insert(indexnum, filecontent)
      indexnum = len(saveContentNew) + 1
      saveContentNew.insert(indexnum, save_friend)
      saveList = [alias, username, password, inventory, wallet_money, bank_money, intelligence, job, pet, stockages, messages, happiness]
      indexnum = len(saveContentNew) + 1
      saveContentNew.insert(indexnum, saveList)
      print(color.RED + "Your gift has been delivered along with a message!  C:" + color.END)

    else:
      print("That item isn't in your inventory. Please try again later.")
      save_friend = [alias_friend, username_friend, password_friend, inventory_friend, wallet_money_friend, bank_money_friend, intelligence_friend, job_friend, pet_friend, stockages_friend, messages_friend, happiness_friend]


  elif cmd == "send message" or cmd == "send ms":
    user_file = {}
    for x in range(len(saveContent)):
      filenum = saveContent[x]
      try:
        username_ex = filenum[1]
      except:
        var = ""
      friendfilenum = str(x)
      user_file[username_ex] = friendfilenum
    testdone = False
    while testdone == False:
      username_input = input(color.BOLD + "Friend's Username: " + color.END)
      if username_input in user_file:
        friendfilenum = user_file[str(username_input)]
        testdone = True
      else:
        print(color.RED + "Please try again.\n" + color.END)
    friend_fileContent = saveContent[int(friendfilenum)]
    alias_friend = friend_fileContent[0]
    username_friend = friend_fileContent[1]
    password_friend = friend_fileContent[2]
    inventory_friend = friend_fileContent[3]
    wallet_money_friend = friend_fileContent[4]
    bank_money_friend = friend_fileContent[5]
    intelligence_friend = friend_fileContent[6]
    job_friend = friend_fileContent[7]
    pet_friend = friend_fileContent[8]
    stockages_friend = friend_fileContent[9]
    messages_friend = friend_fileContent[10]
    happiness_friend = friend_fileContent[11]

    if "phone" in inventory:
      from_ms = color.BOLD + "From: " + color.END + str(alias) + " (" + str(username) + ")" 
      print(color.BOLD + "\nTo: " + color.END + str(alias_friend) + " (" + str(username_friend) + ")")
      print(from_ms)
      print(color.BOLD + "Message Content:" + color.END)
      message_content = input()
      indexnum = len(messages_friend) + 1
      message_send = str(from_ms) + color.BOLD + "     Message Content: " + color.END + str(message_content)
      messages_friend.insert(indexnum, message_send)

      find_opensavefile = dict({})
      for x in range(len(saveContent)):
        filenum = saveContent[x]
        try:
          username_ex = filenum[1]
        except:
          var = "No u"
        find_opensavefile[username_ex] = x
      try:
        opensavefile = find_opensavefile[str(username)]
      except:
        opensavefile = len(saveContent) + 1

      save_friend = [alias_friend, username_friend, password_friend, inventory_friend, wallet_money_friend, bank_money_friend, intelligence_friend, job_friend, pet_friend, stockages_friend, messages_friend, happiness_friend]
      saveContentNew = []
      for x in range(len(saveContent)):
        if x != opensavefile and x != friendfilenum:
          filenum = saveContent[x]
          indexnum = len(saveContentNew) + 1
          filecontent = saveContent[x]
          saveContentNew.insert(indexnum, filecontent)
      indexnum = len(saveContentNew) + 1
      saveContentNew.insert(indexnum, save_friend)
      saveList = [alias, username, password, inventory, wallet_money, bank_money, intelligence, job, pet, stockages, messages, happiness]
      indexnum = indexnum + 1
      saveContentNew.insert(indexnum, saveList)
      print(color.RED + "Your message is sent!" + color.END)

    else:
      print(color.RED + "You need to buy a phone from the shop in order to do that!" + color.END)

  elif cmd == "friend profile":
    user_file = {}
    for x in range(len(saveContent)):
      filenum = saveContent[x]
      try:
        username_ex = filenum[1]
      except:
        var = ""
      friendfilenum = str(x)
      user_file[username_ex] = friendfilenum
    testdone = False
    while testdone == False:
      username_input = input(color.BOLD + "Friend's Username: " + color.END)
      if username_input in user_file:
        friendfilenum = user_file[str(username_input)]
        testdone = True
      else:
        print(color.RED + "Please try again.\n" + color.END)
    friend_fileContent = saveContent[int(friendfilenum)]
    alias_friend = friend_fileContent[0]
    username_friend = friend_fileContent[1]
    password_friend = friend_fileContent[2]
    inventory_friend = friend_fileContent[3]
    wallet_money_friend = friend_fileContent[4]
    bank_money_friend = friend_fileContent[5]
    intelligence_friend = friend_fileContent[6]
    job_friend = friend_fileContent[7]
    pet_friend = friend_fileContent[8]
    stockages_friend = friend_fileContent[9]
    messages_friend = friend_fileContent[10]
    happiness_friend = friend_fileContent[11]
    
    print(color.BOLD + "Alias: " + color.END + alias_friend)
    print(color.BOLD + "Intelligence: " + color.END + str(intelligence_friend))
    print(color.BOLD + "Stockages: " + color.END + str(stockages_friend))
    print(color.BOLD + "Happiness: " + color.END + str(happiness_friend))
    if job_friend != 0:
      print(color.BOLD + "Job: " + color.END + str(job_friend))
    if job_friend == 0:
      print(color.BOLD + "Job: " + color.END + "Unemployed")
    total_money_friend = wallet_money_friend + bank_money_friend
    print(color.BOLD + "Total Money: " + color.END + str(total_money_friend))
    if "house" in inventory_friend:
      print(color.BOLD + "Shelter: " + color.END + "House")
    if "teensy closet apartment" in inventory_friend:
      print(color.BOLD + "Shelter: " + color.END + "Teensy Closet Apartment")
    if "small apartment" in inventory_friend:
      print(color.BOLD + "Shelter: " + color.END + "Small Apartment")
    if "large apartment" in inventory_friend:
      print(color.BOLD + "Shelter: " + color.END + "Large Apartment")
    if "uselessly large apartment" in inventory_friend:
      print(color.BOLD + "Shelter: " + color.END + "Uselessly Large Apartment")
    if intelligence_friend >= 10000:
      print(color.BOLD + "Smarts Status: " + color.END + "Definitely smarter than a rock")
    elif intelligence_friend >= 1000:
      print(color.BOLD + "Smarts Status: " + color.END + "Smarter than a rock")
    elif intelligence_friend >= 0:
      print(color.BOLD + "Smarts Status: " + color.END + "Possibly smarter than a rock")
    elif intelligence_friend < 0:
      print(color.BOLD + "Smarts Status: " + color.END + "More dumber than a rock")


  elif cmd == "donate":
    user_file = {}
    for x in range(len(saveContent)):
      filenum = saveContent[x]
      try:
        username_ex = filenum[1]
      except:
        var = ""
      friendfilenum = str(x)
      user_file[username_ex] = friendfilenum
    testdone = False
    while testdone == False:
      username_input = input(color.BOLD + "Friend's Username: " + color.END)
      if username_input in user_file:
        friendfilenum = user_file[str(username_input)]
        testdone = True
      else:
        print(color.RED + "Please try again.\n" + color.END)
    friend_fileContent = saveContent[int(friendfilenum)]
    alias_friend = friend_fileContent[0]
    username_friend = friend_fileContent[1]
    password_friend = friend_fileContent[2]
    inventory_friend = friend_fileContent[3]
    wallet_money_friend = friend_fileContent[4]
    bank_money_friend = friend_fileContent[5]
    intelligence_friend = friend_fileContent[6]
    job_friend = friend_fileContent[7]
    pet_friend = friend_fileContent[8]
    stockages_friend = friend_fileContent[9]
    messages_friend = friend_fileContent[10]
    happiness_friend = friend_fileContent[11]

    print(color.BOLD + "\nHow much would you like to donate?" + color.END)
    donationnegative = True
    while donationnegative == True:
      try:
        donation_amount = int(input("$"))
      except:
        donation_amount = -1
      if donation_amount > 0:
        donationnegative = False
      else:
        print("Please try again.")

    wallet_money_friend += donation_amount
    wallet_money -= donation_amount

    from_ms = color.BOLD + "From: " + color.END + "System"
    indexnum = len(messages_friend) + 1
    message_send = from_ms + color.BOLD + "      Message Content: " + color.END + str(alias) + " (" + str(username) + ")" + "  has sent you $" + str(donation_amount) + "."
    messages_friend.insert(indexnum, message_send)

    find_opensavefile = dict({})
    for x in range(len(saveContent)):
      filenum = saveContent[x]
      try:
        username_ex = filenum[1]
      except:
        var = "No u"
      find_opensavefile[username_ex] = x
    try:
      opensavefile = find_opensavefile[str(username)]
    except:
      opensavefile = len(saveContent) + 1

    save_friend = [alias_friend, username_friend, password_friend, inventory_friend, wallet_money_friend, bank_money_friend, intelligence_friend, job_friend, pet_friend, stockages_friend, messages_friend, happiness_friend]
    saveContentNew = []
    for x in range(len(saveContent)):
      if x != opensavefile and x != friendfilenum:
        filenum = saveContent[x]
        indexnum = len(saveContentNew) + 1
        filecontent = saveContent[x]
        saveContentNew.insert(indexnum, filecontent)
    indexnum = len(saveContentNew) + 1
    saveContentNew.insert(indexnum, save_friend)
    saveList = [alias, username, password, inventory, wallet_money, bank_money, intelligence, job, pet, stockages, messages, happiness]
    indexnum = len(saveContentNew) + 1
    saveContentNew.insert(indexnum, saveList)
    print(color.RED + "Your gift of $" + str(donation_amount) + " has been sent along with a note!" + color.END)

  #Job Actions:
  elif cmd == "work":
    if job != 0:
      if happiness > 0:
        if job == "Janitor":
          working_job = randint(1, 3)
          if working_job == 1:
            wallet_money += 11
            happiness -= 1
            print("You worked for an hour and recieved $11.")
          else:
            print("There is no need for cleaning right now.")
            happiness -= 2
        if job == "Doctor":
          working_job = randint(1, 6)
          job_done_well = False
          def doctorjob(question, answers):
            print(question)
            answer = input("Answer: ")
            answer = answer.lower()
            answer = answer.strip()
            if answer in answers:
              job_done_well = True

          if working_job == 1:
            print("What part of your body is osteoporosis linked to?")
            answer = input("Answer: ")
            answer = answer.lower()
            answer = answer.strip()
            if answer == "bone" or answer == "bones":
              job_done_well = True
          elif working_job == 2:
            print("What part of your body is rhinitis linked to?")
            answer = input("Answer: ")
            answer = answer.lower()
            answer = answer.strip()
            if answer == "nose":
              job_done_well = True
          elif working_job == 3:
            print("What part of your body is amnesia linked to?")
            answer = input("Answer: ")
            answer = answer.lower()
            answer = answer.strip()
            if answer == "brain" or answer == "head":
              job_done_well = True
          elif working_job == 4:
            print("What is the proper medical term for lazy eye?")
            answer = input("Answer: ")
            answer = answer.lower()
            answer = answer.strip()
            if answer == "amblyophia":
              job_done_well = True
          elif working_job == 5:
            print("What stage of sleep is it most rare for sleep walking to occur?")
            answer = input("Answer: ")
            answer = answer.lower()
            answer = answer.strip("cycle")
            answer = answer.strip()
            if answer == "rem" or answer == "r.e.m" or answer == "r. e. m." or answer == "rapid eye movement":
              job_done_well = True
          elif working_job == 6:
            print("What part of your body is appendicitis related to?")
            answer = input("Answer: ")
            answer = answer.lower()
            answer = answer.strip()
            if answer == "appendix":
              job_done_well = True
          elif working_job == 7:
            doctorjob("How many mg of sodium does the average American consume in a day?", ["3400", "3400mg", "3400 mg", "3400 miligrams", "3400 milligrams"])
            

          if job_done_well == True:
            wallet_money += 99
            happiness -= 1
            print("Good work! You have recieved $99.")
          else:
            print("Not quite!")
            happiness -= 2

        if job == "Office Worker":
          working_job = randint(1, 1)
          if working_job == 1:
            print("Around how many pieces of bread can a single lightning bolt toast?")
            print("(For some reason this needs to be answered in your job.)")
            answer = input("Answer: ")
            answer = answer.lower()
            answer = answer.strip()
            if answer == "10000" or answer == "10,000" or answer == "10, 000" or answer == "10 000":
              job_done_well = True
          if job_done_well == True:
            wallet_money += 36
            print("You worked for an hour and recieved $36")
          else:
            print("Not quite!")

        if job == "Philosopher":
          
          question = randint(1,3)
          if question == 1:
            answer = input("Who said 'Cogito, ergo, sum?' ")
            answer = answer.lower()
            answer = answer.strip()
            if answer == "decartes" or answer == "rene decartes" or answer == "r. decartes":
              print("Correct!")
              goodwork = True
            else:
              print("That's incorrect.")
              goodwork = False
          if question == 2:
            print("What is Epistemology?")
            print("1. The study of beauty (e.g. What makes art art?)")
            print("2. The study of Ethics (e.g. What is right or wrong?)")
            print("3. The study of knowledge (e.g. How do we know what we know?")
            answer = input("Choose a number. ")
            answer = answer.lower()
            answer = answer.strip()
            if answer == "3" or answer == "3.":
              print("Correct!")
              goodwork = True
            else:
              print("That's incorrect.")
              goodwork = False
          if question == 3:
            answer = input("Who is largely credited as being the first real scientist/philosopher? ")
            answer = answer.lower()
            answer = answer.strip()
            if answer == "socrates":
              print("Good job!")
              goodwork = True
            elif answer == "aristotle" or answer == "plato":
              print("Not quite... but close!")
              goodwork = False
            else:
              print("Incorrect.")
              goodwork = False
        
          if goodwork == True:
            wallet_money += philog
            philog = pickle.load( open('philog.env', 'rb'))
            if philog <= 25:
              happiness -= 1
            if philog > 25 and philog < 50:
              happiness += 0
            if philog >= 51:
              happiness += 1
              philog += 1
            philog += 1
            pickle.dump( philog, open('philog.env', 'wb'))
          
          if goodwork == False:
            philog -= 1
            pickle.dump( philog, open('philog.env', 'wb'))
            happiness -= 3
            wallet_money -= 10
            print(color.DARKCYAN + "Better study next time!" + color.END)

      else:
        print("Boost your happiness to work again!")
        print(color.ITALIC + "One way to boost your happiness is to buy dumbages from the shop!" + color.END)
        total_money = wallet_money + bank_money
        if total_money < 25:
          gift_amount = 25 - total_money
          wallet_money += gift_amount
    else:
      print("You don't have a job!")
      print("Use 'Job list' to look for a job!")

  elif cmd == "job list":
    print("Here are some jobs you can apply for:")
    print("Janitor")
    print("Doctor")
    print("Office Worker")
    print("Philosopher")
    print("Use command 'Apply for job' to apply!")

  elif cmd == "apply for job":
    if job == 0:
      print("What job would you like to apply for?")
      applyforjob = input()
      applyforjob = applyforjob.lower()
      if applyforjob == "janitor":
        job = "Janitor"
        print("Congradulations! You now work as a janitor with a salary of $11 per hour.")
      if applyforjob == "office worker":
        if intelligence >= 1000:
          job = "Office Worker"
          print("Congradulations! You are now working as an office worker with a salary of $36 dollars per hour.")
        else:
          print("You need an intelligence of 1000 or higher to apply for this job.")
      if applyforjob == "doctor":
        if intelligence >= 7000:
          job = "Doctor"
          print("Congradulations! You are now working as a doctor with a salary of $99 dollars per hour.")
        else:
          print("You need an intelligence of 7000 or higher to apply for this job.")
      if applyforjob == "philosopher":
        if intelligence >= 10000:
          job = "Philosopher"
          print("Congradulations! You are now a philosopher. The more you work, the more you earn per working hour.")
        else:
          print("You need an intelligence of 10000 or higher to become that.")



  elif cmd == "quit job":
    job = 0
    print("You quit your job. Your colleagues are sad to see you go.")

  #Using items:
  elif cmd == "study":
    if "textbook" in inventory:
      inventory.remove("textbook")
      study_points = randint(4, 40)
      print("You studied for a while.")
      intelligence += study_points
      print("You gained", str(study_points), "intelligence points!")
    else:
      print("You need to buy some textbooks from the shop in order to study!")

  elif cmd == "practice" or cmd == "practise":
    print("What instrument would you like to practice?")
    practiceinst = input()
    practiceinst = practiceinst.lower()
    practiceinst = practiceinst.strip()
    practiced = False
    if practiceinst in inventory or practiceinst == "mike" or practiceinst == "mic":
      if practiceinst == "microphone" or practiceinst == "mike" or practiceinst == "mic":
        prac_activity = randint(1,1)
        if prac_activity == 1:
          print("Which aria of the below is from Turandot?")
          print("1. Nessun Dorma")
          print("2. L'amour est un oiseau rebelle (Also known as Habanera)")
          print("3. Queen of the Night")
          print("4. E lucevan le stelle")
          nessundorma = input("Insert a number. ")
          if nessundorma == "1":
            print("Yes, Nessun Dorma is an aria from Turandot. The translation of the title means \"No one is allowed to sleep.\" Turandot is written and composed by Franco Alfano and Giacomo Puccini.")
            correct = True
          if nessundorma == "2":
            print("No, Habanera is from Carmen, the full title means \"Love is a rebellious bird.\" Carmen is written and composed by Georges Bizet.")
            correct = False
          if nessundorma == "3":
            print("No, Queen of the Night is from The Magic Flute by Mozart.")
            correct = False
          if nessundorma == "4":
            print("No, E lucevan le stelle is from Tosca. The name means \"And the stars were shining.\" The opera was composed and written by Giacomo Puccini.")
            correct = False
        if correct == True:
          write("Good job!")
          happiness += 3
          intelgain = randint(8, 32)
          intelligence += intelgain
          write(color.CYAN + "You gained " + str(intelgain) + " intelligence!" + color.END)
        if correct == False:
          write("Not quite!")
          write("Try again soon!")
          happiness -= 1

      else:
        prac_activity = randint(1, 5)
        if prac_activity == 1:
          print("What note is equivalent to Eb?")
          print("(Please do not enter more sharps/flats than necessary)")
          note_test = input("Note: ")
          note_test = note_test.lower()
          note_test = note_test.strip()
          if note_test == "d#" or note_test == "d sharp":
            practiced = True

        if prac_activity == 2:
          print("What note is equivalent to Fb?")
          print("(Please do not enter more sharps/flats than necessary)")
          note_test = input("Note: ")
          note_test = note_test.lower()
          note_test = note_test.strip()
          if note_test == "e":
            practiced = True

        if prac_activity == 3:
          print("Who wrote Fur Elise?")
          note_test = input("Composer: ")
          note_test = note_test.lower()
          note_test = note_test.strip()
          if note_test == "beethoven" or note_test == "ludwig beethoven" or note_test == "ludwig van beethoven":
            practiced = True

        if prac_activity == 4:
          print("Who wrote the Winter Wind Etude?")
          note_test = input("Composer: ")
          note_test = note_test.lower()
          note_test = note_test.strip()
          if note_test == "chopin" or note_test == "frédéric chopin" or note_test == "frederic chopin":
            practiced = True

        if prac_activity == 5:
          print("Who wrote Suite No. 1 in G major for unaccompanied cello, BWV 1007?")
          note_test = input("Composer: ")
          note_test = note_test.lower()
          note_test = note_test.strip()
          if note_test == "johann sebastian bach" or note_test == "js bach" or note_test == "bach" or note_test == "j.s. bach":
            practiced = True

        if practiced == True:
          if practiceinst == "viola":
            intelgain = randint(0, 2)
          elif practiceinst == "ukulele":
            intelgain = randint(3, 6)
          elif practiceinst == "violin":
            intelgain = randint(7, 20)
          elif practiceinst == "flute":
            intelgain = randint(10, 30)
          elif practiceinst == "piano":
            intelgain = randint(10, 40)
          elif practiceinst == "strad":
            intelgain = randint(10000, 100000)
          intelligence += intelgain
          print("You gained " + str(intelgain) + " intelligence!")
          happiness += 3

        else:
          print("\nNot quite!")

    else:
      print("Please check if you own that/an instrument and try again.")


  elif cmd == "eat waffle":
    if "waffle" in inventory:
      inventory.remove("waffle")
      print("You ate a waffle! :D")
      happiness += 1
    else:
      print("You don't have any waffles.")

  elif cmd == "eat waffles":
    print("How many waffles would you like to eat?")
    foodnum = int(input("\n"))
    y = 1
    testgood = True
    try:
      for x in range(foodnum):
        inventory.remove("waffle")
        y += 1
    except:
      for x in range(y):
        indexnum = len(inventory) + 1
        inventory.insert(indexnum, "waffle")
      testgood = False
    if testgood == True:
      print("You ate", str(foodnum), "waffles.")
      happiness += 1 * foodnum
    else:
      print("You don't have that many waffles.")
  
  elif cmd == "eat dumbage":
    if "dumbage" in inventory:
      inventory.remove("dumbage")
      print("You ate a dumbage! :o")
      happiness += 10
      intelligence -= 20
    else:
      print("You don't have any dumbages.")

  elif cmd == "eat dumbages":
    print("How many dumbages would you like to eat?")
    foodnum = int(input("\n"))
    y = 1
    testgood = True
    try:
      for x in range(foodnum):
        inventory.remove("dumbage")
        y += 1
    except:
      for x in range(y):
        indexnum = len(inventory) + 1
        inventory.insert(indexnum, "dumbage")
      testgood = False
    if testgood == True:
      print("You ate", str(foodnum), "dumbages.")
      happiness += 10 * foodnum
      intelligence -= 20 * foodnum
    else:
      print("You don't have that many dumbages.")

  elif cmd == "play":
    if "laptop" in inventory:
      print("You played for a while.")
      intelligence -= 2
      happiness += 3
    else:
      print("You need a laptop to play videogames.")
  
  elif cmd == "magic 8 ball":
    if "magic 8 ball" in inventory:
      input(color.BOLD + "Question: " + color.END)
      magic8ball = ["It is certain.", "It is decidedly so.", "Without a doubt.", "Yes - definitely.", "You may rely on it.", "As I see it, yes.", "Most likely.", "Outlook good.", "Yes.", "Signs point to yes.", "Reply hazy, try again.", "Ask again later.", "Better not tell you now.", "Cannot predict now.", "Concentrate and ask again.", "Don't count on it.", "My reply is no.", "My sources say no.", "Outlook not so good.", "Very doubtful."]
      print(color.ITALIC + random.choice(magic8ball) + color.END)
    else:
      print(color.RED + "Buy a Magic 8 Ball from the shop first!" + color.END)

  elif cmd == "check messages" or cmd == "check ms":
    if len(messages) == 0:
      print(color.RED + "You have no messages." + color.END)
    else:
      for x in range(len(messages) + 1):
        try:
          print("\n" + str(messages[x]))
        except:
          var = "death"


  elif cmd == "clear messages" or cmd == "clear ms":
    messages = []
    print("Messages Cleared!")

  #Shop:
  elif cmd == "shop":
    print("Here are some things you can buy:")
    print("Textbooks                 --> $10/ea")
    print("Waffles                   --> $10/ea")
    print("Dumbages                  --> $25/ea")
    print("Magic 8 Ball              --> $45/ea")
    print("Laptop                    --> $1349/ea")
    print("Phone                     --> $3000/ea")
    print("Apartment                 --> $100,000-350,500/ea")
    print("House                     --> $500,000/ea")
    print("Instrument                --> $5-$16,000,000/ea")
    print("Pets                      --> $5-1000000")
    print("Use command 'buy __' to purchase an item.")

  elif cmd == "buy waffle" or cmd == "purchase waffle":
    if wallet_money >= 10:
      wallet_money -= 10
      indexnum = len(inventory) + 1
      inventory.insert(indexnum, "waffle")
      print("You bought a waffle.")
    else:
      print("You don't have enough money in your wallet to buy that.")

  elif cmd == "buy waffles" or cmd == "purchase waffles":
    print("How many would you like to buy?")
    try:
      shoppingspree = int(input(""))
      if wallet_money >= (shoppingspree * 10):
        wallet_money -= (shoppingspree * 10)
        for x in range(shoppingspree):
          indexnum = len(inventory) + 1
          inventory.insert(indexnum, "waffle")
        print("You bought", str(shoppingspree), "waffles.")
      else:
        print("You don't have enough money in your wallet to buy that.")      
    except:
      print("Please input an integer.")
    if wallet_money >= (shoppingspree * 10):
      wallet_money -= (shoppingspree * 10)
      for x in range(shoppingspree):
        indexnum = len(inventory) + 1
        inventory.insert(indexnum, "waffle")
      print("You bought", str(shoppingspree), "waffles.")
    else:
      print("You don't have enough money in your wallet to buy that.")

  elif cmd == "buy dumbage" or cmd == "purchase dumbage":
    if wallet_money >= 25:
      wallet_money -= 25
      indexnum = len(inventory) + 1
      inventory.insert(indexnum, "dumbage")
      print("You bought a dumbage.")
    else:
      print("You don't have enough money in your wallet to buy that.")

  elif cmd == "buy dumbages" or cmd == "purchase dumbages":
    print("How many would you like to buy?")
    try:
      shoppingspree = int(input(""))
    except:
      print("Please input an integer.")
    if wallet_money >= (shoppingspree * 25):
      wallet_money -= (shoppingspree * 25)
      for x in range(shoppingspree):
        indexnum = len(inventory) + 1
        inventory.insert(indexnum, "dumbage")
      print("You bought", str(shoppingspree), "dumbages.")
    else:
      print("You don't have enough money in your wallet to buy that.")

  elif cmd == "buy magic 8 ball" or cmd == "purchase magic 8 ball":
    if wallet_money >= 45:
      wallet_money -= 45
      indexnum = len(inventory) + 1
      inventory.insert(indexnum, "magic 8 ball")
      print(color.RED + "You bought a Magic 8 Ball. Use the command 'Magic 8 Ball' to use it!" + color.END)
    else:
      print(color.RED + "You don't have enough money in your wallet to buy that." + color.END)

  elif cmd == "buy magic 8 balls" or cmd == "purchase magic 8 balls":
    print("How many would you like to buy?")
    try:
      shoppingspree = int(input(""))
    except:
      print(color.RED + "Please input an integer." + color.END)
    if wallet_money >= (shoppingspree * 10):
      wallet_money -= (shoppingspree * 10)
      for x in range(shoppingspree):
        indexnum = len(inventory) + 1
        inventory.insert(indexnum, "textbook")
      print(color.RED + "You bought", str(shoppingspree), "textbooks." + color.END + colour)
    else:
      print(color.RED + "You don't have enough money in your wallet to buy that." + color.END + colour)

  elif cmd == "buy textbook" or cmd == "purchase textbook":
    if wallet_money >= 10:
      wallet_money -= 10
      indexnum = len(inventory) + 1
      inventory.insert(indexnum, "textbook")
      print("You bought a textbook.")
    else:
      print("You don't have enough money in your wallet to buy that.")

  elif cmd == "buy textbooks" or cmd == "purchase textbooks":
    print("How many would you like to buy?")
    try:
      shoppingspree = int(input(""))
    except:
      print("Please input an integer.")
    if wallet_money >= (shoppingspree * 10):
      wallet_money -= (shoppingspree * 10)
      for x in range(shoppingspree):
        indexnum = len(inventory) + 1
        inventory.insert(indexnum, "textbook")
      print("You bought", str(shoppingspree), "textbooks.")
    else:
      print("You don't have enough money in your wallet to buy that.")

  elif cmd == "buy laptop" or cmd == "purchase laptop":
    if wallet_money >= 4000:
      wallet_money -= 4000
      indexnum = len(inventory) + 1
      inventory.insert(indexnum, "laptop")
      print("You bought a laptop.")
    else:
      print("You don't have enough money in your wallet to buy that.")
  elif cmd == "buy laptops" or cmd == "purchase laptops":
    print("How many would you like to buy?")
    shoppingspree = int(input(""))
    if wallet_money >= (shoppingspree * 4000):
      wallet_money -= (shoppingspree * 4000)
      for x in range(shoppingspree):
        indexnum = len(inventory) + 1
        inventory.insert(indexnum, "laptop")
      print("You bought", str(shoppingspree), "laptops.")
    else:
      print("You don't have enough money in your wallet to buy that.")
  
  elif cmd == "buy phone" or cmd == "purchase phone":
    if wallet_money >= 3000:
      wallet_money -= 3000
      indexnum = len(inventory) + 1
      inventory.insert(indexnum, "phone")
      print("You bought a phone! Message your friends!")
    else:
      print("You don't have enough money in your wallet to buy that.")

  elif cmd == "buy apartment" or cmd == "purchase apartment":
    if "house" or "teensy closet apartment" or "small apartment" or "large apartment" or "uselessly large apartment" in inventory:
      print("You already have somewhere to live. Sell your current shelter to buy a new one.")
    
    else:
      print("Which of the following would you like to buy?")
      print("1) Teensy Closet Apartment     --> $10,000")
      print("2) Small Apartment             --> $40,500")
      print("3) Large Apartment             --> $100,000")
      print("4) Uselessly Large Apartment   --> $350,000")
      apartment_choice = input()

      if apartment_choice == "1":
        if wallet_money >= 10000:
          wallet_money -= 10000
          indexnum = len(inventory) + 1
          inventory.insert(indexnum, "teensy closet apartment")
          print("Congradulations! You bought a Teensy Closet Apartment!")
        else:
          print("You don't have enough money to buy that.")
      elif apartment_choice == "2":
        if wallet_money >= 40500:
          wallet_money -= 40500
          indexnum = len(inventory) + 1
          inventory.insert(indexnum, "small apartment")
          print("Congradulations! You bought a Small Apartment!")
        else:
          print("You don't have enough money to buy that.") 
      elif apartment_choice == "3":
        if wallet_money >= 100000:
          wallet_money -= 100000
          indexnum = len(inventory) + 1
          inventory.insert(indexnum, "large apartment")
          print("Congradulations! You bought a Large Apartment!")
        else:
          print("You don't have enough money to buy that.")  
      elif apartment_choice == "4":
        if wallet_money >= 350500:
          wallet_money -= 350500
          indexnum = len(inventory) + 1
          inventory.insert(indexnum, "uselessly large apartment")
          print("Congradulations! You bought a Uselessly Large Apartment! WIth that money, why don't you just buy a house?")
        else:
          print("You don't have enough money to buy that.")
    
  elif cmd == "buy house" or cmd == "purchase house":
    if "house" or "teensy closet apartment" or "small apartment" or "large apartment" or "uselessly large apartment" in inventory:
      print("You already have somewhere to live. Sell your current shelter to buy a new one.")
    else:
      if wallet_money >= 500000:
        wallet_money -= 500000
        indexnum = len(inventory) + 1
        inventory.insert(indexnum, "house")
        print("Congradulations! You bought a house!")
      else:
        print("You don't have enough money to buy that, you homeless person.")

  elif cmd == "buy instrument":
    print("Which would you like to purchase?")
    print("Viola     --> $5/ea")
    print("Ukulele   --> $500/ea")
    print("Microphone -->$1800/ea")
    print("Violin    --> $2000/ea")
    print("Flute     --> $2000/ea")
    print("Piano     --> $7,000/ea")
    print("Strad     --> $16,000,000/ea")
    instrumentshopping = input("\n")
    instrumentshopping = instrumentshopping.lower()
    if instrumentshopping == "viola":
      if wallet_money >= 5:
        wallet_money -= 5
        indexnum = len(inventory) + 1
        inventory.insert(indexnum, "viola")
        print("Sacrilegious! You bought a viola. Could you not afford a violin though?")
      else:
        print("You don't have enough money to buy that.")
    if instrumentshopping == "ukulele":
      if wallet_money >= 500:
        wallet_money -= 500
        indexnum = len(inventory) + 1
        inventory.insert(indexnum, "ukulele")
        print("You now own a ukulele. Start practicing.")
      else:
        print("You don't have enough money to buy that.")
    if instrumentshopping == "microphone" or instrumentshopping == "mike" or instrumentshopping == "mic":
      if wallet_money >= 1800:
        wallet_money -= 1800
        indexnum = len(inventory) + 1
        inventory.insert(indexnum, "microphone")
        print("Congradulations! You now own a microphone. Start practicing your music trivia!")
        print("When practicing, you can type in \"mic\" or \"mike\" instead of microphone.")
      else:
        print("You don't have enough money to buy that.")
    if instrumentshopping == "violin":
      if wallet_money >= 2000:
        wallet_money -= 2000
        indexnum = len(inventory) + 1
        inventory.insert(indexnum, "violin")
        print("Congradulations! You now own a violin.")
      else:
        print("You don't have enough money to buy that.")
    if instrumentshopping == "flute":
      if wallet_money >= 2000:
        wallet_money -= 2000
        indexnum = len(inventory) + 1
        inventory.insert(indexnum, "flute")
        print("You now own a flute. Start practicing.")
      else:
        print("You don't have enough money to buy that.")
    if instrumentshopping == "piano":
      if wallet_money >= 7000:
        wallet_money -= 7000
        indexnum = len(inventory) + 1
        inventory.insert(indexnum, "piano")
        print("Nice! You have a piano now. Start practicing!")
      else:
        print("You don't have enough money to buy that.")
    if instrumentshopping == "strad":
      if wallet_money >= 16000000:
        wallet_money -= 16000000
        indexnum = len(inventory) + 1
        inventory.insert(indexnum, "strad")
        print("You now own a strad. Start practicing.")
      else:
        print("You don't have enough money to buy that.")


  #Sell

  elif cmd == "sell house":
    if "house" in inventory:
      inventory.remove("house")
      wallet_money += 400000
      print("You sold your house and got $400,000 back. Planning to buy a new one?")
    else:
      print("Check if you even have a house first.")

  elif cmd == "sell apartment":
    if "teensy closet apartment" in inventory:
      inventory.remove("teensy closet apartment")
      wallet_money += 8000
      print("You sold your apartment and got $8000 back.")
    elif "small apartment" in inventory:
      inventory.remove("small apartment")
      wallet_money += 30250
      print("You sold your apartment and got $8000 back.")
    elif "large apartment" in inventory:
      inventory.remove("large apartment")
      wallet_money += 80000
      print("You sold your apartment and got $80,000 back.")
    elif "uselessly large apartment" in inventory:
      inventory.remove("uselessly large apartment")
      wallet_money += 300000
      print("You sold your apartment and got $300,000 back.")
    else:
      print(color.RED + "You don't own an apartment." + color.END + colour)
  
  elif cmd == "fhfhfh" or cmd == "sjkdhfksdjf":
    print("Stop fricken spamming boi")
  elif cmd == "give me money" or cmd == "give money":
    print("You don't get anything you poor human being")

  elif cmd == "doctor":
    if input(color.BOLD + "Password: " + color.END) == "9708":
      job = "Doctor"
      print("with alyakus magical admin powers your job is now a doctor")
    else:
      print("you typed the password wrong, get better")

  elif cmd == "alyakus magic happiness booster cmd":
    happiness += 100
    print("done!")

  #Transition
  print()
  saveGame()
  if cmd != "logout" and cmd != "log out" and cmd != "murder currency game" and cmd != "delete account" and cmd != "delete acc":
    saveList = [alias, username, password, inventory, wallet_money, bank_money, intelligence, job, pet, stockages, messages, happiness]
    pickle.dump( saveList, open( "loggedin.env", "wb"))
  elif cmd == "murder currency game":
    find_opensavefile = dict({})
    for x in range(len(saveContent)):
      filenum = saveContent[x]
      try:
        username_ex = filenum[1]
      except:
        var = "No u"
      find_opensavefile[username_ex] = x
    try:
      opensavefile = find_opensavefile[str(username)]
    except:
      opensavefile = len(saveContent) + 1
    saveList = [alias, username, password, [], 0, 0, 0, 0, 0, 0, [], 0]
    saveContentNew = []
    for x in range(len(saveContent)):
      if x != opensavefile:
        indexnum = len(saveContentNew) + 1
        fc = saveContent[x]
        saveContentNew.insert(indexnum, fc)
    indexnum = len(saveContentNew) + 1
    saveContentNew.insert(indexnum, saveList)
    pickle.dump( saveContentNew, open("saveContent.env", "wb"))
    loggedin = 0
    pickle.dump( loggedin, open('loggedin.env', 'wb'))
