import typing

import settings
import os
from BaseClasses import Region
from .Client import TLOZTMCClient
from worlds.AutoWorld import World, WebWorld
from .Items import itemList, itemFrequencies, itemTable, TLOZTMCItem
from .Locations import locationList, TLOZTMCLocation
from .Rom import TLOZTMCProcedurePatch, write_tokens
from .Options import TLOZTMCOptions
import pkgutil



class TLOZTMCWebWorld(WebWorld):
    theme = "partyTime"
    bug_report_page = ""
    tutorials = [

    ]

class TLOZTMCSettings(settings.Group):
    class TLOZTMCRomFile(settings.UserFilePath):
        copy_to = "Legend of Zelda, The - The Minish Cap (USA).gba"
        description = "TLOZ TMC ROM File"
        md5s = ["a104896da0047abe8bee2a6e3f4c7290"]

    rom_file: TLOZTMCRomFile = TLOZTMCRomFile(TLOZTMCRomFile.copy_to)
    rom_start: bool = True

class TLOZTMCWorld(World):
    """
    what
    """

    game = "The Legend of Zelda - The Minish Cap"
    web = TLOZTMCWebWorld()
    options_dataclass = TLOZTMCOptions
    options: TLOZTMCOptions
    settings_key = "tloz_tmc_options"
    settings: typing.ClassVar[TLOZTMCSettings]
    item_name_to_id = {name: data.code for name, data in itemTable.items()}
    location_name_to_id = {loc_data.name: loc_data.locCode for loc_data in locationList}

    def create_regions(self):

        ret = Region("First Check", self.player, self.multiworld)
        loc = TLOZTMCLocation(self.player, locationList[0].name, locationList[0].locCode, ret)
        ret.locations.append(loc)
        self.multiworld.regions.append(ret)

        menuRegion = Region("Menu", self.player, self.multiworld)
        menuRegion.connect(ret)
        self.multiworld.regions.append(menuRegion)

        print("pppp")


    def create_items(self) -> TLOZTMCItem:
        # aaaa
        print("aaaa")

        for item in itemList:
            self.multiworld.itempool.append(self.create_item(item.itemName))

    def create_item(self, name: str) -> TLOZTMCItem:
        # aaaa
        print("aaaa")
        item = itemTable[name]
        return TLOZTMCItem(item.itemName, item.classification, item.code, self.player)

    def generate_output(self, output_directory: str) -> None:
        patch = TLOZTMCProcedurePatch(player=self.player, player_name=self.multiworld.player_name[self.player])
        #patch.write_file("basepatch.bsdiff4", pkgutil.get_data(__name__, "data/basepatch.bsdiff4"))
        write_tokens(self, patch)
        rom_path = os.path.join(
            output_directory, f"{self.multiworld.get_out_file_name_base(self.player)}" f"{patch.patch_file_ending}"
        )
        #print(rom_path)
        #patch.write(rom_path)
        out_file_name = self.multiworld.get_out_file_name_base(self.player)
        patch.write(os.path.join(output_directory, f"{out_file_name}{patch.patch_file_ending}"))
print("help")