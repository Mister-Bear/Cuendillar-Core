from evennia import Command

# Full Master Skills List
skills = [
    # Warrior Skills
    {"name": "Swordplay", "type": "Common", "role": "Warrior"},
    {"name": "Archery", "type": "Common", "role": "Warrior"},
    {"name": "Shield Defense", "type": "Common", "role": "Warrior"},
    {"name": "Mounted Combat", "type": "Common", "role": "Warrior"},
    {"name": "Tactics", "type": "Common", "role": "Warrior"},

    # Rogue Skills
    {"name": "Stealth", "type": "Common", "role": "Rogue"},
    {"name": "Thievery", "type": "Common", "role": "Rogue"},
    {"name": "Acrobatics", "type": "Common", "role": "Rogue"},
    {"name": "Poisons", "type": "Common", "role": "Rogue"},
    {"name": "Disguise", "type": "Common", "role": "Rogue"},

    # Channeler Skills
    {"name": "Weaving", "type": "Common", "role": "Channeler"},
    {"name": "Linking", "type": "Common", "role": "Channeler"},
    {"name": "Warding", "type": "Common", "role": "Channeler"},
    {"name": "Healing", "type": "Common", "role": "Channeler"},
    {"name": "Reading Residues", "type": "Common", "role": "Channeler"},

    # Scholar Skills
    {"name": "History", "type": "Common", "role": "Scholar"},
    {"name": "Investigation", "type": "Common", "role": "Scholar"},
    {"name": "Herbalism", "type": "Common", "role": "Scholar"},
    {"name": "Cartography", "type": "Common", "role": "Scholar"},
    {"name": "Languages", "type": "Common", "role": "Scholar"},

    # Faction-Locked: Warder
    {"name": "Warder Bond", "type": "Faction", "role": "Warder"},
    {"name": "Warder Tactics", "type": "Faction", "role": "Warder"},

    # Faction-Locked: Aes Sedai
    {"name": "Aes Sedai Etiquette", "type": "Faction", "role": "AesSedai"},
    {"name": "Tower Politics", "type": "Faction", "role": "AesSedai"},

    # Faction-Locked: Kin
    {"name": "Hidden Kin Networks", "type": "Faction", "role": "Kin"},
    {"name": "Potioncraft", "type": "Faction", "role": "Kin"},

    # Faction-Locked: Forsaken
    {"name": "True Power Affinity", "type": "Faction", "role": "Forsaken"},
    {"name": "Shadow Schemes", "type": "Faction", "role": "Forsaken"},
]

class CmdSkills(Command):
    """
    View available skills to learn.

    Usage:
      +skills
    """

    key = "+skills"
    locks = "cmd:all()"

    def func(self):
        caller = self.caller

        # Organize skills by type
        common_skills = []
        faction_skills = []

        for skill in skills:
            entry = f"{skill['name']} ({skill['role']})"
            if skill['type'] == "Common":
                common_skills.append(entry)
            elif skill['type'] == "Faction":
                faction_skills.append(entry)

        # Build output
        output = "=== COMMON SKILLS ===\n"
        output += "\n".join(common_skills) if common_skills else "None available."
        output += "\n\n=== FACTION-LOCKED SKILLS ===\n"
        output += "\n".join(faction_skills) if faction_skills else "None available."

        caller.msg(output)
