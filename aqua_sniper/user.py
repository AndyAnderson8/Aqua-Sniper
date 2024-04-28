from bs4 import BeautifulSoup, Tag

from aqua_sniper.items import RareItem
from aqua_sniper.user_session import UserSession


class User:
    """
    BrickPlanet user instances.

    :ivar _session: Session for authenticated user.
    """

    username: str
    _session: UserSession

    def __init__(self, username: str, password: str) -> None:
        """
        Authenticate a user

        :param username: Username for user to be authenticated.
        :param password: Password for user to be authenticated.
        """
        self.username = username
        self._session = UserSession()
        response = self._session.post(
            "https://www.brickplanet.com/login",
            {"username": username, "password": password},
        )

        parser = BeautifulSoup(response.content, "html.parser")
        title_tag = parser.find("title")
        if isinstance(title_tag, Tag):
            title_text = title_tag.get_text()
            if title_text != "Home | BrickPlanet":
                raise ConnectionRefusedError(
                    f"User '{username}' was not authenticated."
                )
        else:
            raise ConnectionError("Unable to find title tag.")

    def get_rares(
        self,
    ) -> list[RareItem]:
        """
        Get list of rare items from BrickPlanet's API.

        :return: List of all rare items.
        """
        response = self._session.get("https://www.brickplanet.com/api/shop/rare-items")
        data = response.json()
        rares = [
            RareItem(item["id"], item["name"], item["value"]) for item in data["data"]
        ]
        return rares

    def buy_item(self, item_id: int, currency_type: int = 1, quantity: int = 1) -> None:
        response = self._session.post(
            f"https://www.brickplanet.com/shop/{item_id}/buy-item",
            {"currency": currency_type, "quantity": quantity},
        )
        if "You own this" not in response.text:
            raise ValueError("Purchase failed!")
