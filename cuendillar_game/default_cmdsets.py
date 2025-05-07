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

class CharacterCmdSet(default_cmds.CharacterCmdSet):
    key = "DefaultCharacter"

    def at_cmdset_creation(self):
        super().at_cmdset_creation()
        self.add(CmdCharSheetMain())
        self.add(CmdSkills())
        self.add(CmdLearn())
        self.add(CmdAwardXP())
        self.add(CmdVote())
        self.add(CmdContacts())
        self.add(CmdAddContact())
        self.add(CmdRemoveContact())
        self.add(CmdDescription())

class AccountCmdSet(default_cmds.AccountCmdSet):
    key = "DefaultAccount"
