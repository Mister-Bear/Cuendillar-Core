# commands/default_cmdsets.py

from evennia import default_cmds
from evennia.commands.cmdset import CmdSet
from commands.command import CmdQuit  # Import your custom quit command


class CharacterCmdSet(default_cmds.CharacterCmdSet):
    """
    This is the cmdset available to in-game Characters.
    We override it here to insert our custom CmdQuit.
    """
    def at_cmdset_creation(self):
        super().at_cmdset_creation()
        self.add(CmdQuit())  # Add your custom version of the quit command


class AccountCmdSet(default_cmds.AccountCmdSet):
    """
    Commands available on the unpuppeted Account (OOC)
    """
    def at_cmdset_creation(self):
        super().at_cmdset_creation()


class UnloggedinCmdSet(default_cmds.UnloggedinCmdSet):
    """
    Commands available before logging in.
    """
    def at_cmdset_creation(self):
        super().at_cmdset_creation()


class SessionCmdSet(CmdSet):
    """
    Commands available on all sessions, regardless of login state.
    """
    def at_cmdset_creation(self):
        pass
