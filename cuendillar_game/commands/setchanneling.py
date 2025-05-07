from evennia import Command

# ----------------------------------
# Set One Power Strength
# ----------------------------------

class CmdSetStrength(Command):
    """
    +setstrength <target> = <value>
    Set a character's One Power strength (1–15).
    """
    key = "+setstrength"
    locks = "cmd:perm(Builder)"
    help_category = "Channeling"

    def func(self):
        caller = self.caller

        if not self.args or "=" not in self.args:
            caller.msg("Usage: +setstrength <target> = <1–15>")
            return

        lhs, rhs = [s.strip() for s in self.args.split("=", 1)]
        target = caller.search(lhs, global_search=True)
        if not target:
            return

        try:
            value = int(rhs)
            if value < 1 or value > 15:
                raise ValueError
        except ValueError:
            caller.msg("Value must be a number between 1 and 15.")
            return

        target.db.power_strength = value
        caller.msg(f"Set One Power Strength for {target.key} to {value}.")

# ----------------------------------
# Set One Power Control
# ----------------------------------

class CmdSetControl(Command):
    """
    +setcontrol <target> = <value>
    Set a character's One Power control level (1–5).
    """
    key = "+setcontrol"
    locks = "cmd:perm(Builder)"
    help_category = "Channeling"

    def func(self):
        caller = self.caller

        if not self.args or "=" not in self.args:
            caller.msg("Usage: +setcontrol <target> = <1–5>")
            return

        lhs, rhs = [s.strip() for s in self.args.split("=", 1)]
        target = caller.search(lhs, global_search=True)
        if not target:
            return

        try:
            value = int(rhs)
            if value < 1 or value > 5:
                raise ValueError
        except ValueError:
            caller.msg("Value must be a number between 1 and 5.")
            return

        target.db.control = value
        caller.msg(f"Set Control for {target.key} to {value}.")

# ----------------------------------
# Set Channeling Gender
# ----------------------------------

class CmdSetChannelGender(Command):
    """
    +setchannelgender <target> = <male/female>
    Set a character's channeling gender (used for +sense).
    """
    key = "+setchannelgender"
    locks = "cmd:perm(Builder)"
    help_category = "Channeling"

    def func(self):
        caller = self.caller

        if not self.args or "=" not in self.args:
            caller.msg("Usage: +setchannelgender <target> = <male/female>")
            return

        lhs, rhs = [s.strip().lower() for s in self.args.split("=", 1)]
        if rhs not in ("male", "female"):
            caller.msg("Value must be 'male' or 'female'.")
            return

        target = caller.search(lhs, global_search=True)
        if not target:
            return

        target.db.channeling_gender = rhs
        caller.msg(f"Set channeling gender for {target.key} to {rhs}.")

# ----------------------------------
# Set Elemental Affinities
# ----------------------------------

class CmdSetAffinity(Command):
    """
    +setaffinity <target>/<element> = <value>
    Set affinity value for a single element (1–5).
    """
    key = "+setaffinity"
    locks = "cmd:perm(Builder)"
    help_category = "Channeling"

    def func(self):
        caller = self.caller

        if not self.args or "=" not in self.args or "/" not in self.args:
            caller.msg("Usage: +setaffinity <target>/<element> = <1–5>")
            return

        target_part, rhs = [s.strip() for s in self.args.split("=", 1)]
        target_name, element = [s.strip().capitalize() for s in target_part.split("/", 1)]
        target = caller.search(target_name, global_search=True)
        if not target:
            return

        if element not in ("Air", "Water", "Fire", "Earth", "Spirit"):
            caller.msg("Element must be one of: Air, Water, Fire, Earth, Spirit.")
            return

        try:
            value = int(rhs)
            if value < 0 or value > 5:
                raise ValueError
        except ValueError:
            caller.msg("Affinity must be a number between 0 and 5.")
            return

        affinities = target.db.affinities or {}
        affinities[element] = value
        target.db.affinities = affinities
        caller.msg(f"Set {element} affinity for {target.key} to {value}.")
