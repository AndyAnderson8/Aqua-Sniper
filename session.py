from bs4 import BeautifulSoup
from requests import Session

class Session(Session):
  def __init__(self):
    self.lastResponse = None
    super().__init__()

  def request(self, method, url, data=None, json=None, **kwargs):
    if method == "POST":
      parser = BeautifulSoup(self.lastResponse.content, "html.parser")
      token = parser.find("input", {"name": "_token"})["value"]
      if data is None:
        data = f"_token={token}"
      else:
        data = data + f"&_token={token}"
    response = super().request(method, url, data=data, json=json, **kwargs)
    xsrfToken = self.cookies.get("XSRF-TOKEN")
    sessionToken = self.cookies.get("brickplanet_session")
    self.headers.update({
      "Content-Type": "application/x-www-form-urlencoded",
      "Cookie": f"brickplanet_session={sessionToken}; XSRF-TOKEN={xsrfToken}"
    })
    if "brickplanet.com" in url: #dont store auth response
      self.lastResponse = response
    return response