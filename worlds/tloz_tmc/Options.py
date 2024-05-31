import typing
from Options import Choice, Toggle, StartInventoryPool, PerGameCommonOptions, Range
from dataclasses import dataclass

if typing.TYPE_CHECKING:
    from . import TLOZTMCWorld

class SilencedEzlo(Toggle):
    """
    Ezlo (the hat) talks a lot. Turn to true if you want him to shut up
    """
    display_name = "Silence Ezlo"

@dataclass
class TLOZTMCOptions(PerGameCommonOptions):
    silence_ezlo: SilencedEzlo