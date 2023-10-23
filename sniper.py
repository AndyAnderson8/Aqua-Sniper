import math
import time
from utils import *
from user import User

asciiArt = f"""
_______                          ________      _____                     
___    |_____ ____  _______ _    __  ___/_________(_)____________________
__  /| |  __ `/  / / /  __ `/    _____ \__  __ \_  /___  __ \  _ \_  ___/
_  ___ / /_/ // /_/ // /_/ /     ____/ /_  / / /  / __  /_/ /  __/  /    
/_/  |_\__, / \__,_/ \__,_/      /____/ /_/ /_//_/  _  .___/\___//_/     
         /_/                                        /_/                  
Aqua Sniper (v{VERSION}) - BrickPlanet rare sniping tool
"""

def run():
  print(asciiArt)
  while True:
    try:
      print("Checking version...")
      version = checkVersion()
      if version != 3: #update not required
        if version == 1:
          print("Sniper is up-to-date\n")
        else:
          print("Optional update available: https://andylabs.org/bp/Aqua-Sniper/download\n")
        try:
          runCounter = 0
          previousRareID = 0
          waitTime = getWait()
          try:
            print("Loading proxies...")
            proxies = getProxies()
            maxRunCount = min(math.ceil(86400 / (waitTime + .1**8)), 84600)
            if len(proxies) > 0:
              print(f"{len(proxies)} proxies found\n")
            else:
              print("No proxies found, using local network\n")
              proxies = [{}] #no proxies
            while True:
              if runCounter % maxRunCount == 0: #reload users once a day
                if runCounter != 0: 
                  print("Full day elapsed, new user tokens required\n") #only actually required every 7 days, but gets login funds
                try:
                  print("Loading user tokens...\n")
                  users = []
                  userCredentials = getUserCredentials()
                  for userCredential in userCredentials:
                    username, password = userCredential
                    try:
                      print(f"Attempting user \"{username}\" login and authentication...")
                      user = User(username, password)
                      if user.username != None:
                        print("Login successful")
                        if user.authenticated:
                          print("Authentication successful\n")
                          users.append(user)
                        else:
                          print(f"Authentication failed - Please contact the develeloper and provide this hash: {getHash(user.id)}\n")
                      else:
                        print("Login failed, check credentials")
                    except:
                      print("User login or authentication failed, check internet connection and server availability\n")    
                  if len(users) > 0:
                    print(f"{len(users)} users ready for sniping\n")
                  else:
                    print("Unable to start sniper, no users ready")
                    break
                except:
                  print("Unable to load users, config file could not be found or is corrupted")
                  break
              proxy = proxies.pop(0)
              proxies.append(proxy) # add proxy to end for revolving
              runCounter += 1
              print(f"\r    Checking for new rares... ({runCounter})", end="", flush=True)
              try:
                newestRare = getNewestRare(proxy)
                if previousRareID != 0 and previousRareID != newestRare["id"]: #not first iteration or old rare
                  time.sleep(1) #TODO: delay, remove later
                  print(f"New Rare Found!\n\n(ID: {newestRare['id']}) {newestRare['name']} - {newestRare['price']:,} Credits")
                  for user in users:
                    print(f"\nAttempting snipe on user \"{user.username}\"...")
                    if newestRare["price"] <= user.creditBalance:
                      try:
                        if newestRare["price"] >= 0 and user.purchaseItem(newestRare["id"]):
                          print("Snipe successful!\n")
                        else:
                          print("Unable to purchase rare, item is unavailable\n")
                      except:
                        print("Unable to purchase rare, check internet connection and server availability\n")
                    else:
                      print("Unable to purchase rare, Insufficient credits\n")
                previousRareID = newestRare["id"]
                time.sleep(waitTime)
              except:
                print("Unable to check newest rare, check internet connection and server availability")
          except:
            print("Unable to load proxies, config file could not be found or is corrupted")
        except:
          print("Unable to load settings, config file could not be found or is corrupted")
      else:
        print("Update required: https://andylabs.org/bp/Aqua-Sniper/download")
    except:
      print("Unable to check version, check internet connection and server availability")
    print("\nEnter 'r' to restart, or any other character to exit")
    if input().lower() != "r":
      break

run()