from evennia import Command
import random

# -------------------------------------
# CmdWeaves - Shows the Weaves List
# -------------------------------------

class CmdWeaves(Command):
    """
    +weaves

    Shows a list of all known weaves categorized by tier.
    """

    key = "+weaves"
    locks = "cmd:all()"
    help_category = "Channeling"

    def func(self):
        weaves_data = {
            "Novice": [
                "Light Sphere", "Minor Healing", "Warmth", "Air Push", "Water Shaping",
                "Earth Ripple", "Fire Spark", "Spirit Touch", "Thread Detection", "Voice Amplify"
            ],
            "Trained": [
                "Light Beam", "Mend Wound", "Heat Wave", "Air Cushion", "Purify Water",
                "Stone Shield", "Ignite", "Spirit Ward", "Weave Mask", "Silence Bubble"
            ],
            "Expert": [
                "Blinding Flash", "Restore Health", "Control Temperature", "Air Wall", "Summon Rain",
                "Earth Bind", "Fireball", "Shielding", "Mask Emotions", "Dreamwalk Anchor"
            ],
            "Aes Sedai": [
                "True Healing", "Severing", "Balefire", "Compulsion", "Earthquake",
                "Firestorm", "Floodcall", "Gateway", "Warding", "Dream Trap"
            ],
            "Lost": [
                "Mirror of Mists", "Tel'aran'rhiod Shift", "Call Lightning", "Age Regression", "Pattern Echo",
                "Unweaving", "Reality Fracture", "Reverse Balefire", "Weave Resurrection", "True Shield"
            ]
        }

        text = "|wYour Known Weaves:|n\n\n"
        for tier, weaves in weaves_data.items():
            text += f"|c{tier} Level Weaves:|n\n"
            for weave in weaves:
                text += f"  - {weave}\n"
            text += "\n"

        self.caller.msg(text)

# -------------------------------------
# CmdChannel - Channel a Weave at a Target
# -------------------------------------

class CmdChannel(Command):
    """
    +channel <target> = <weave>

    Attempts to channel a weave at a target using Power Strength + Control.
    """

    key = "+channel"
    locks = "cmd:all()"
    help_category = "Channeling"

    def parse(self):
        if "=" in self.args:
            self.targetname, self.weavename = [part.strip() for part in self.args.split("=", 1)]
        else:
            self.targetname = None
            self.weavename = self.args.strip()

    def func(self):
        caller = self.caller

        # Check basic input
        if not self.targetname or not self.weavename:
            caller.msg("|rUsage: +channel <target> = <weave>|n")
            return

        target = caller.search(self.targetname)
        if not target:
            caller.msg(f"|rNo target found matching '{self.targetname}'.|n")
            return

        # Check that caller has power attributes
        strength = caller.db.power_strength or 0
        control = caller.db.control or 0

        if strength <= 0 or control <= 0:
            caller.msg("|rYou are not a channeler or have no control over the One Power.|n")
            return

        # Check that the weave exists
        known_weaves = (
            "Light Sphere Minor Healing Warmth Air Push Water Shaping Earth Ripple Fire Spark Spirit Touch Thread Detection Voice Amplify "
            "Light Beam Mend Wound Heat Wave Air Cushion Purify Water Stone Shield Ignite Spirit Ward Weave Mask Silence Bubble "
            "Blinding Flash Restore Health Control Temperature Air Wall Summon Rain Earth Bind Fireball Shielding Mask Emotions Dreamwalk Anchor "
            "True Healing Severing Balefire Compulsion Earthquake Firestorm Floodcall Gateway Warding Dream Trap "
            "Mirror of Mists Tel'aran'rhiod Shift Call Lightning Age Regression Pattern Echo Unweaving Reality Fracture Reverse Balefire Weave Resurrection True Shield"
        ).split()

        if self.weavename not in known_weaves:
            caller.msg(f"|rUnknown weave '{self.weavename}'.|n")
            return

        # Perform channeling roll
        roll = random.randint(1, 10)
        total = roll + strength + control

        caller.msg(f"|cYou attempt to weave {self.weavename} at {target.key}!|n")
        caller.msg(f"You roll: {roll} + Strength ({strength}) + Control ({control}) = Total {total}")

        # Simple success/failure check
        if total >= 15:
            caller.msg(f"|gSUCCESS!|n Your {self.weavename} successfully strikes {target.key}!")
            target.msg(f"|r{caller.key} channels {self.weavename} at you successfully!|n")
        elif total >= 10:
            caller.msg(f"|yPARTIAL SUCCESS!|n Your {self.weavename} hits {target.key} but is weakened.")
            target.msg(f"|y{caller.key}'s {self.weavename} grazes you with reduced effect.|n")
        else:
            caller.msg(f"|rFAILURE!|n Your {self.weavename} fizzles before reaching {target.key}.")
            target.msg(f"{caller.key} tries to channel {self.weavename} at you but it fizzles uselessly.")

