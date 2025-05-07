from evennia import Command

class CmdDescription(Command):
    """
    View or set your short character description.

    Usage:
      +description
      +description <your short description>

    Examples:
      +description A tall man with piercing blue eyes and a calm demeanor.
    """

    key = "+description"
    locks = "cmd:all()"

    def func(self):
        caller = self.caller

        if not self.args:
            # View current description
            desc = caller.db.description or "No description set."
            caller.msg(f"=== DESCRIPTION ===\n{desc}")
            return

        # Set new description
        caller.db.description = self.args.strip()
        caller.msg("Your description has been updated.")

