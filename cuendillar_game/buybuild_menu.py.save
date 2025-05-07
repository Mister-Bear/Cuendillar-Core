from evennia.utils.evmenu import EvMenu

# Entry point to start the menu
def start_buybuild(caller):
    EvMenu(caller, "char_gen.buybuild_menu", startnode="node_choose_class")

# Node 1: Choose class
def node_choose_class(caller):
    text = "|cChoose your class:|n\n\n"
    text += " 1) Channeler\n"
    text += " 2) Warrior\n"
    text += " 3) Rogue\n"
    text += " 4) Scholar\n"
    text += " 5) Performer\n"
    text += " 6) Merchant\n"
    text += "\nType the number of your choice."

    options = [
        {"key": "1", "desc": "Channeler", "goto": "node_assign_power_strength"},
        {"key": "2", "desc": "Warrior", "goto": "node_assign_str"},
        {"key": "3", "desc": "Rogue", "goto": "node_assign_str"},
        {"key": "4", "desc": "Scholar", "goto": "node_assign_str"},
        {"key": "5", "desc": "Performer", "goto": "node_assign_str"},
        {"key": "6", "desc": "Merchant", "goto": "node_assign_str"},
    ]
    return text, options

# Node 2: Assign Power Strength (Channeler only)
def node_assign_power_strength(caller, raw_input, **kwargs):
    caller.ndb.buybuild_data = caller.ndb.buybuild_data or {}
    caller.ndb.buybuild_data["class"] = "Channeler"
    caller.ndb.buybuild_data["power_strength"] = 5

    text = (
        "You selected: |cChanneler|n.\n"
        "Power Strength has been temporarily set to |w5|n.\n"
        "Next, assign your Control (1–5):"
    )
    options = [{"key": "_default", "goto": "node_assign_control"}]
    return text, options

# Node 3: Assign Control (Channeler)
def node_assign_control(caller, raw_input, **kwargs):
    if not raw_input:
        return "|cAssign your Control (1–5):|n", None

    try:
        val = int(raw_input.strip())
        if not (1 <= val <= 5):
            raise ValueError
    except ValueError:
        return "|rInvalid input.|n Enter a number between 1 and 5:", None

    caller.ndb.buybuild_data["power_control"] = val
    return (
        "|cAssign your elemental affinities (1–5 each):|n\n"
        "Format: air=3, water=5, earth=1, fire=2, spirit=4",
        "node_assign_affinities"
    )

# Node 4: Assign Affinities (Channeler)
def node_assign_affinities(caller, raw_input, **kwargs):
    if not raw_input:
        return (
            "|cAssign your elemental affinities (1–5 each):|n\n"
            "Format: air=3, water=5, earth=1, fire=2, spirit=4",
            None
        )

    input_data = raw_input.lower().split(",")
    allowed = {"air", "water", "earth", "fire", "spirit"}
    affinities = {}

    for item in input_data:
        if "=" not in item:
            return "|rInvalid format.|n Use air=3, water=5, etc.", None
        key, val = item.strip().split("=", 1)
        key = key.strip()
        val = val.strip()
        if key not in allowed:
            return f"|rInvalid element: {key}|n", None
        try:
            val = int(val)
            if not (1 <= val <= 5):
                raise ValueError
        except ValueError:
            return f"|rAffinity for {key} must be between 1 and 5.|n", None
        affinities[key] = val

    if set(affinities.keys()) != allowed:
        missing = allowed - set(affinities.keys())
        return f"|rMissing elements: {', '.join(missing)}|n", None

    caller.ndb.buybuild_data["affinities"] = affinities
    return "|cAssign a value for STR (1–10):|n", "node_assign_str"

# Node 5: Assign STR (All classes)
def node_assign_str(caller, raw_input, **kwargs):
    if not raw_input:
        return "|cAssign a value for STR (1–10):|n", None

    try:
        val = int(raw_input.strip())
        if not (1 <= val <= 10):
            raise ValueError
    except ValueError:
        return "|rInvalid input.|n Enter a number between 1 and 10:", None

    caller.ndb.buybuild_data = caller.ndb.buybuild_data or {}
    caller.ndb.buybuild_data["str"] = val

    data = caller.ndb.buybuild_data
    summary = (
        f"|gCharacter build complete!|n\n\n"
        f"|cClass|n: {data.get('class', '-')}\n"
    )
    if data.get("class") == "Channeler":
        summary += (
            f"|cPower Strength|n: {data.get('power_strength', '-')}\n"
            f"|cControl|n: {data.get('power_control', '-')}\n"
            f"|cAffinities|n:\n"
        )
        for key, val in data.get("affinities", {}).items():
            summary += f"  {key.title()}: {val}\n"

    summary += f"|cSTR|n: {data.get('str', '-')}"
    return summary, None
