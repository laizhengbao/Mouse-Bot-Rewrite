from packages.namespace_pack import *
from packages import core
from packages import config_mixin

class TempCog(core.CogBase):
    def __init__(self, bot: Bot) -> None:
        super().__init__(bot)
    
    TempSlashCommandGroup = SlashCommandGroup('temp', **config_mixin.get_setting())

def setup(bot: Bot):
    bot.add_cog(TempCog(bot))