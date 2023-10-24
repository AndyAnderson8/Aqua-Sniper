from bs4 import BeautifulSoup
import json
import re
from session import Session
from utils import *

class User:
  #Initialization
  def __init__(self, username, password):
    self.session = Session()
    self.id = None
    self.username = None
    self.creditBalance = None
    self.authenticated = False

    #login
    self.session.request("GET", "https://www.brickplanet.com/login") #send initial GET request for first token grab
    response = self.session.request("POST", "https://www.brickplanet.com/login", data=f"username={username}&password={password}")
    parser = BeautifulSoup(response.content, "html.parser")
    title = parser.find("title").get_text()
    if title == "Home | BrickPlanet":
      userID = int(parser.find(href=re.compile("https://www.brickplanet.com/profile/"))["href"].split("/")[4])
      creditBalance = int("".join(re.findall(r'\d', parser.find("a", {"class": "nav-link text-credits"})["title"])))
      self.id = userID
      self.username = username
      self.creditBalance = creditBalance

      #authenticate
      self.authenticated = True #remove this and blockquote to reenable whitelist, but idrc for now 
      """
      hashedID = getHash(userID)
      response = self.session.request("GET", "https://andylabs.org/bp/Aqua-Sniper/whitelist")
      whitelist = response.json()
      whitelistedUserIDs = whitelist["users"]
      if hashedID in whitelistedUserIDs:
        self.authenticated = True
      """

  def getOwnedRares(self): 
    rares = [] #name, serial, backpackid, img (doesnt have ID for some reason)
    i = 1
    while True:
      response = self.session.request("GET", f"https://www.brickplanet.com/trades/inventory/{self.id}?page={i}")
      if "No items found" not in response.text:
        i += 1
        items = BeautifulSoup(response.text, "html.parser").find_all("div", {"class": "col-md-3 col-4 mb-4"})
        for item in items:
          name = item.find(class_="fw-semibold text-sm mb-1").text
          serial = int("".join(re.findall(r'\d', item.find(class_="text-muted mb-1").text))) #removes the pound symbol and commas
          backpackID = int("".join(re.findall(r'\d', item["id"])))
          img = "https://www.brickplanet.com" + item.find(class_="card-thumbnail")["src"]
          rares.append({"name": name, "serial": serial, "backpackID": backpackID, "img": img})
      return rares

  #Interfaces
  def setBodyColor(self, color):
    response = json.loads(self.session.request("POST", f"https://www.brickplanet.com/account/avatar/change-all-body-colors/{color}").text)
    status = response.get("status")
    if status == "ok":
      return True
    return False
    
  def purchaseItem(self, itemID):
    response = self.session.request("POST", f"https://www.brickplanet.com/shop/{itemID}/buy-item", data="currency=1&quantity=1")
    if "Awesome! You own this" in response.text: #assumes you can only own one, i.e. did not own one before
      return True
    return False
    
  def purchaseResaleItem(self, itemID, resellerID):
    response = self.session.request("POST", f"https://www.brickplanet.com/shop/{itemID}/buy-item-reseller", data=f"reseller_id={resellerID}")
    if True: #TODO: to see if sucessful, need to check backpack for same name + serial
      return True 
    return False

  def sendTrade(self, userID, givingItems, requestingItems, givingCredits, requestingCredits):
    requestItems = ",".join(map(str, requestingItems))
    giveItems = ",".join(map(str, givingItems))
    payload = f"giving_list={giveItems}&requesting_list={requestItems}&giving_credits={givingCredits}&requesting_credits={requestingCredits}"
    response = self.session.request("POST", f"https://www.brickplanet.com/trades/process/{userID}", data=payload)
    if "Your trade request has been sent" in response.text:
      return True
    return False

  def acceptTrade(self, tradeID):
    response = self.session.request("POST", f"https://www.brickplanet.com/trades/accept/{tradeID}")
    if "This trade has been accepted" in response.text:
      return True
    return False

  def declineTrade(self,  tradeID):
    response = self.session.request("POST", f"https://www.brickplanet.com/trades/deny/{tradeID}")
    if "This trade has been denied" in response.text:
      return True
    return False