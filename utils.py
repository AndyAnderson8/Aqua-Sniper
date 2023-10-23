from bs4 import BeautifulSoup
import builtins
import json
import os
import re
import requests
import hashlib

VERSION = "0.1.2"

def print(*args, sep=' ', end='\n', file=None, flush=False): #overrided for color printing
  os.system('')
  if args:
    text = sep.join(str(arg) for arg in args)
    lines = text.split('\n')
    for line_index, line in enumerate(lines):
      n = len(line)
      red_step = 255 / max(n - 1, 1) if n > 1 else 255
      green_step = 255 / max(n - 1, 1) if n > 1 else 255
      string = ""
      for i in range(n):
        red = int(i * red_step)
        green = 255 - int(i * green_step)
        string += f"\033[38;2;{red};{green};255m{line[i]}\033[0m"
      builtins.print(f"    {string}", end='\n' if line_index < len(lines) - 1 else end, file=file, flush=flush)
  else:
    builtins.print(end=end, file=file, flush=flush)

def checkVersion():
  response = requests.request("GET", "https://andylabs.org/bp/Aqua-Sniper/whitelist")
  whitelist = response.json()
  newestVersion = whitelist["version"]
  if newestVersion == VERSION: #newest version
    return 1
  elif newestVersion.rsplit(".", 1)[0] == VERSION.rsplit(".", 1)[0]: #optional update
    return 2
  else:
    return 3

def getHash(string):
  salt = "1xypzyexy8p6rhuii0je3zj87s16ufbt"
  hash = hashlib.sha256()
  hash.update((salt + str(string)).encode('utf-8'))
  hashedID = hash.hexdigest()
  return hashedID

def getProxies():
  proxies = []
  with open("config.json", "r") as file:
    config = json.load(file)
    proxyList = config["proxies"]
    for proxy in proxyList:
      proxies.append({"https": f"http://{proxy}"})
  return proxies

def getUserCredentials():
  userList = []
  userCredentials = []
  with open("config.json", "r") as file:
    config = json.load(file)
    usersCredentials = config["users"]
    for userCredentials in usersCredentials:
      username = userCredentials["username"]
      password = userCredentials["password"]
      userList.append([username, password])
  return userList

def getWait():
  proxies = getProxies()
  if len(proxies) >= 4:
    return 0
  if len(proxies) >= 2:
    return 1
  return 2

def getNewestRare(proxy):
  response = requests.request("GET", "https://www.brickplanet.com/shop/search?featured=0&rare=1&type=0&search=&sort_by=0&page=1", proxies=proxy)
  parser = BeautifulSoup(response.content, "html.parser")
  url = parser.find(class_="d-block position-relative")["href"]
  id = re.findall(r"\d+", url)[0]
  name = parser.find(class_="d-block truncate text-decoration-none fw-semibold text-light mb-1").text.split("\n")[0]
  price = int(parser.find(class_="text-credits")["title"].replace(".00 Credits", "").replace(",", "").replace("No Sellers", "-1"))
  img = parser.find(class_="card-thumbnail")["src"]
  item = {"id": id, "name": name, "price": price, "img": img}
  return item