"""
Here:

https://www.evennia.com/docs/latest/Setup/Settings-Default.html

Remember:

Don't copy more from the default file than you actually intend to
change; this will make sure that you don't overload upstream updates
unnecessarily.

When changing a setting requiring a file system path (like
path/to/actual/file.py), use GAME_DIR and EVENNIA_DIR to reference
your game folder and the Evennia library folders respectively. Python
paths (path.to.module) should be given relative to the game's root
folder (typeclasses.foo) whereas paths within the Evennia library
needs to be given explicitly (evennia.foo).

If you want to share your game dir, including its settings, you can
put secret game- or server-specific settings in secret_settings.py.
"""

# Use the defaults from Evennia unless explicitly overridden
from evennia.settings_default import *

######################################################################
# Evennia base server config
######################################################################

# This is the name of your game. Make it catchy!
SERVERNAME = "Cuendillar: Reforged"

######################################################################
# Settings given in secret_settings.py override those in this file.
######################################################################
try:
    from server.conf.secret_settings import *
except ImportError:
    print("secret_settings.py file not found or failed to import.")

######################################################################
# FULL CMDSET OVERRIDES
######################################################################

# Load your custom command sets (especially to override CmdQuit)
CMDSET_CHARACTER = "commands.default_cmdsets.CharacterCmdSet"
CMDSET_ACCOUNT = "evennia.commands.default.cmdset_account.AccountCmdSet"
CMDSET_SESSION = "evennia.commands.default.cmdset_session.SessionCmdSet"
CMDSET_UNLOGGEDIN = "evennia.commands.default.cmdset_unloggedin.UnloggedinCmdSet"

######################################################################
# CONNECTION / QUIT MESSAGES
######################################################################

from server.conf import connection_screens
QUIT_MESSAGE = connection_screens.QUIT_MESSAGE
