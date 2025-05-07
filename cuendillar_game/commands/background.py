from evennia import Command

class CmdBackground(Command):
    """
    View or set your background story.

    Usage:
      +background
      +background <your background story>

    Examples:
      +background Born in the Borderlands, trained by the Tower.

    """

    key = "+background"
    locks = "cmd:all()"

    def func(self):
        caller = self.caller

        if not self.args:
            # View current background
            background = caller.db.background or "No background set."
            caller.msg(f"=== BACKGROUND ===\n{background}")
            return

        # Set new background
        caller.db.background = self.args.strip()
        caller.msg("Your background story has been updated.")
