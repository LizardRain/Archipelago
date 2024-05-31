import struct
import asyncio

from typing import TYPE_CHECKING

from NetUtils import ClientStatus

import worlds._bizhawk as bizhawk
from worlds._bizhawk.client import BizHawkClient

if TYPE_CHECKING:
    from worlds._bizhawk.context import BizHawkClientContext


print("help me please god")
class TLOZTMCClient(BizHawkClient):
    game = "The Legend of Zelda - The Minish Cap"
    system = "GBA"
    player_name = "testing"
    patch_suffix = ".aptloztmc"
    # todo: yes.

    def __init__(self) -> None:
        super().__init__()

    async def validate_rom(self, ctx: "BizHawkClientContext") -> bool:
        from CommonClient import logger
        try:
            rom_name_bytes = await bizhawk.read(ctx.bizhawk_ctx, [(0xA0, 8, "ROM")])
            rom_name = bytes([byte for byte in rom_name_bytes[0] if byte != 0]).decode("ascii")
            if rom_name != "GBAZELDA":
                return False  # Not a GBAZELDA ROM
        except UnicodeDecodeError:
            return False
        except bizhawk.RequestFailedError:
            return False

        ctx.game = self.game
        ctx.items_handling = 0b001
        ctx.want_slot_data = True
        return True

    async def game_watcher(self, ctx: "BizHawkClientContext") -> None:
        # how do????
        #bizhawk.read()
        if self.player_name != "testing":
            print("how")