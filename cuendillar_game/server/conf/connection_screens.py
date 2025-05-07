# -*- coding: utf-8 -*-
"""
Connection screen

This is the text to show the user when they first connect to the game (before
they log in).

To change the login screen in this module, do one of the following:

- Define a function `connection_screen()`, taking no arguments. This will be
  called first and must return the full string to act as the connection screen.
  This can be used to produce more dynamic screens.
- Alternatively, define a string variable in the outermost scope of this module
  with the connection string that should be displayed. If more than one such
  variable is given, Evennia will pick one of them at random.

The commands available to the user when the connection screen is shown
are defined in evennia.default_cmds.UnloggedinCmdSet. The parsing and display
of the screen is done by the unlogged-in "look" command.
"""

from django.conf import settings
from evennia import utils

CONNECTION_SCREEN = """
|n
                        |C⟣⟣⟣⟣⟣⟣⟣⟣⟣⟣⟣⟣⟣⟣⟣⟣⟣⟣⟣⟣⟣⟣  |wCuendillar: Reforged|C  ⟢⟢⟢⟢⟢⟢⟢⟢⟢⟢⟢⟢⟢⟢⟢⟢⟢⟢⟢⟢⟢⟢

                   |W────────────────────────────────────────────────────────

           |wThe Wheel turns again — but the Pattern is no longer whole.

              This is the Fourth Age. The Tower fractures.  
           The old prophecies unravel. The Seals weaken.

         And yet... new threads emerge. Woven by those bold enough to grasp them.

                   |W────────────────────────────────────────────────────────

           |nTo begin your thread:     |Ccreate <name> <password>
           |nTo rejoin the Pattern:    |Cconnect <name> <password>

           |nStaff watch the winds:    |saidincuendillar@gmail.com

                   |W────────────────────────────────────────────────────────

         |mWhy, Hello There.|n  (Every great coder starts with a spark.)
"""

QUIT_MESSAGE = """
|n
                                |W────────────────────────────────

         |wThe Pattern loosens its grip as your thread slips from the Loom.

        But no thread is ever truly lost — only waiting to be woven again.

                     The Wheel turns, always. Until you return...

                                |W────────────────────────────────

         |mYou have left Cuendillar: Reforged.|n  Be good, or don’t get caught.
"""

