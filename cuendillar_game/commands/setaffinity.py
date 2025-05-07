from evennia import Command
from evennia.utils.search import search_object

class CmdSetAffinity(Command):
    """
    +setaffinity <target> <element> <value>

    Set a channeler's elemental affinity.
    Staff-only command.

    Example:
        +setaffinity testchar air 4
    """

    key = "+setaffinity"
    locks = "cmd:perm(Builder)"
    help_category = "Channeling"

    def func(self):
        caller = self.caller
        args = self.args.strip().split()

        if len(args) != 3:
            caller.msg("Usage: +setaffinity <target> <element> <value>")
            return

        target_name, element, value = args
        target = search_object(target_name)

        if not target:
            caller.msg("Target not found.")
            return

        target = target[0]
        try:
            value = int(value)
        except ValueError:
            caller.msg("Affinity value must be a number (0–5).")
            return

        if element.lower() not in ["air", "water", "fire", "earth", "spirit"]:
            caller.msg("Element must be one of: air, water, fire, earth, spirit.")
            return

        if not target.db.affinities:
            target.db.affinities = {}

        target.db.affinities[element.lower()] = value
        caller.msg(f"Set {element.title()} affinity for {target.key} to {value}.")
        target.msg(f"|gYour {element.title()} affinity has been set to {value} by {caller.key}.")
