from dataclasses import dataclass
from typing import Any


@dataclass
class RareItem:
    """
    Store data values for each rare item.

    :ivar item_id: Rare item ID.
    :ivar name: The name of the rare item.
    :ivar value: The credit value of the item.
    """

    item_id: int
    name: str
    value: int

    def __eq__(self, other: Any) -> bool:
        """
        Verify two rare items have same attributes.

        :param other: Other object to compare rare to.
        :return: Whether two items share the same attributes.
        """
        if not isinstance(other, type(self)):
            return False

        for key, value in vars(self).items():
            if vars(other).get(key) != value:
                return False
        return True

    def __str__(self) -> str:
        """
        String representation of the rare and its attributes, formatted.

        :return: Formatted rare item attributes.
        """
        string = f"(ID: {self.item_id}) {self.name}\n"
        if self.value == 0:
            string += "Free"
        elif self.value >= 0:
            string += f"{self.    value:,} Credits"
        else:
            string += "Not for Sale"
        return string
