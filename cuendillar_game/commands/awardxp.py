from evennia import Command
from evennia.utils import search

class CmdAwardXP(Command):
    """
    Award XP to a player.

    Usage:
      +awardxp <target> = <amount>

    Example:
      +awardxp Saidin = 10
    """

    key = "+awardxp"
    locks = "cmd:perm(Builders)"

    def parse(self):
        """Split arguments into target and amount."""
        if "=" not in self.args:
            self.target_name = None
            self.amount = None
        else:
            self.target_name, self.amount = [part.strip() for part in self.args.split("=", 1)]

    def func(self):
        """Actually do the awarding."""
        caller = self.caller

        if not self.target_name or not self.amount:
            caller.msg("Usage: +awardxp <target> = <amount>")
            return

        target = search.object_search(self.target_name)
        if not target:
            caller.msg(f"Could not find '{self.target_name}'.")
            return
        target = target[0]  # Take first match

        try:
            amount = int(self.amount)
        except ValueError:
            caller.msg("Amount must be a number.")
            return

        if amount <= 0:
            caller.msg("Amount must be positive.")
            return

        # Give XP
        current_xp = target.db.xp or 0
        target.db.xp = current_xp + amount

        caller.msg(f"You have awarded {amount} XP to {target.key}.")
        target.msg(f"You have been awarded {amount} XP by Staff.")
