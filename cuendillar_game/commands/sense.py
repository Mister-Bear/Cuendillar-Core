from evennia import Command

class CmdSense(Command):
    """
    +sense <target>

    Allows a channeler to sense if someone nearby can channel.
    Only male channelers can sense male channelers, and female channelers can sense female channelers.
    """
    key = "+sense"
    help_category = "Channeling"

    def func(self):
        caller = self.caller
        args = self.args.strip()

        if not args:
            caller.msg("Usage: +sense <target>")
            return

        if not caller.db.is_channeler:
            caller.msg("You cannot sense the One Power.")
            return

        target = caller.search(args)
        if not target:
            return  # Evennia auto-error

        if not target.db.is_channeler:
            caller.msg(f"{target.key} does not appear to be a channeler.")
            return

        caller_gender = caller.db.channeling_gender
        target_gender = target.db.channeling_gender

        if caller_gender == target_gender:
            strength = target.db.power_strength or 0
            if strength >= 12:
                rating = "incredibly strong"
            elif strength >= 9:
                rating = "very strong"
            elif strength >= 6:
                rating = "moderately strong"
            elif strength >= 3:
                rating = "somewhat weak"
            else:
                rating = "barely able to touch the Source"

            caller.msg(f"You sense that {target.key} can channel and is {rating}.")
        else:
            caller.msg(f"{target.key} is of the opposite gender. You cannot sense their ability to channel.")
