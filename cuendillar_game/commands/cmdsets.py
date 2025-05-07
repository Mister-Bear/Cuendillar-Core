"""
Custom Character CommandSet for Cuendillar: Reforged.
This is where you register all your in-game commands.
"""

from evennia import default_cmds
from commands.sheet_main import CmdCharSheetMain
from commands.skills import CmdSkills
from commands.learn import CmdLearn
from commands.awardxp import CmdAwardXP
from commands.vote import CmdVote
from commands.contacts import CmdContacts
from commands.addcontact import CmdAddContact
from commands.removecontact import CmdRemoveContact
from commands.description import CmdDescription
from commands.channel import CmdWeaves, CmdChannel
from commands.rollbuild import CmdRollBuild
from commands.buybuild import CmdBuyBuild
from commands.sense import CmdSense  
from commands.setaffinity import CmdSetAffinity
from commands.setchanneling import CmdSetStrength, CmdSetControl, CmdSetChannelGender

class CharacterCmdSet(default_cmds.CharacterCmdSet):
    """
    This is the default command set for in-game characters.
    """
    key = "DefaultCharacter"

    def at_cmdset_creation(self):
        super().at_cmdset_creation()

        # Core Commands
        self.add(CmdCharSheetMain())
        self.add(CmdSkills())
        self.add(CmdLearn())
        self.add(CmdAwardXP())
        self.add(CmdVote())
        self.add(CmdContacts())
        self.add(CmdAddContact())
        self.add(CmdRemoveContact())
        self.add(CmdDescription())
        self.add(CmdWeaves())
        self.add(CmdChannel())
        self.add(CmdRollBuild())
        self.add(CmdBuyBuild())
        self.add(CmdSense())  # <- NEW
        self.add(CmdSetAffinity())
        self.add(CmdSetStrength())
        self.add(CmdSetControl())
        self.add(CmdSetChannelGender())

class AccountCmdSet(default_cmds.AccountCmdSet):
    """
    This is the default command set for OOC accounts.
    """
    key = "DefaultAccount"

    def at_cmdset_creation(self):
        super().at_cmdset_creation()
        self.add(CmdRollBuild())  # Optional: Allow build access for OOC users
