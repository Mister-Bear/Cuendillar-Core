from evennia import Command
import random

class CmdRollBuild(Command):
    """
    Roll your attributes randomly and save them.
    Usage:
      +rollbuild
    """

    key = "+rollbuild"
    locks = "cmd:all()"

    def func(self):
        caller = self.caller

        if caller.db.has_rolled:
            caller.msg("|rYou have already used +rollbuild. Contact staff if you need a reset.|n")
            return

        # Roll attributes
        rolls = {
            "str": random.randint(1, 5),
            "dex": random.randint(1, 5),
            "sta": random.randint(1, 5),
            "per": random.randint(1, 5),
            "int": random.randint(1, 5),
            "wit": random.randint(1, 5),
            "cha": random.randint(1, 5),
            "man": random.randint(1, 5),
            "com": random.randint(1, 5),
        }

        # Save rolls into the character's db
        for attr, value in rolls.items():
            setattr(caller.db, attr, value)

        # Set marker
        caller.db.has_rolled = True

        # Display the results
        message = "|w=== Character Rolls ===|n\nAttributes:"
        for attr, value in rolls.items():
            message += f"\n  {attr.upper()}: {value}"

        message += "\n\nStarter Skills:\n(Coming Soon!)"
        caller.msg(message)
