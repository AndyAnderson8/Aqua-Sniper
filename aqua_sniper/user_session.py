import os
from queue import Queue
from typing import Any, ClassVar, Optional

import yaml
from bs4 import BeautifulSoup, Tag
from requests import Response, Session


class UserSession:
    """
    Make requests with user token.

    :ivar _session: The user session with all necessary headers.
    :ivar _token: The user token needed to make POST requests.
    """

    _proxies: ClassVar[Queue] = Queue()
    _session: Session
    _token: str

    def __init__(self) -> None:
        if UserSession._proxies.qsize() == 0:
            self._initialize_proxies()
        self._session = Session()
        self._token = ""
        self.get("https://www.brickplanet.com/login")  # grab token

    @classmethod
    def _initialize_proxies(cls) -> None:
        """Initialize all proxies for making requests."""
        credentials_file = os.path.join(os.getcwd(), "credentials.yaml")
        with open(credentials_file) as file:
            data: dict[str, Any] = yaml.safe_load(file)
        try:
            for proxy in data["proxies"]:
                cls._proxies.put({"https": f"http://{proxy}"})
        except TypeError:
            cls._proxies.put({})

    @classmethod
    def _get_next_proxy(cls) -> dict[str, str]:
        """
        Get next available proxy for a request.

        :return: Proxy formatted as dict (ready for use in request).
        """
        proxy = UserSession._proxies.get()
        UserSession._proxies.put(proxy)
        return proxy

    def _update_headers(self, response: Response) -> None:
        """
        Handle response and headers after making an HTTP request.

        :param response: Response from HTTP request.
        """
        response.raise_for_status()
        xsrf_token = response.cookies.get("XSRF-TOKEN")
        session_token = response.cookies.get("brickplanet_session")
        self._session.headers.update(
            {
                "Content-Type": "application/x-www-form-urlencoded",
                "Cookie": f"brickplanet_session={session_token}; XSRF-TOKEN={xsrf_token}",
            }
        )
        if "https://www.brickplanet.com/api/" not in response.url:
            parser = BeautifulSoup(response.content, "html.parser")
            input_tag = parser.find("input", {"name": "_token"})
            if not isinstance(input_tag, Tag):
                raise TypeError("Input is not a tag.")
            token_value = input_tag.get("value")
            if not isinstance(token_value, str):
                raise TypeError("Token value is not a string.")
            self._token = token_value

    def post(
        self, url: str, payload: Optional[dict[str, Any]] = None, use_proxy: bool = True
    ) -> Response:
        """
        Make a POST request.

        :param url: BrickPlanet URL to make POST request to.
        :param payload: Parameters for payload in POST request.
        :param use_proxy: Whether to use a proxy for request.
        :return: The response from request.
        """
        response = self._session.request(
            "POST",
            url,
            data=f"_token={self._token}",
            params=payload,
            proxies=self._get_next_proxy() if use_proxy else None,
        )
        self._update_headers(response)
        return response

    def get(self, url: str, use_proxy: bool = True) -> Response:
        """
        Make a GET request.

        :param url: BrickPlanet URL to make GET request to.
        :param use_proxy: Whether to use a proxy for request.
        :return: The response from the request.
        """
        response = self._session.request(
            "GET",
            url,
            data=f"_token={self._token}",
            proxies=self._get_next_proxy() if use_proxy else None,
        )
        self._update_headers(response)
        return response
