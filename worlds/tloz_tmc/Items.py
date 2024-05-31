import typing

from enum import IntEnum, Enum
from BaseClasses import Item, ItemClassification
if typing.TYPE_CHECKING:
    from . import TLOZTMCWorld


class ItemData(typing.NamedTuple):
    code: int
    itemName: str
    classification: ItemClassification
    itemID: int


class TLOZTMCItem(Item):
    game: str = "The Legend of Zelda - The Minish Cap"

BASE_ITEM_ID = 27022001000

# options: filler, progression, useful, trap, skip_balancing, progression_skip_balancing
itemList: typing.List[ItemData] = [
    ItemData(27022001000, "Smith's Sword", ItemClassification.progression, 0x01),

]


# TODO: Get a count of checks; am tired.
itemFrequencies: typing.Dict[str, int] = {
    "Piece of Heart": 44,
    "Heart Container": 5,
    "Bottle": 4,
}

itemTable: typing.Dict[str, ItemData] = {item.itemName: item for item in itemList}
items_by_id: typing.Dict[int, ItemData] = {item.code: item for item in itemList}