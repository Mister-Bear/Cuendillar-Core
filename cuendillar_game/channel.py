from evennia import Command
import random

# Weaves data
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

class CmdWeaves(Command):
    """
    +weaves

    Shows your available weaves categorized by level.
    """

    key = "+weaves"
    locks = "cmd:all()"
    help_category = "Channeling"

    def func(self):
        caller = self.caller
        text = "\n|cYour Known Weaves:|n\n"

        for tier, weaves in weaves_data.items():
            text += f"\n|w{tier} Level Weaves:|n\n"
            for weave in weaves:
                text += f"  - {weave}\n"

        caller.msg(text)

class CmdChannel(Command):
    """
    +channel <weave>

    Attempt to weave the One Power into an effect.
    """

    key = "+channel"
    locks = "cmd:all()"
    help_category = "Channeling"

    def func(self):
        caller = self.caller

        if not self.args:
            caller.msg("Usage: +channel <weave>")
            return

        weave = self.args.strip().title()

        # Check if the weave exists in the data
        known_weaves = [w for weaves in weaves_data.values() for w in weaves]

        if weave not in known_weaves:
            caller.msg(f"You don't know a weave called '{weave}'.")
            return

        # Check if the caller has channeling stats
        strength = caller.db.strength if caller.db.strength else 0
        control = caller.db.control if caller.db.control else 0

        if strength == 0 or control == 0:
            caller.msg("You do not seem to have the ability to channel the One Power.")
            return

        # Roll dice!
        roll = random.randint(1, 10)
        total = roll + strength + control

        # Simple success threshold (for now)
        difficulty = 15

        caller.msg(f"You attempt to weave |c{weave}|n...")
        caller.msg(f"(Roll: {roll} + Strength {strength} + Control {control} = {total})")

        if total >= difficulty:
            caller.msg(f"|gSuccess!|n Your {weave} weaves into reality!")
        else:
            caller.msg(f"|rFailure!|n Your {weave} slips away before it can form properly.")
