import typing

from BaseClasses import Location

if typing.TYPE_CHECKING:
    from . import TLOZTMCWorld


class LocationData(typing.NamedTuple):
    locCode: int
    name: str
    locBitMask: int


class TLOZTMCLocation(Location):
    game: str = "The Legend of Zelda - The Minish Cap"


# add location data
locationList: typing.List[LocationData] = [
    LocationData(0x0f2f86, "thing", 0x00),
]