from evennia import Command

class CmdCharSheetMain(Command):
    """
    +sheet

    View your complete character sheet.
    """
    key = "+sheet"
    help_category = "Character"

    def func(self):
        caller = self.caller

        sheet = []

        # CHARACTER INFO
        sheet.append("|w=== CHARACTER INFORMATION ===|n")
        sheet.append(f"Name: {caller.key}")
        sheet.append(f"Gender: {caller.db.gender or 'Unknown'}         Nation: {caller.db.origin or 'Unknown'}")
        sheet.append(f"Concept: {caller.db.concept or 'Unknown'}           Age: {caller.db.age or 'Unknown'}    Faction/Sect: {caller.db.faction or 'Unknown'}")
        sheet.append(f"XP Available: {caller.db.xp or 0}")

        # ATTRIBUTES
        sheet.append("\n|w=== ATTRIBUTES ===|n")
        attrs = caller.db.attributes or {}

        def stat_row(label, a, b, c):
            def dots(val): return "●" * val + "○" * (5 - val)
            return f"{label}: {a.upper()} {dots(attrs.get(a, 0))}  {b.upper()} {dots(attrs.get(b, 0))}  {c.upper()} {dots(attrs.get(c, 0))}"

        sheet.append(stat_row("Physical", "str", "dex", "sta"))
        sheet.append(stat_row("Mental", "per", "int", "wit"))
        sheet.append(stat_row("Social", "cha", "man", "com"))

        # ONE POWER STATS
        if caller.db.is_channeler:
            gender_power = caller.db.channeling_gender
            if gender_power == "male":
                header = "|w=== ONE POWER: SAIDIN ===|n"
            elif gender_power == "female":
                header = "|w=== ONE POWER: SAIDAR ===|n"
            else:
                header = "|w=== ONE POWER ===|n"

            strength = caller.db.power_strength or 0
            control = caller.db.control or 0
            affinities = caller.db.affinities or {}

            elements = ["Air", "Water", "Spirit", "Fire", "Earth"]
            display_affinities = []
            for element in elements:
                level = affinities.get(element, 0)
                dots = "●" * level + "○" * (5 - level)
                display_affinities.append(f"{element}: {dots}")

            sheet.append(f"\n{header}")
            sheet.append(f"Power Strength: {strength}")
            sheet.append(f"Control: {control}")
            sheet.append("Elemental Affinities:")
            sheet.extend(display_affinities)

        # ADVANTAGES
        sheet.append("\n|w=== ADVANTAGES ===|n")
        sheet.append(caller.db.advantages or "None")

        # FLAWS
        sheet.append("\n|w=== FLAWS ===|n")
        sheet.append(caller.db.flaws or "None")

        # EQUIPMENT
        sheet.append("\n|w=== EQUIPMENT ===|n")
        sheet.append(caller.db.equipment or "None")

        # NOTES
        sheet.append("\n|w=== PERSONAL NOTES ===|n")
        sheet.append(caller.db.notes or "None")

        caller.msg("\n".join(sheet))
