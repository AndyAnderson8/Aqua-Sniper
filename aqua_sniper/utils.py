import os
import sys
from typing import Any

import yaml

from aqua_sniper.user import User


def color_print(text: str, overwrite: bool = False) -> None:
    """
    Print text with a color transition.

    :param text: The text to print.
    :param overwrite: If True, overwrite the last line. Defaults to False.
    """
    if overwrite:
        sys.stdout.write("\033[2K\r")

    start_color = (0, 255, 255)
    end_color = (255, 95, 255)
    lines = text.split("\n")

    for line in lines:
        indented_line = "    " + line
        n = len(indented_line)
        for i, char in enumerate(indented_line):
            r = int(start_color[0] + (end_color[0] - start_color[0]) * i / max(n - 1, 1))
            g = int(start_color[1] + (end_color[1] - start_color[1]) * i / max(n - 1, 1))
            b = int(start_color[2] + (end_color[2] - start_color[2]) * i / max(n - 1, 1))
            sys.stdout.write(f"\033[38;2;{r};{g};{b}m{char}\033[0m")
        sys.stdout.flush()
        if not overwrite or line != lines[-1]:
            sys.stdout.write("\n")


def load_authenticated_users() -> list[User]:
    """
    Get user instances for all users.

    :return: A list of all user instances.
    """
    credentials_file = os.path.join(os.getcwd(), "credentials.yaml")
    with open(credentials_file) as file:
        data: dict[str, Any] = yaml.safe_load(file)
        users = [User(**user_data) for user_data in data["users"]]
    return users
