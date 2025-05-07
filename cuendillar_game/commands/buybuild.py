from evennia import Command
from char_gen.buybuild_menu import start_buybuild

class CmdBuyBuild(Command):
    """
    Launch the character creation buy/build menu.

    Usage:
        +buybuild
    """
    key = "+buybuild"
    locks = "cmd:perm(Developer)"  # Adjust as needed
    help_category = "Character"

    def func(self):
        start_buybuild(self.caller)
from evennia import Command
from char_gen.buybuild_menu import start_buybuild

class CmdBuyBuild(Command):
    """
    Launch character builder menu.
    Usage:
        +buybuild
    """
    key = "+buybuild"

    def func(self):
        start_buybuild(self.caller)
