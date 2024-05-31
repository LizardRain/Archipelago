from typing import TYPE_CHECKING
from settings import get_settings
from worlds.Files import APProcedurePatch, APTokenMixin, APTokenTypes
from .Items import itemList, itemFrequencies, itemTable, TLOZTMCItem
from .Locations import locationList, TLOZTMCLocation

if TYPE_CHECKING:
    from . import TLOZTMCWorld

class TLOZTMCProcedurePatch(APProcedurePatch, APTokenMixin):
    game = "The Legend of Zelda - The Minish Cap"
    hash = "b4bd50e4131b027c334547b4524e2dbbd4227130"
    patch_file_ending = ".aptloztmc"
    result_file_ending = ".gba"
#         ("apply_bsdiff4", ["basepatch.bsdiff4"]),

    procedure = [

        ("apply_tokens", ["token_data.bin"])
    ]

    @classmethod
    def get_source_data(cls) -> bytes:
        with open(get_settings().tloz_tmc_options.rom_file, "rb") as infile:
            base_rom_bytes = bytes(infile.read())

        return base_rom_bytes

def write_tokens(world: "TLOZTMCWorld", patch: TLOZTMCProcedurePatch) -> None:
    # get that good good intro skip
    patch.write_token(APTokenTypes.WRITE, 0x2002ce4, bytes([0x40]))
    for location in locationList:
        patch.write_token(APTokenTypes.WRITE, location.locCode, bytes([itemList[0].itemID]))
    print("hello")
    patch.write_file("token_data.bin", patch.get_token_binary())

